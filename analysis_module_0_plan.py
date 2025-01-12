import os
import google.generativeai as genai
from typing import TypedDict, Optional, List, Dict, Any
from langgraph.graph.state import StateGraph, START, END
from langchain_core.runnables import RunnableConfig
from langgraph.types import Command
import json
from datetime import datetime
from langsmith import traceable
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Verify environment variables are loaded
required_env_vars = [
    "GEMINI_API_KEY"
]

missing_vars = [var for var in required_env_vars if not os.getenv(var)]
if missing_vars:
    raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

# ----------------------------------------------------------------------------
# 1. State Definition
# ----------------------------------------------------------------------------

class AnalysisState(TypedDict):
    """
    Holds the entire state for the initial user input + planning module.
    """
    user_query: str
    company_name: str
    analysis_type: Optional[str]
    information_needs: Optional[List[Dict[str, str]]]
    execution_plan: Optional[List[Dict[str, Any]]]
    plan_raw: Optional[Dict[str, Any]]  # New field for tracking metrics
    metrics: Optional[Dict[str, Any]]

# ----------------------------------------------------------------------------
# 3. Context Cache (Workflow + Modules Overview)
# ----------------------------------------------------------------------------

CONTEXT_CACHE = """
## TASKCONTEXT
You are an expert financial analysis agent with deep expertise in finance, accounting, financial modeling, financial statements analysis and financial documentation and document structures.
You are a deliberate and comprehensive structured thinker and planner for comprehensive financial analysis.

## TASK
Your task is to plan a comprehensive analysis based on a user's query about a company's financial data and performance. 
You will create a structured plan that outlines the information gathering needs and subsequent analysis steps.
The plan must be thorough, logically sequenced, and follow all specified constraints.

## WORKFLOW CONTEXT
The analysis process is divided into distinct modules:
1. User Input Processing (Current)
2. Analysis Planning (Current - Your Focus)
3. Information Gathering (Separate Module)
4. Analysis Execution (Separate Module)

## BACKGROUND: DOCUMENT STR
The 10-K filing follows a standardized structure with specific items containing distinct types of information:

### Core Business Information
- **Item 1. Business**: Company operations, products/services, revenue streams, competitive landscape, market share, industry trends, key customers, suppliers, seasonality, regulations, IP, R&D, geographic markets, corporate structure
- **Item 1A. Risk Factors**: Major business risks including economic, market, operational, financial, regulatory, cybersecurity, environmental, competition, litigation risks
- **Item 1B. Unresolved Staff Comments**: SEC staff comments on previous filings

### Assets and Legal
- **Item 2. Properties**: Physical assets, facilities, real estate, manufacturing locations, distribution centers
- **Item 3. Legal Proceedings**: Ongoing litigation, regulatory proceedings, patent disputes, settlements
- **Item 4. Mine Safety Disclosures**: Mine safety information if applicable

### Financial Performance
- **Item 5. Market for Registrant's Common Equity**: Stock information, dividends, repurchase programs
- **Item 6. [Reserved]**: Currently reserved by SEC
- **Item 7. Management's Discussion and Analysis**: Business overview, performance indicators, liquidity, operations results, future outlook, trends
- **Item 7A. Market Risk Disclosures**: Analysis of market risks (interest rate, currency, commodity price risks)
- **Item 8. Financial Statements**: Complete audited financial statements, footnotes, accounting policies
- **Item 9. Changes in and Disagreements with Accountants**: Accounting changes and disputes
- **Item 9A. Controls and Procedures**: Internal control assessment
- **Item 9B. Other Information**: Additional material information
- **Item 9C. Foreign Jurisdictions Disclosure**: Information about operations in jurisdictions preventing PCAOB inspections

### Governance and Management
- **Item 10. Directors and Executive Officers**: Leadership details, governance policies
- **Item 11. Executive Compensation**: Detailed compensation information
- **Item 12. Security Ownership**: Major shareholders information
- **Item 13. Related Transactions**: Related party transactions
- **Item 14. Principal Accountant Fees**: Accounting services and fees
- **Item 15. Exhibits**: Additional documentation and certifications
- **Item 16. Form 10-K Summary**: Optional report summary

### Common Analysis Patterns

Here are some common analysis planning patterns that you can adapt to the specific user query for formulating your plan.

1. **Revenue Analysis Pattern**
   - **Core Information Needs**:
     - Historical revenue data by segment/product line
     - Revenue growth rates and trends
     - Geographic distribution of revenue
     - Revenue concentration (key customers/products)
   - **Supporting Information Needs**:
     - Market size and share data
     - Pricing strategies and changes
     - Seasonality patterns
     - Currency exposure impacts
   - **Analysis Components**:
     - Segment contribution analysis
     - Year-over-year growth decomposition
     - Revenue quality assessment
     - Forward-looking indicators

2. **Risk Assessment Pattern**
   - **Core Information Needs**:
     - Identified risk factors and their potential impact
     - Risk mitigation strategies
     - Historical risk events and outcomes
     - Industry-specific risk factors
   - **Supporting Information Needs**:
     - Control measures and their effectiveness
     - Insurance and hedging strategies
     - Regulatory compliance status
     - Pending litigation or disputes
   - **Analysis Components**:
     - Risk severity and likelihood matrix
     - Year-over-year risk evolution
     - Comparative industry risk assessment
     - Risk response effectiveness

3. **Growth Analysis Pattern**
   - **Core Information Needs**:
     - Strategic growth initiatives
     - Market expansion plans
     - R&D investments and pipeline
     - Capital allocation strategy
   - **Supporting Information Needs**:
     - Competitive landscape changes
     - Market penetration metrics
     - Historical execution success
     - Resource availability
   - **Analysis Components**:
     - Growth driver identification
     - Investment return analysis
     - Market opportunity sizing
     - Execution capability assessment

4. **Competitive Position Pattern**
   - **Core Information Needs**:
     - Market share data and trends
     - Competitive advantages
     - Product/service differentiation
     - Cost position and efficiency metrics
   - **Supporting Information Needs**:
     - Industry structure and dynamics
     - Technology and innovation position
     - Brand strength indicators
     - Customer relationship metrics
   - **Analysis Components**:
     - Competitive advantage sustainability
     - Market position trajectory
     - Capability gap analysis
     - Strategic response assessment

5. **Financial Health Pattern**
   - **Core Information Needs**:
     - Key financial metrics and ratios
     - Cash flow composition
     - Capital structure
     - Working capital efficiency
   - **Supporting Information Needs**:
     - Credit ratings and debt covenants
     - Off-balance sheet obligations
     - Liquidity sources
     - Asset quality indicators
   - **Analysis Components**:
     - Financial flexibility assessment
     - Stress test scenarios
     - Capital efficiency analysis
     - Sustainability of financial position

6. **Operational Efficiency Pattern**
   - **Core Information Needs**:
     - Operating margins and trends
     - Cost structure breakdown
     - Productivity metrics
     - Capacity utilization
   - **Supporting Information Needs**:
     - Supply chain performance
     - Quality metrics
     - Employee productivity
     - Asset performance data
   - **Analysis Components**:
     - Margin driver analysis
     - Operational bottleneck identification
     - Efficiency improvement potential
     - Cost optimization opportunities

### Key Information Interconnections
1. **Operational Performance Analysis**
   - Item 7 (MD&A) → Item 8 (Financial Statements)
   - Item 1 (Business Operations) → Item 2 (Operational Assets)
   - Item 1A (Risks) → Item 7 (Risk Mitigation Strategies)

2. **Strategic Analysis**
   - Item 1 (Strategy) → Item 7 (Implementation Progress)
   - Item 1A (Risks) → Item 9A (Control Measures)
   - Item 2 (Assets) → Item 8 (Asset Utilization)

3. **Financial Health Assessment**
   - Item 8 (Financials) → Item 7 (Management's Interpretation)
   - Item 7A (Risks) → Item 7 (Risk Management)
   - Item 1A (Risks) → Item 5 (Market Impact)

### Information Depth Guide
1. **Quantitative Data (High Precision)**
   - Item 8: Detailed financial statements, exact figures
   - Item 5: Specific share counts, prices, dividends
   - Item 11: Precise compensation figures

2. **Qualitative Analysis (Medium-High Detail)**
   - Item 7: Detailed management discussion, trends
   - Item 1: Comprehensive business description
   - Item 1A: Extensive risk descriptions

3. **Contextual Information (Medium Detail)**
   - Item 2: Asset descriptions and locations
   - Item 10: Management backgrounds
   - Item 13: Related party descriptions

4. **Supporting Information (Variable Detail)**
   - Item 9B: Supplementary information
   - Item 15: Referenced documents
   - Item 16: Optional summary

## DATA SOURCES
Primary Source: 10-K Financial Documents
- Stored in Pinecone vector database
- Documents are chunked with metadata tags
- Tags include: top-level item headings, subheadings
- Contains both numerical data and textual analysis

## PLANNING INSTRUCTIONS
Follow these steps to create a comprehensive analysis plan:

1. Query Analysis
   - Deeply understand the user's request
   - Identify key analysis components needed
   - Determine if request needs factual data, qualitative analysis, or both

2. Information Requirements
   - List all required data points and information
   - Distinguish between factual data and broad analysis needs
   - For each information need, specify the data source (10k or web)
   - Ensure data source selection matches the type of information needed

3. Analysis Structure
   - Break down analysis into concrete, actionable steps
   - Each step must be a specific calculation, analysis, or reasoning task
   - NO data consolidation or preparation steps - these are handled automatically
   - Steps should build upon each other logically
   - Examples of concrete steps:
     ✓ Calculate year-over-year growth rates
     ✓ Perform segment contribution analysis
     ✓ Analyze margin trends by business unit
     ✓ Compare profitability ratios to industry benchmarks
     ✓ Evaluate operational efficiency metrics
     ✗ NO "Consolidate data" or "Prepare information" steps
     ✗ NO "Gather" or "Collect" steps

4. Output Planning
   - Define specific metrics and insights to be presented
   - Specify any visualizations or comparisons needed
   - Plan clear and actionable conclusions

## JSON OUTPUT SCHEMA
{
  "analysisType": "string - Categorize the type of analysis (e.g., 'Revenue Analysis', 'Growth Assessment')",
  "informationNeeds": [
    {
      "summary": "Brief description of needed information",
      "description": "Detailed explanation of data format and context needed",
      "tag": "factual | broad",
      "dataSource": "10k | web",
      "stored": "unique_identifier_for_retrieval"
    }
  ],
  "executionPlan": [
    {
      "stepName": "Specific analysis or calculation name",
      "actions": [
        {
          "actionType": "FinancialCalculation | TextAnalysis | ComparisonAnalysis | ScenarioModeling | WebResearch | ResultFormatting",
          "task": "Concrete calculation or analysis instruction",
          "information": ["stored_identifiers_from_information_needs"]
        }
      ]
    }
  ]
}

## CONSTRAINTS
1. Return ONLY valid JSON - no additional text or markdown
2. Final step MUST be ResultFormatting type
3. Do not include data consolidation or preparation steps
4. Each step must be a concrete analysis, calculation, or reasoning task
5. Ensure all stored identifiers are unique
6. All steps must be logically connected

## QUALITY CHECKS
- Is each step a concrete analysis or calculation?
- Are there any data consolidation steps that need to be removed?
- Is the execution plan logically sequenced?
- Are dependencies between steps clear?
- Is the final output format well-defined?
- Have potential challenges been noted?
"""

# ----------------------------------------------------------------------------
# 4. Configure Gemini & (Optional) Context Caching
# ----------------------------------------------------------------------------

# Configure Gemini with API key from environment
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set")
genai.configure(api_key=gemini_api_key)

def get_planning_model():
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=genai.types.GenerationConfig(
            temperature=0.5,
            max_output_tokens=2500,
        )
    )

    # Define the response schema for structured output
    model.response_schema = {
        "type": "object",
        "properties": {
            "analysisType": {"type": "string"},
            "informationNeeds": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "summary": {"type": "string"},
                        "description": {"type": "string"},
                        "tag": {
                            "type": "string",
                            "enum": ["factual", "broad"]
                        },
                        "dataSource": {
                            "type": "string",
                            "enum": ["10k", "web"]
                        },
                        "stored": {"type": "string"}
                    },
                    "required": ["summary", "description", "tag", "dataSource", "stored"]
                }
            },
            "executionPlan": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "stepName": {"type": "string"},
                        "actions": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "actionType": {
                                        "type": "string",
                                        "enum": [
                                            "FinancialCalculation",
                                            "TextAnalysis",
                                            "ComparisonAnalysis",
                                            "ScenarioModeling",
                                            "WebResearch",
                                            "ResultFormatting"
                                        ]
                                    },
                                    "task": {"type": "string"},
                                    "information": {
                                        "type": "array",
                                        "items": {"type": "string"}
                                    }
                                },
                                "required": ["actionType", "task", "information"]
                            }
                        }
                    },
                    "required": ["stepName", "actions"]
                }
            }
        },
        "required": [
            "analysisType",
            "informationNeeds",
            "executionPlan"
        ]
    }
    
    return model

# ----------------------------------------------------------------------------
# 5. Planning Node
# ----------------------------------------------------------------------------

@traceable(name="planning_node", tags=["planning", "gemini"])
def planning_node(state: AnalysisState, config: RunnableConfig, use_context_cache: bool = True) -> AnalysisState:
    """
    Module 2 - Planning:
    1. Accept user_query & company_name from state
    2. Optionally provide the big context (CONTEXT_CACHE) to the LLM
    3. Call Gemini to produce a JSON-based plan
    4. Parse & store each portion into state
    """
    user_query = state.get("user_query", "")
    company_name = state.get("company_name", "")
    if not user_query or not company_name:
        state["plan_raw"] = {
            "error": "Missing user_query or company_name",
            "raw_response": None
        }
        return state

    # Initialize metrics tracking
    start_time = time.time()
    metrics = {
        "latency": 0,
        "token_usage": {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0
        },
        "cost": {
            "prompt_cost": 0,
            "completion_cost": 0,
            "total_cost": 0
        }
    }
    raw_text = ""

    # Build prompt
    context_part = CONTEXT_CACHE if use_context_cache else ""
    prompt = f"""
{context_part}

User's query: '{user_query}'
Company name: '{company_name}'

Return a JSON object following the schema provided. Do not include any markdown formatting or extra text.
"""

    try:
        model = get_planning_model()
        
        # Generate response with timing
        response = model.generate_content(
            prompt
        )
        
        raw_text = response.text.strip()
        
        # Remove any markdown formatting if present
        if raw_text.startswith("```"):
            raw_text = raw_text.split("```")[1]
            if raw_text.startswith("json"):
                raw_text = raw_text[4:]
        raw_text = raw_text.strip()
        
        # Parse JSON and update metrics
        parsed = json.loads(raw_text)
        
        # Track token usage and cost
        if hasattr(response, 'usage'):
            # Actual token usage from Gemini
            metrics["token_usage"] = {
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
                "total_tokens": response.usage.total_tokens
            }
            
            # Calculate costs based on model type (Gemini 1.5 Flash/Pro pricing)
            # For prompts <= 128K tokens:
            # Flash: $0.00001875/1K chars input, $0.000075/1K chars output
            # Pro: $0.0003125/1K chars input, $0.00125/1K chars output
            # Note: ~4 characters per token as per Google's documentation
            chars_per_token = 4
            if model.model_name == "gemini-1.5-flash":
                prompt_cost = (response.usage.prompt_tokens * chars_per_token * 0.00001875) / 1000
                completion_cost = (response.usage.completion_tokens * chars_per_token * 0.000075) / 1000
            else:  # gemini-1.5-pro
                prompt_cost = (response.usage.prompt_tokens * chars_per_token * 0.0003125) / 1000
                completion_cost = (response.usage.completion_tokens * chars_per_token * 0.00125) / 1000
            
            metrics["cost"] = {
                "prompt_cost": prompt_cost,
                "completion_cost": completion_cost,
                "total_cost": prompt_cost + completion_cost,
                "model": model.model_name
            }
        else:
            # Fallback to simple estimation if usage not available
            prompt_chars = len(prompt) * 4  # Approximate character count
            completion_chars = len(raw_text) * 4
            
            metrics["token_usage"] = {
                "prompt_tokens": prompt_chars // 4,
                "completion_tokens": completion_chars // 4,
                "total_tokens": (prompt_chars + completion_chars) // 4
            }
            
            # Estimate costs using Gemini 1.5 Pro pricing by default
            prompt_cost = (prompt_chars * 0.0003125) / 1000
            completion_cost = (completion_chars * 0.00125) / 1000
            
            metrics["cost"] = {
                "prompt_cost": prompt_cost,
                "completion_cost": completion_cost,
                "total_cost": prompt_cost + completion_cost,
                "model": "gemini-1.5-pro (estimated)"
            }
        
        # Add latency
        metrics["latency"] = time.time() - start_time
        
        # Store results in state
        state["plan_raw"] = parsed
        state["analysis_type"] = parsed.get("analysisType")
        state["information_needs"] = parsed.get("informationNeeds")
        state["execution_plan"] = parsed.get("executionPlan")
        state["metrics"] = metrics

    except Exception as e:
        error_info = {
            "error": f"Error processing response: {str(e)}",
            "raw_response": raw_text
        }
        state["plan_raw"] = error_info
        metrics["error"] = str(e)
        state["metrics"] = metrics

    return state

# ----------------------------------------------------------------------------
# 5. Graph Setup
# ----------------------------------------------------------------------------

def build_initial_planning_graph(use_context_cache: bool = True):
    """
    Builds a simple LangGraph workflow:
      START -> planning_node -> END
    """
    builder = StateGraph(AnalysisState)

    def planning_node_wrapper(state: AnalysisState, config: RunnableConfig) -> AnalysisState:
        return planning_node(state, config, use_context_cache=use_context_cache)

    builder.add_node("planning_node", planning_node_wrapper)

    builder.add_edge(START, "planning_node")
    builder.add_edge("planning_node", END)

    return builder.compile()

def run_planning_workflow(user_query: str, company_name: str, use_context_cache: bool = True) -> dict:
    """
    High-level function that sets up the graph state with user inputs,
    then runs the planning node.
    """
    graph = build_initial_planning_graph(use_context_cache=use_context_cache)
    initial_state: AnalysisState = {
        "user_query": user_query,
        "company_name": company_name,
        "analysis_type": None,
        "information_needs": None,
        "execution_plan": None,
        "plan_raw": None,
        "metrics": None
    }
    final_state = graph.invoke(initial_state)
    return final_state

def save_plan_as_markdown(state: AnalysisState, output_file: str = None) -> str:
    """
    Save the analysis plan as a well-formatted markdown file.
    Returns the path to the saved file.
    """
    # Create output directory if it doesn't exist
    output_dir = "analysis_plans"
    os.makedirs(output_dir, exist_ok=True)

    # Generate default output name if none provided
    if not output_file:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        company_name = state.get("company_name", "unknown").replace(" ", "_")
        output_file = os.path.join(output_dir, f"analysis_plan_{company_name}_{timestamp}.md")

    # Format the content
    content = []
    content.append(f"# Analysis Plan for {state['company_name']}\n")
    content.append(f"## Query\n{state['user_query']}\n")
    
    if state.get("analysis_type"):
        content.append(f"## Analysis Type\n{state['analysis_type']}\n")
    
    if state.get("information_needs"):
        content.append("## Information Needs\n")
        for i, need in enumerate(state["information_needs"], 1):
            content.append(f"### {i}. {need['summary']}")
            content.append(f"- **Description**: {need['description']}")
            content.append(f"- **Type**: {need['tag']}")
            content.append(f"- **Data Source**: {need['dataSource']}")
            content.append(f"- **Storage ID**: `{need['stored']}`\n")
    
    if state.get("execution_plan"):
        content.append("## Execution Plan\n")
        for i, step in enumerate(state["execution_plan"], 1):
            content.append(f"### Step {i}: {step['stepName']}")
            for j, action in enumerate(step["actions"], 1):
                content.append(f"#### Action {j}")
                content.append(f"- **Type**: {action['actionType']}")
                content.append(f"- **Task**: {action['task']}")
                if action.get("information"):
                    content.append("- **Required Information**:")
                    for info in action["information"]:
                        content.append(f"  - `{info}`")
                content.append("")

    # Write to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(content))

    return output_file

# ----------------------------------------------------------------------------
# 6. Testing / Main
# ----------------------------------------------------------------------------

if __name__ == "__main__":
    test_query = "Analyze NVIDIA's equity and debt financing activities."
    test_company = "NVIDIA"
    result = run_planning_workflow(test_query, test_company, use_context_cache=True)
    print("\n===== Analysis Planning Output =====")
    print(f"\nQuery: {test_query}")
    print(f"Company: {test_company}\n")
    
    # Save as markdown
    output_file = save_plan_as_markdown(result)
    print(f"\nAnalysis plan saved to: {output_file}")
    
    # Also print JSON for debugging
    plan = result.get("plan_raw", {})
    formatted_json = json.dumps(plan, indent=2)
    print("\nRaw JSON output:")
    print(formatted_json)