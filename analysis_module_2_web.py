"""
Analysis Module 2 - Web Search

This module is responsible for retrieving information from web sources using search APIs.
"""

import os
import time
import json
import logging
from typing import TypedDict, Any, List, Dict, Optional
from datetime import datetime
import google.generativeai as genai
from exa_py import Exa
from langgraph.graph.state import StateGraph, START, END
from langchain_core.runnables import RunnableConfig
from langgraph.types import Command

###############################################################################
# 1. State Definitions
###############################################################################

class WebSearchNeed(TypedDict):
    """
    One item from 'information_needs' that has dataSource='web'.
    We'll store extra fields for intermediate steps if needed.
    """
    summary: str
    description: str
    tag: str
    dataSource: str
    stored: str

class WebSearchState(TypedDict):
    """
    Main state for the web search sub-graph.
    This matches the orchestrator's format for passing information needs.
    """
    # The full analysis plan
    analysis_plan: Dict[str, Any]

    # Web-based info needs
    information_needs: List[Dict[str, str]]

    # Storing final texts (keyed by 'stored' from each info need)
    retrieved_text: Dict[str, str]

    # Track parallel or item-by-item statuses
    parallel_status: Dict[int, str]  # e.g. { item_index: "pending" | "complete" | "error" }
    error_states: Dict[int, List[str]]  # e.g. { item_index: ["some error", "another error"] }
    done_count: int

    # Credentials
    exa_api_key: Optional[str]
    gemini_api_key: Optional[str]
    
    # Search logs
    search_logs: Dict[str, List[Dict[str, Any]]]  # Store detailed search process logs

def setup_logging():
    """Configure logging to write to both file and console with timestamps."""
    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"logs/web_search_{timestamp}.log"
    
    # Configure formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Configure file handler
    file_handler = logging.FileHandler(log_filename)
    file_handler.setFormatter(formatter)
    
    # Configure console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    # Get root logger and set level
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    
    # Remove existing handlers and add new ones
    root_logger.handlers = []
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
    
    logging.info(f"Logging initialized. Log file: {log_filename}")

###############################################################################
# 2. Node A - validate_credentials
###############################################################################

def validate_credentials(
    state: WebSearchState
) -> Any:
    """
    Checks environment variables for EXA_API_KEY.
    Also optionally checks GEMINI_API_KEY if we want to use Gemini for query transformation.
    If missing, logs an error and ends the sub-graph.
    """
    exa_api_key = os.getenv("EXA_API_KEY")
    gemini_api_key = os.getenv("GEMINI_API_KEY")

    if not exa_api_key:
        msg = "Missing EXA_API_KEY environment variable."
        logging.error(msg)
        # We can store an error or skip
        for i in range(len(state["information_needs"])):
            state["parallel_status"][i] = "error"
            state["error_states"][i].append(msg)
        return Command(update={}, goto=END)

    # If found, store them
    state["exa_api_key"] = exa_api_key
    # Optional
    if gemini_api_key:
        state["gemini_api_key"] = gemini_api_key
    
    # Initialize search logs
    state["search_logs"] = {
        "query_transformations": [],
        "search_queries": [],
        "retry_attempts": [],
        "final_results": []
    }

    # Next step
    return Command(
        update={
            "exa_api_key": exa_api_key,
            "gemini_api_key": gemini_api_key,
            "search_logs": state["search_logs"]
        },
        goto="parse_information_needs"
    )

###############################################################################
# 3. Node B - parse_information_needs
###############################################################################

def parse_information_needs(
    state: WebSearchState
) -> Any:
    """
    Sets up the parallel structures for each item in 'information_needs', marking them pending.
    """
    info_needs = state.get("information_needs", [])
    for i in range(len(info_needs)):
        state["parallel_status"][i] = "pending"
        state["error_states"][i] = []

    # done_count to 0
    state["done_count"] = 0

    # If no info needs, we just continue (the orchestrator won't typically pass us an empty list).
    if not info_needs:
        return Command(update={}, goto="compile_search_results")

    return Command(update={}, goto="transform_query_with_gemini")

###############################################################################
# 4. Node C - transform_query_with_gemini
###############################################################################

def transform_query_with_gemini(
    state: WebSearchState
) -> Any:
    """
    Optional step: Use Gemini to transform each query into a better web search query.
    If no Gemini API key, we'll skip transformation and use original queries.
    """
    gemini_api_key = state.get("gemini_api_key")
    needs = state["information_needs"]

    if not gemini_api_key:
        logging.info("No Gemini API key found, using original queries")
        for need in needs:
            need["transformed_query"] = need["description"]
        return Command(update={}, goto="exa_search")

    # Configure Gemini
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    for i, need in enumerate(needs):
        original_query = need["description"]
        logging.info(f"\nTransforming query {i+1}: {original_query[:100]}...")

        try:
            prompt = (
                "You are a search query optimization expert. Transform this information need into "
                "an effective web search query that will find recent, relevant information:\n\n"
                f"Information Need: {original_query}\n\n"
                "Return only the transformed search query, nothing else."
            )

            response = model.generate_content(
                contents=prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.2,
                    max_output_tokens=100
                )
            )

            transformed = response.text.strip()
            need["transformed_query"] = transformed

            # Log transformation
            state["search_logs"]["query_transformations"].append({
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "original_query": original_query,
                "transformed_query": transformed,
                "info_need_summary": need["summary"]
            })

            logging.info(f"Original: {original_query[:100]}...")
            logging.info(f"Transformed: {transformed[:100]}...")

        except Exception as e:
            error_msg = f"Query transformation failed: {str(e)}"
            logging.error(error_msg)
            need["transformed_query"] = original_query
            state["error_states"][i].append(error_msg)

    return Command(update={}, goto="exa_search")

###############################################################################
# 5. Node D - exa_search
###############################################################################

def exa_search(
    state: WebSearchState
) -> Any:
    """
    Perform the actual Exa search. We'll do a single pass for each info need in parallel.
    - If we see a rate-limit error, store it and mark that item for retry.
    - We'll store results in something like item["exa_results"] or directly in final state["retrieved_text"]?
    For the aggregator approach, let's store partial in item["exa_results"].
    """
    exa_api_key = state.get("exa_api_key")

    # We assume the user has exa_py installed
    try:
        from exa_py import Exa
    except ImportError:
        msg = "exa_py library not installed. Please install exa_py to proceed."
        logging.error(msg)
        for i in range(len(state["information_needs"])):
            state["parallel_status"][i] = "error"
            state["error_states"][i].append(msg)
        return Command(update={}, goto="compile_search_results")

    exa = Exa(api_key=exa_api_key)
    needs = state["information_needs"]

    for i, need in enumerate(needs):
        # If we already have an error or something, skip
        if state["parallel_status"][i] == "error":
            continue

        # Build the final query from 'transformed_query'
        qtext = need.get("transformed_query", need["description"])
        logging.info(f"\nExecuting search {i+1} for: {qtext[:100]}...")

        try:
            # Log search attempt
            search_log = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "info_need_summary": need["summary"],
                "query": qtext,
                "search_config": {
                    "type": "neural",
                    "use_autoprompt": False,
                    "num_results": 3
                }
            }

            results = exa.search_and_contents(
                qtext,
                type="neural",
                use_autoprompt=False,
                text=True,
                num_results=3,
            )

            # Process results
            snippet_list = []
            for r in results.results:
                snippet = f"Title: {r.title}\nURL: {r.url}\nSnippet: {r.text[:300]}..."
                snippet_list.append(snippet)

            final_text = "\n\n---\n\n".join(snippet_list) if snippet_list else "No results found."
            need["exa_results"] = final_text
            state["parallel_status"][i] = "completed"

            # Update search log with results
            search_log["results_found"] = len(snippet_list)
            search_log["result_previews"] = [
                {
                    "title": r.title,
                    "url": r.url,
                    "text_preview": r.text[:200] + "..."
                }
                for r in results.results
            ]
            state["search_logs"]["search_queries"].append(search_log)

            logging.info(f"Found {len(snippet_list)} results")

        except Exception as e:
            err_str = str(e).lower()
            if "429" in err_str or "rate limit" in err_str:
                state["parallel_status"][i] = "retry"
                error_msg = f"Rate-limit encountered. Will retry: {str(e)}"
                state["error_states"][i].append(error_msg)
                logging.warning(error_msg)
            else:
                state["parallel_status"][i] = "error"
                error_msg = str(e)
                state["error_states"][i].append(error_msg)
                logging.error(f"Search error: {error_msg}")

            # Log error in search logs
            search_log["error"] = error_msg
            state["search_logs"]["search_queries"].append(search_log)

    return Command(update={}, goto="retry_failed_searches")

###############################################################################
# 6. Node E - retry_failed_searches
###############################################################################

def retry_failed_searches(
    state: WebSearchState
) -> Any:
    """
    Check for any items marked for retry (rate-limits, etc).
    We'll do a single retry pass with some delay.
    """
    exa = Exa(api_key=state["exa_api_key"])
    needs = state["information_needs"]

    # Find items marked for retry
    retry_indices = [
        i for i, status in state["parallel_status"].items()
        if status == "retry"
    ]

    if not retry_indices:
        return Command(update={}, goto="compile_search_results")

    logging.info(f"\nRetrying {len(retry_indices)} failed searches...")
    time.sleep(5)  # wait 5 seconds

    for i in retry_indices:
        need = needs[i]
        qtext = need.get("transformed_query", need["description"])
        
        try:
            # Log retry attempt
            retry_log = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "info_need_summary": need["summary"],
                "query": qtext,
                "original_error": state["error_states"][i][-1] if state["error_states"][i] else None
            }

            results = exa.search_and_contents(
                qtext,
                type="neural",
                use_autoprompt=False,
                text=True,
                num_results=3
            )

            snippet_list = []
            for r in results.results:
                snippet = f"Title: {r.title}\nURL: {r.url}\nSnippet: {r.text[:300]}..."
                snippet_list.append(snippet)

            final_text = "\n\n---\n\n".join(snippet_list) if snippet_list else "No results found."
            need["exa_results"] = final_text
            state["parallel_status"][i] = "completed"

            # Update retry log with results
            retry_log["success"] = True
            retry_log["results_found"] = len(snippet_list)
            retry_log["result_previews"] = [
                {
                    "title": r.title,
                    "url": r.url,
                    "text_preview": r.text[:200] + "..."
                }
                for r in results.results
            ]

            logging.info(f"Retry successful for query {i+1}. Found {len(snippet_list)} results")

        except Exception as e:
            err_str = str(e).lower()
            if "429" in err_str or "rate limit" in err_str:
                state["parallel_status"][i] = "error"
                error_msg = "Rate-limit again. Aborting item."
                state["error_states"][i].append(error_msg)
                logging.error(error_msg)
            else:
                state["parallel_status"][i] = "error"
                error_msg = str(e)
                state["error_states"][i].append(error_msg)
                logging.error(f"Retry failed: {error_msg}")

            # Update retry log with error
            retry_log["success"] = False
            retry_log["error"] = error_msg

        # Add retry log
        state["search_logs"]["retry_attempts"].append(retry_log)

    return Command(update={}, goto="compile_search_results")

###############################################################################
# 7. Node F - compile_search_results
###############################################################################

def compile_search_results(
    state: WebSearchState
) -> WebSearchState:
    """
    For each info need, take item['exa_results'] (if any) and place it in
    state["retrieved_text"][need["stored"]] = ...
    If an item is in error or no result, set an empty or error message.
    """
    needs = state["information_needs"]
    
    # Log final results compilation
    for i, need in enumerate(needs):
        result_log = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "info_need_summary": need["summary"],
            "status": state["parallel_status"][i],
            "errors": state["error_states"].get(i, [])
        }

        # If completed, we have exa_results
        if state["parallel_status"][i] == "completed":
            text_val = need.get("exa_results", "")
            state["retrieved_text"][need["stored"]] = text_val
            result_log["has_results"] = bool(text_val)
            result_log["text_preview"] = text_val[:200] + "..." if text_val else ""
        else:
            # error or skip
            errs = state["error_states"][i]
            if errs:
                error_msg = f"Error or no data. Errors: {errs}"
                state["retrieved_text"][need["stored"]] = error_msg
                result_log["error_message"] = error_msg
            else:
                state["retrieved_text"][need["stored"]] = "No data found."
                result_log["error_message"] = "No data found"

        # Add to final results log
        state["search_logs"]["final_results"].append(result_log)
        
        # Log summary
        if state["parallel_status"][i] == "completed":
            logging.info(f"\n✅ Results compiled for: {need['summary']}")
        else:
            logging.error(f"\n❌ Failed to get results for: {need['summary']}")
            for error in state["error_states"].get(i, []):
                logging.error(f"  Error: {error}")

    # Save detailed search logs to file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"logs/web_search_details_{timestamp}.json"
    
    with open(log_file, "w") as f:
        json.dump(state["search_logs"], f, indent=2)
    
    logging.info(f"\nDetailed search logs saved to: {log_file}")

    return state

###############################################################################
# 8. Graph Construction
###############################################################################
def build_web_search_graph() -> StateGraph:
    """
    Build and compile the sub-graph for web searching via Exa.
    """
    builder = StateGraph(WebSearchState)

    builder.add_node("validate_credentials", validate_credentials)
    builder.add_node("parse_information_needs", parse_information_needs)
    builder.add_node("transform_query_with_gemini", transform_query_with_gemini)
    builder.add_node("exa_search", exa_search)
    builder.add_node("retry_failed_searches", retry_failed_searches)
    builder.add_node("compile_search_results", compile_search_results)

    # Edges
    builder.add_edge(START, "validate_credentials")
    builder.add_edge("validate_credentials", "parse_information_needs")
    builder.add_edge("parse_information_needs", "transform_query_with_gemini")
    builder.add_edge("transform_query_with_gemini", "exa_search")
    builder.add_edge("exa_search", "retry_failed_searches")
    builder.add_edge("retry_failed_searches", "compile_search_results")
    builder.add_edge("compile_search_results", END)

    return builder.compile()

###############################################################################
# Example usage
###############################################################################
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Example plan matching orchestrator format
    test_plan = {
        "analysisType": "Market Analysis",
        "informationNeeds": [
            {
                "summary": "Competitor Websites",
                "description": "Find me links or references to top e-commerce competitors in the apparel industry",
                "tag": "broad",
                "dataSource": "web",
                "stored": "competitor_websites"
            },
            {
                "summary": "Recent Tech Innovations",
                "description": "What are some recent technology innovations in manufacturing from major supply chain providers",
                "tag": "broad",
                "dataSource": "web",
                "stored": "tech_innovations"
            }
        ]
    }

    # Build state matching orchestrator's format
    initial_state: WebSearchState = {
        "analysis_plan": test_plan,
        "information_needs": test_plan["informationNeeds"],
        "retrieved_text": {},
        "parallel_status": {},
        "error_states": {},
        "done_count": 0,
        "exa_api_key": None,
        "gemini_api_key": None
    }

    # Build graph
    graph = build_web_search_graph()

    # Run
    final_state = graph.invoke(initial_state)
    logging.info("=== Web Search Results ===")
    for k, v in final_state["retrieved_text"].items():
        logging.info(f"\nStored Key: {k}\nValue:\n{v}\n{'='*50}")