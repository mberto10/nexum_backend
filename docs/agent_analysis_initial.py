import os
import google.generativeai as genai
from typing import TypedDict, Optional, List, Dict, Any
from langgraph.graph.state import StateGraph, START, END
from langgraph.graph.state import GraphRecursionError
from langchain_core.runnables import RunnableConfig
from langgraph.types import Command

# ----------------------------------------------------------------------------
# 1. State Definition
# ----------------------------------------------------------------------------

class AnalysisState(TypedDict):
    """
    Holds the entire state for the initial user input + planning module.
    """
    # Module 1: User Input
    user_query: str
    company_name: str

    # Module 2: Planning Output
    # We'll store the plan as a dictionary or list. If the plan is in raw JSON string,
    # we can store it as a string. For demonstration, let's store structured data.
    plan: Optional[Dict[str, Any]]

    # Additional placeholders for future expansions
    # E.g. with multi-step info gathering, partial results, etc.


# ----------------------------------------------------------------------------
# 2. Configure Gemini & Context Caching
# ----------------------------------------------------------------------------

# Example: Basic Gemini configuration + optional context caching demonstration.
# In real usage, you might store your API key in an environment variable or a vault.
API_KEY = os.environ.get("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

# For demonstration, we can create an in-memory context cache or a
# file-based approach. We'll keep it minimal here:
def create_context_cache():
    """
    Demonstrates uploading (or preparing) a file to cache.
    In real usage, you might gather user docs or large reference text to store.
    """
    # Placeholder: No actual doc uploading. If needed, do e.g.:
    # document = genai.upload_file("big_10K_file.pdf")
    # return genai.caching.CachedContent.create(...)
    return None

# We can attach the cache reference to a model if needed:
def get_planning_model():
    """
    Returns a generative model with optional context caching.
    """
    # Optionally create a cached content reference
    # cache = create_context_cache()
    # model = genai.GenerativeModel.from_cached_content(cache)
    # or a direct model approach:
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",  # or "gemini-1.5-pro-latest"
        generation_config=genai.types.GenerationConfig(
            temperature=0.2,
            max_output_tokens=1024,
        ),
    )
    return model


# ----------------------------------------------------------------------------
# 3. Planning Node
# ----------------------------------------------------------------------------

def planning_node(state: AnalysisState, config: RunnableConfig) -> AnalysisState:
    """
    Module 2 - Planning:
    1. Accept user_query & company_name from state
    2. Call Gemini to produce a JSON-based plan
    3. Parse & store it in `state["plan"]`
    """
    model = get_planning_model()
    user_query = state.get("user_query", "")
    company_name = state.get("company_name", "")
    if not user_query or not company_name:
        # Return minimal if missing
        state["plan"] = {"error": "No user query or company name provided."}
        return state

    # We request the model to produce structured plan:
    # Example prompt: We'll request a structured JSON output with
    # 1) Requirements
    # 2) ExecutionSteps
    # Real usage: refine prompt with instructions as needed.

    # Example schema in code, but you can pass it as an object if you prefer:
    plan_schema = {
        "type": "object",
        "properties": {
            "information_requirements": {
                "type": "array",
                "items": {"type": "object"}
            },
            "execution_steps": {
                "type": "array",
                "items": {"type": "object"}
            },
            "notes": {"type": "string"}
        },
        "required": ["information_requirements", "execution_steps"]
    }

    # Prompt asking for a JSON plan
    prompt = f"""
    You are an analysis planning agent.

    The user asks about: '{user_query}'
    The company name is: '{company_name}'

    Please produce a structured plan in JSON format with:
    - 'information_requirements': an array of objects that detail what data is needed,
      mark each requirement as 'factual' or 'broad'.
    - 'execution_steps': an ordered array of step objects describing how to collect the data
      (including any sub-graph usage or retrieval strategy).
    - 'notes': a short summary or disclaimers about the plan.

    Important: Return ONLY valid JSON.
    """

    # We leverage structured outputs in generation_config
    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(
            temperature=0.2,
            max_output_tokens=1200,
            response_mime_type="application/json",
            response_schema=plan_schema,
        ),
    )

    # Attempt to parse the text as JSON
    import json
    try:
        parsed_plan = json.loads(response.text.strip())
        state["plan"] = parsed_plan
    except json.JSONDecodeError:
        # Fallback if invalid JSON
        state["plan"] = {
            "error": "Invalid JSON returned.",
            "raw_response": response.text
        }
    return state


# ----------------------------------------------------------------------------
# 4. Graph Setup
# ----------------------------------------------------------------------------

def build_initial_planning_graph():
    """
    Builds a simple LangGraph workflow:
      START -> planning_node -> END
    """
    builder = StateGraph(AnalysisState)

    # Add nodes
    builder.add_node("planning_node", planning_node)

    # Edges
    builder.add_edge(START, "planning_node")
    builder.add_edge("planning_node", END)

    return builder.compile()


def run_planning_workflow(user_query: str, company_name: str) -> dict:
    """
    High-level function that sets up the graph state with user inputs,
    then runs the planning node.
    """
    graph = build_initial_planning_graph()
    initial_state: AnalysisState = {
        "user_query": user_query,
        "company_name": company_name,
        "plan": None
    }

    final_state = graph.invoke(initial_state)
    return final_state


# ----------------------------------------------------------------------------
# 5. Testing / Main
# ----------------------------------------------------------------------------

if __name__ == "__main__":
    # Example usage
    user_query = "Analyze the capital expenditure trends and revenue growth for last 3 years."
    company_name = "Microsoft"

    output_state = run_planning_workflow(user_query, company_name)
    print("===== Final Plan Output =====")
    print(output_state.get("plan", {}))