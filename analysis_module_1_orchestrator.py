"""Analysis Module Orchestrator 

This module is responsible for:
1. Receiving the analysis plan from the planning module
2. Splitting information needs by data source
3. Creating parallel sub-graphs (one per data source) for info gathering
4. Aggregating results (fan-in)
5. Evaluating completeness
6. Optionally refining or proceeding to execution sub-graph

Flow (High-level):
    START
      ↓
    parse_information_needs   # Node: parse and group data by source
      ↓
    parallel_subgraphs        # Parallel execution of sub-graphs (10k, web, etc.)
      ↓
    aggregate_results         # Fan-in aggregator merges partial results
      ↓
    evaluate_completeness     # LLM check
      ↓
    fill_plan_with_results    # LLM merges final data into plan (optional step)
      ↓
    check_evaluation          # If met, proceed to execution
      ↓
    execute_plan              # Step-by-step execution sub-graph
      ↓
    END
"""

import os
import json
import time
import logging
import importlib
from typing import TypedDict, Any, List, Dict, Literal
from datetime import datetime

import google.generativeai as genai
from langgraph.graph.state import StateGraph, START, END
from langchain_core.runnables import RunnableConfig
from langgraph.types import Command

# Import the single execution module
from analysis_module_3_single import build_single_call_execution_graph, SingleExecutorState

# ----------------------------------------------------------------------------
# 1. Configuration and Type Definitions
# ----------------------------------------------------------------------------

class MarkdownLogger:
    """Utility class to generate a markdown log of the orchestrator's execution."""
    def __init__(self, company_name: str):
        self.company_name = company_name
        self.sections = []
        self.current_section = None
        self.start_time = datetime.now()
        
        # Start the document
        self.add_header(f"Analysis Orchestrator Report - {company_name}", level=1)
        self.add_text(f"Generated on: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    def add_header(self, text: str, level: int = 2):
        """Add a markdown header."""
        self.sections.append(f"\n{'#' * level} {text}\n")
    
    def add_text(self, text: str):
        """Add plain text."""
        self.sections.append(f"\n{text}\n")
    
    def add_code(self, code: str, language: str = ""):
        """Add a code block."""
        self.sections.append(f"\n```{language}\n{code}\n```\n")
    
    def add_list(self, items: List[str], ordered: bool = False):
        """Add a list of items."""
        for i, item in enumerate(items, 1):
            prefix = f"{i}." if ordered else "-"
            self.sections.append(f"{prefix} {item}\n")
    
    def start_section(self, name: str):
        """Start a new section with timing."""
        self.add_header(name)
        self.current_section = name
        self.add_text(f"Started at: {datetime.now().strftime('%H:%M:%S')}")
    
    def end_section(self, status: str = "completed", error: str = None):
        """End the current section with timing and status."""
        if error:
            self.add_text(f"❌ Error: {error}")
        else:
            self.add_text(f"✅ Status: {status}")
        self.current_section = None
    
    def add_state_snapshot(self, state: Dict[str, Any], keys_to_show: List[str] = None):
        """Add a snapshot of the current state."""
        self.add_header("Current State", level=3)
        if keys_to_show:
            state_snapshot = {k: state.get(k) for k in keys_to_show if k in state}
        else:
            state_snapshot = state
        self.add_code(json.dumps(state_snapshot, indent=2), "json")
    
    def save(self):
        """Save the markdown log to a file."""
        # Create logs directory if it doesn't exist
        os.makedirs("logs", exist_ok=True)
        
        # Generate filename with timestamp
        timestamp = self.start_time.strftime("%Y%m%d_%H%M%S")
        filename = f"logs/orchestrator_report_{self.company_name.lower()}_{timestamp}.md"
        
        # Write the file
        with open(filename, "w") as f:
            f.write("\n".join(self.sections))
        
        return filename

# Global markdown logger instance
md_logger = None

DataSourceType = Literal["10k", "web"]

DATA_SOURCE_CONFIG = {
    "10k": {
        "module": "analysis_module_2_vectordb",
        "builder": "build_vectordb_retrieval_graph",
        "description": "Retrieves information from parsed 10-K documents using vector search"
    },
    "web": {
        "module": "analysis_module_2_web",
        "builder": "build_web_search_graph",
        "description": "Retrieves information from web sources using search APIs"
    }
}

class OrchestratorState(TypedDict):
    """State definition for the parallel orchestrator."""
    analysis_plan: Dict[str, Any]           # entire plan, from planning
    information_needs: List[Dict[str, str]] # info needs from plan
    # we store sub-states for parallel subgraphs
    sub_states: List[Dict[str, Any]]        # states for parallel processing
    subgraph_outputs: Dict[str, Dict[str, str]]  # e.g. {"10k": {...}, "web": {...}}
    gathered_results: Dict[str, str]        # merged results keyed by 'stored'
    processed_sources: List[DataSourceType]
    parallel_status: Dict[str, str]         # Track status of parallel processing
    error_states: Dict[str, List[str]]      # Track errors in parallel processing
    
    metrics: Dict[str, Any]                 # optional tracking
    execution_output: Dict[str, str]        # Contains 'detailed' and 'summary' from single executor

# ----------------------------------------------------------------------------
# 2. Node A: parse_information_needs (Fan-Out Preparation)
# ----------------------------------------------------------------------------

def parse_information_needs(state: OrchestratorState) -> Command:
    """Extract the list of info needs and group them by data source. We'll store them for parallel usage."""
    global md_logger
    md_logger.start_section("Parse Information Needs")
    
    plan = state.get("analysis_plan", {})
    state["information_needs"] = plan.get("informationNeeds", [])
    state["subgraph_outputs"] = {}
    state["gathered_results"] = {}
    state["processed_sources"] = []
    state["parallel_status"] = {}  # Initialize empty
    state["error_states"] = {}     # Initialize empty
    state["execution_output"] = {"detailed": "", "summary": ""}
    
    # Log the information needs
    md_logger.add_header("Information Needs", level=3)
    for i, need in enumerate(state["information_needs"], 1):
        md_logger.add_text(f"**Need {i}:**")
        md_logger.add_list([
            f"Summary: {need['summary']}",
            f"Description: {need['description']}",
            f"Data Source: {need['dataSource']}",
            f"Tag: {need['tag']}"
        ])
    
    md_logger.end_section()
    return Command(
        update=state,
        goto="route_and_fanout"
    )

# ----------------------------------------------------------------------------
# 3. Node B: parallel_subgraphs (Fan-Out)
# ----------------------------------------------------------------------------

def parallel_subgraphs(state: OrchestratorState) -> Command:
    """
    This is the parallel processor function:
    - Each sub-state is assigned to a single data source.
    - We'll run that data source's subgraph, gather partial results, and store them in subgraph_outputs.
    """
    global md_logger
    md_logger.start_section("Parallel Subgraphs Processing")
    
    sub_states = state.get("sub_states", [])
    
    for sub_state in sub_states:
        source = sub_state.get("current_source", "")
        plan = sub_state["analysis_plan"]
        needs = sub_state["information_needs"]
        
        md_logger.add_header(f"Processing {source.upper()} Source", level=3)
        
        # Load the subgraph
        config_info = DATA_SOURCE_CONFIG.get(source)
        if not config_info:
            error_msg = f"Unknown data source: {source}"
            md_logger.add_text(f"❌ {error_msg}")
            state["parallel_status"][source] = "error"
            state["error_states"][source] = [error_msg]
            state["subgraph_outputs"][source] = {}
            continue
        
        try:
            module = importlib.import_module(config_info["module"])
            builder_func = getattr(module, config_info["builder"])
            retrieval_graph = builder_func()
            
            # Build subgraph state
            local_needs = [n for n in needs if n.get("dataSource") == source]
            subgraph_state = {
                "analysis_plan": plan,
                "information_needs": local_needs,
                "retrieved_text": {},
                "company_namespace": plan.get("company_namespace", ""),
                "parallel_status": {},
                "error_states": {}
            }
            
            md_logger.add_text(f"Invoking {source} subgraph with {len(local_needs)} information needs")
            
            # Invoke
            final_sub = retrieval_graph.invoke(subgraph_state)
            
            # Both web and vectordb now use retrieved_text format
            retrieved_text = final_sub.get("retrieved_text", {})
            state["subgraph_outputs"][source] = retrieved_text
            
            # Log search details if available (from vectordb)
            if source == "10k" and "search_details" in final_sub:
                search_details = final_sub["search_details"]
                md_logger.add_header(f"{source.upper()} Search Process", level=4)
                
                # Log metadata queries
                if "search_logs" in search_details:
                    md_logger.add_text("**Metadata Queries:**")
                    for query in search_details["search_logs"]["metadata_queries"]:
                        md_logger.add_code(json.dumps(query, indent=2), "json")
                    
                    md_logger.add_text("**Search Configurations:**")
                    for config in search_details["search_logs"]["search_configurations"]:
                        md_logger.add_code(json.dumps(config, indent=2), "json")
                    
                    md_logger.add_text("**Vector Searches:**")
                    for search in search_details["search_logs"]["vector_searches"]:
                        md_logger.add_code(json.dumps(search, indent=2), "json")
            
            # Log results for each need
            md_logger.add_header(f"{source.upper()} Results", level=4)
            for need in local_needs:
                stored_key = need["stored"]
                if stored_key in retrieved_text:
                    result_text = retrieved_text[stored_key]
                    preview = result_text[:200] + "..." if len(result_text) > 200 else result_text
                    md_logger.add_text(f"✅ Found results for '{need['summary']}':")
                    md_logger.add_code(preview)
                else:
                    md_logger.add_text(f"❌ No results for '{need['summary']}'")
            
            # Mark processed
            state["parallel_status"][source] = "completed"
            if source not in state["processed_sources"]:
                state["processed_sources"].append(source)
                
        except Exception as e:
            error_msg = f"Error with subgraph for {source}: {str(e)}"
            md_logger.add_text(f"❌ {error_msg}")
            logging.error(error_msg)
            state["parallel_status"][source] = "error"
            state["error_states"][source] = [error_msg]
            state["subgraph_outputs"][source] = {}
    
    md_logger.end_section()
    return Command(
        update=state,
        goto="aggregate_results"
    )

# ----------------------------------------------------------------------------
# 4. Node C: route_information_needs_and_fanout
# ----------------------------------------------------------------------------

def route_and_fanout(state: OrchestratorState) -> Command:
    """
    Creates a sub-state for each unique data source and fans them out in parallel.
    We'll return them as a list from the orchestrator perspective.
    """
    global md_logger
    md_logger.start_section("Route and Fan-out")
    
    # Identify distinct data sources
    data_sources = set(need.get("dataSource", "10k") for need in state["information_needs"])
    sub_states = []
    
    md_logger.add_text(f"Identified data sources: {', '.join(data_sources)}")
    
    for src in data_sources:
        new_state = dict(state)  # shallow copy
        new_state["current_source"] = src
        sub_states.append(new_state)
        # Initialize tracking for this source
        state["parallel_status"][src] = "pending"
        state["error_states"][src] = []
        md_logger.add_text(f"Created sub-state for source: {src}")
    
    md_logger.end_section()
    return Command(
        update={"sub_states": sub_states},
        goto="parallel_subgraphs"
    )

# ----------------------------------------------------------------------------
# 5. Node D: aggregate_results (Fan-In)
# ----------------------------------------------------------------------------

def aggregate_results(state: OrchestratorState) -> Command:
    """
    Merges partial results from each parallel sub-state into the main state.
    subgraph_outputs: { dataSource: { stored_key: text } }
    We'll combine them all into gathered_results (by stored key).
    """
    global md_logger
    md_logger.start_section("Aggregate Results")
    
    # Merge everything into state["gathered_results"]
    for source, src_dict in state["subgraph_outputs"].items():
        state["gathered_results"].update(src_dict)
        md_logger.add_text(f"Merged {len(src_dict)} results from {source}")
    
    # Log the final results summary
    md_logger.add_header("Results Summary", level=3)
    for need in state["information_needs"]:
        stored_key = need["stored"]
        if stored_key in state["gathered_results"]:
            result_text = state["gathered_results"][stored_key]
            preview = result_text[:200] + "..." if len(result_text) > 200 else result_text
            md_logger.add_text(f"**{need['summary']}**:")
            md_logger.add_code(preview)
        else:
            md_logger.add_text(f"**{need['summary']}**: No results found")
    
    md_logger.end_section()
    return Command(
        update=state,
        goto="fill_plan_with_results"
    )

# ----------------------------------------------------------------------------
# 6. Node E: evaluate_completeness (LLM-based)
# ----------------------------------------------------------------------------

# [Removed evaluate_completeness function]

# ----------------------------------------------------------------------------
# 7. Node F: fill_plan_with_results (Optional LLM Step)
# ----------------------------------------------------------------------------

def fill_plan_with_results(state: OrchestratorState) -> Command:
    """
    Non-LLM approach: Merge subgraph outputs into the plan's informationNeeds directly.
    We'll read the 'gathered_results' dict and store them in the plan under the matching item.
    The plan remains purely python-based, no generative step.
    """
    global md_logger
    md_logger.start_section("Fill Plan with Results")
    
    plan = state["analysis_plan"]
    gathered = state["gathered_results"]

    # For each info need, store the gathered results into the plan
    info_needs = plan.get("informationNeeds", [])
    for item in info_needs:
        stored_key = item.get("stored")
        if stored_key in gathered:
            item["analysisOutput"] = gathered[stored_key]
            md_logger.add_text(f"✅ Added output for: {item['summary']}")
        else:
            md_logger.add_text(f"❌ No output for: {item['summary']}")
    
    # Optionally update the plan
    state["analysis_plan"] = plan
    
    md_logger.end_section()
    return Command(
        update=state,
        goto="execute_plan"
    )

# ----------------------------------------------------------------------------
# 8. Node G: check_evaluation
# ----------------------------------------------------------------------------

# [Removed check_evaluation function]

# ----------------------------------------------------------------------------
# 9. Node H: execute_plan
# ----------------------------------------------------------------------------

def execute_plan(state: OrchestratorState) -> OrchestratorState:
    """
    Use the single-call execution module to process the analysis results.
    """
    global md_logger
    md_logger.start_section("Execute Plan")
    
    try:
        # Create single executor state
        executor_state: SingleExecutorState = {
            "analysis_plan": state["analysis_plan"],
            "information_needs": state["information_needs"],
            "gathered_results": state["gathered_results"],
            "execution_steps": state["analysis_plan"].get("executionPlan", []),
            "final_output_detailed": "",
            "final_output_summary": ""
        }
        
        # Build and run single execution graph
        execution_graph = build_single_call_execution_graph()
        md_logger.add_text("Starting single-call execution")
        
        final_exec = execution_graph.invoke(executor_state)
        
        # Store both detailed and summary outputs
        state["execution_output"] = {
            "detailed": final_exec["final_output_detailed"],
            "summary": final_exec["final_output_summary"]
        }
        
        if final_exec["final_output_detailed"]:
            md_logger.add_text("✅ Execution completed successfully")
            md_logger.add_header("Detailed Analysis", level=3)
            md_logger.add_text(final_exec["final_output_detailed"])
            md_logger.add_header("Summary", level=3)
            md_logger.add_text(final_exec["final_output_summary"])
        else:
            md_logger.add_text("⚠️ No execution output generated")
            
    except Exception as e:
        error_msg = f"Execution module error: {str(e)}"
        logging.error(error_msg)
        md_logger.add_text(f"❌ {error_msg}")
        state["execution_output"] = {
            "detailed": f"Error during execution: {str(e)}",
            "summary": "Execution failed"
        }
    
    md_logger.end_section()
    return state

# ----------------------------------------------------------------------------
# 10. Build Graph
# ----------------------------------------------------------------------------

def build_orchestration_graph() -> StateGraph:
    """
    Construct the orchestrator with:
      1. parse_information_needs
      2. route_and_fanout -> parallel_subgraphs -> aggregate_results
      3. fill_plan_with_results (merging subgraph results into plan)
      4. execute_plan
      5. END
    """
    builder = StateGraph(OrchestratorState)
    
    builder.add_node("parse_information_needs", parse_information_needs)
    builder.add_node("route_and_fanout", route_and_fanout)
    builder.add_node("parallel_subgraphs", parallel_subgraphs)
    builder.add_node("aggregate_results", aggregate_results)
    builder.add_node("fill_plan_with_results", fill_plan_with_results)
    builder.add_node("execute_plan", execute_plan)
    
    # Edges
    builder.add_edge(START, "parse_information_needs")
    builder.add_edge("parse_information_needs", "route_and_fanout")
    builder.add_edge("route_and_fanout", "parallel_subgraphs")
    builder.add_edge("parallel_subgraphs", "aggregate_results")
    builder.add_edge("aggregate_results", "fill_plan_with_results")
    builder.add_edge("fill_plan_with_results", "execute_plan")
    builder.add_edge("execute_plan", END)
    
    return builder.compile()

# ----------------------------------------------------------------------------
# 11. run_orchestration
# ----------------------------------------------------------------------------

def run_orchestration(analysis_plan: Dict[str, Any]) -> OrchestratorState:
    """
    Main entry point. We create initial orchestrator state and run the compiled graph.
    """
    global md_logger
    
    # Initialize markdown logger
    company_name = analysis_plan.get("company_namespace", "unknown")
    md_logger = MarkdownLogger(company_name)
    
    initial_state: OrchestratorState = {
        "analysis_plan": analysis_plan,
        "information_needs": analysis_plan.get("informationNeeds", []),
        "sub_states": [],
        "subgraph_outputs": {},
        "gathered_results": {},
        "processed_sources": [],
        "parallel_status": {},
        "error_states": {},
        "metrics": {},
        "execution_output": {"detailed": "", "summary": ""}
    }
    
    # Log initial state
    md_logger.add_header("Initial Configuration")
    md_logger.add_text("Analysis Plan Details:")
    md_logger.add_list([
        f"Analysis Type: {analysis_plan.get('analysisType', 'Not specified')}",
        f"Company Namespace: {analysis_plan.get('company_namespace', 'Not specified')}",
        f"Total Information Needs: {len(analysis_plan.get('informationNeeds', []))}"
    ])
    
    md_logger.add_header("Information Needs", level=3)
    for i, need in enumerate(analysis_plan.get("informationNeeds", []), 1):
        md_logger.add_text(f"\n**Information Need {i}:**")
        md_logger.add_list([
            f"Summary: {need.get('summary', 'Not specified')}",
            f"Description: {need.get('description', 'Not specified')}",
            f"Data Source: {need.get('dataSource', 'Not specified')}",
            f"Tag: {need.get('tag', 'Not specified')}",
            f"Storage Key: {need.get('stored', 'Not specified')}"
        ])
    
    # Run graph
    graph = build_orchestration_graph()
    final_state = graph.invoke(initial_state)
    
    # Log final state with detailed results
    md_logger.add_header("Final Results")
    
    # Log processing status
    md_logger.add_header("Processing Status", level=3)
    for source, status in final_state["parallel_status"].items():
        status_icon = "✅" if status == "completed" else "❌"
        md_logger.add_text(f"{status_icon} **{source.upper()}**: {status}")
        if source in final_state["error_states"] and final_state["error_states"][source]:
            md_logger.add_text("Errors:")
            for error in final_state["error_states"][source]:
                md_logger.add_text(f"- {error}")
    
    # Log results for each information need
    md_logger.add_header("Information Need Results", level=3)
    for need in final_state["analysis_plan"]["informationNeeds"]:
        stored_key = need["stored"]
        md_logger.add_text(f"\n**{need['summary']}** ({need['dataSource']})")
        md_logger.add_text(f"Query: {need['description']}")
        
        if stored_key in final_state["gathered_results"]:
            result_text = final_state["gathered_results"][stored_key]
            md_logger.add_text("Results:")
            md_logger.add_code(result_text)
        else:
            md_logger.add_text("❌ No results found")
    
    # Log final analysis plan state
    md_logger.add_header("Final Analysis Plan State", level=3)
    md_logger.add_code(json.dumps(final_state["analysis_plan"], indent=2), "json")
    
    report_file = md_logger.save()
    logging.info(f"Generated markdown report: {report_file}")
    
    return final_state

# ----------------------------------------------------------------------------
# 12. Example usage
# ----------------------------------------------------------------------------

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    # Test case: Analysis plan for NVIDIA
    company_name = "NVIDIA"
    # Generate clean namespace (lowercase alphanumeric only)
    namespace = company_name.lower()

    test_plan = {
        "analysisType": "Growth and Competition Analysis",
        "company_namespace": namespace,  # Add namespace to plan
        "informationNeeds": [
            {
                "summary": "Revenue Growth",
                "description": "Extract NVIDIA's revenue growth data and segment breakdown from recent quarters",
                "tag": "factual",
                "dataSource": "10k",
                "stored": "revenue_growth"
            },
            {
                "summary": "Market Competition",
                "description": "Find recent news and analysis about NVIDIA's competition in the AI chip market",
                "tag": "broad",
                "dataSource": "web",
                "stored": "market_competition"
            },
            {
                "summary": "Risk Factors",
                "description": "Identify key risk factors related to semiconductor supply chain and market competition",
                "tag": "analysis",
                "dataSource": "10k",
                "stored": "risk_factors"
            }
        ]
    }

    # Run orchestration
    try:
        logging.info("Starting orchestration test...")
        final_state = run_orchestration(test_plan)
        
        # Print results
        logging.info("\n=== Final Results ===")
        for need in test_plan["informationNeeds"]:
            stored_key = need["stored"]
            if stored_key in final_state.get("gathered_results", {}):
                print(f"\nResults for: {need['summary']}")
                print("-" * 50)
                print(final_state["gathered_results"][stored_key][:500] + "...")
            else:
                print(f"\nNo results found for: {need['summary']}")
        
    except Exception as e:
        logging.error(f"Orchestration failed: {str(e)}", exc_info=True)