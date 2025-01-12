"""
Analysis Module 3 - Single Executor

This module performs a single Gemini LLM call to combine the plan, information needs, 
and execution steps into a single comprehensive analysis output with source references.
"""

import os
import json
import time
import logging
import google.generativeai as genai
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from typing import TypedDict, Any, List, Dict
from langgraph.graph.state import StateGraph, START, END
from langchain_core.runnables import RunnableConfig

class SingleExecutorState(TypedDict):
    """State for the single-call executor"""
    analysis_plan: Dict[str, Any]
    information_needs: List[Dict[str, Any]]
    gathered_results: Dict[str, Any]
    execution_steps: List[Dict[str, Any]]
    final_output_detailed: str
    final_output_summary: str

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10),
    retry=retry_if_exception_type(Exception),
    reraise=True
)
def call_gemini_with_retry(model: Any, prompt: str) -> str:
    """Call Gemini API with retry logic"""
    try:
        start_time = time.time()
        response = model.generate_content(
            contents=prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.7,
                max_output_tokens=2048
            )
        )
        elapsed_time = time.time() - start_time
        logging.info(f"Gemini API call completed in {elapsed_time:.2f} seconds")
        return response.text.strip()
    except Exception as e:
        logging.error(f"Unexpected error in Gemini API call: {str(e)}")
        raise

def single_call_executor(
    state: SingleExecutorState,
    config: RunnableConfig
) -> Any:
    """
    Makes one Gemini LLM call that:
    - Receives the entire plan, information needs, gathered results, and execution steps
    - Produces comprehensive analysis with source references
    - Documents the execution process and reasoning
    """
    gemini_api_key = os.getenv("GEMINI_API_KEY", "")
    if not gemini_api_key:
        logging.warning("No GEMINI_API_KEY found. Cannot call Gemini. Returning placeholders.")
        state["final_output_detailed"] = "GEMINI_API_KEY missing. No LLM call executed."
        state["final_output_summary"] = "No summary available."
        return state

    # Configure generative AI
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Build the prompt
    analysis_plan_json = json.dumps(state["analysis_plan"], indent=2)
    information_needs_json = json.dumps(state["information_needs"], indent=2)
    gathered_results_json = json.dumps(state["gathered_results"], indent=2)
    execution_steps_json = json.dumps(state["execution_steps"], indent=2)

    prompt = f"""You are a highly sophisticated AI analyst tasked with producing a comprehensive analysis report.

AVAILABLE DATA:
1) Analysis Plan (JSON):
{analysis_plan_json}

2) Information Needs (JSON):
{information_needs_json}

3) Gathered Results (JSON):
{gathered_results_json}

4) Execution Steps (JSON):
{execution_steps_json}

YOUR TASK:
Produce a comprehensive analysis report in markdown format with the following sections:

# Main Analysis
- Thoroughly analyze all gathered data
- Identify key patterns, trends, and insights
- Draw meaningful conclusions
- Use superscript numbers to reference sources (e.g., "Revenue grew by 25%[1] while market share expanded[2]")
- Each distinct piece of information should have a source reference
- When combining multiple sources, use multiple references (e.g., "Market dynamics[1,2,3] suggest...")

# Execution Process Documentation
- Document how each execution step was performed
- Explain the reasoning behind key analytical decisions
- Note any data transformations or special processing
- Highlight important findings from each step
- Document any assumptions or limitations
- Include source references for key decisions and findings

# Limitations and Assumptions
- Document any important caveats or assumptions
- Note data limitations or potential biases
- Include source references for key limitations

# Sources and References
For each source used, provide:
- [1] Source Type: (10K/Web/etc)
  - Information: What information was provided
  - Relevance: How it was used in the analysis
  - Limitations: Any biases or limitations

# Summary
A concise summary of key findings and recommendations.

IMPORTANT:
- Be thorough but clear in your analysis
- Maintain professional analytical tone
- Focus on actionable insights
- Document your process clearly
- Be meticulous with source references
- Ensure every claim has a source reference
- Cross-reference sources when possible

Return your analysis in markdown format with all the sections above."""

    logging.info("Starting Gemini API call with retries...")
    
    try:
        # Call Gemini with retry logic
        raw_text = call_gemini_with_retry(model, prompt)
        
        # Store the markdown output directly
        state["final_output_detailed"] = raw_text
        
        # Extract the summary section for the summary output
        try:
            summary_section = raw_text.split("# Summary")[-1].strip()
            state["final_output_summary"] = summary_section
        except Exception as e:
            state["final_output_summary"] = "Error extracting summary section"
        
        logging.info("Successfully generated analysis report")
            
    except Exception as e:
        error_msg = f"Unexpected error in execution: {str(e)}"
        logging.error(error_msg)
        state["final_output_detailed"] = error_msg
        state["final_output_summary"] = "Analysis failed due to unexpected error"

    return state

def build_single_call_execution_graph() -> StateGraph:
    """Builds the single-node graph that does everything in one shot."""
    builder = StateGraph(SingleExecutorState)
    builder.add_node("single_call_executor", single_call_executor)
    builder.add_edge(START, "single_call_executor")
    builder.add_edge("single_call_executor", END)
    return builder.compile()