import os
import sys
import logging
from typing import List, Dict, Any, TypedDict, Optional
from datetime import datetime
from dotenv import load_dotenv

try:
    import google.generativeai as genai
except ImportError:
    raise ImportError("Please install google-generativeai via: pip install google-generativeai")

try:
    from pinecone import Pinecone
except ImportError:
    raise ImportError("Please install Pinecone via: pip install pinecone")

from langgraph.graph.state import StateGraph, START, END
from langchain_core.runnables import RunnableConfig

# Load environment variables from .env file
load_dotenv()

# Standard 10-K item headings and approximate info stored
TENK_ITEM_HEADINGS = {
    "Item 1. Business": "Description of business operations, main products and services, revenue streams, competitive landscape, market share, industry trends, key customers, suppliers, seasonality, government regulations, intellectual property, research and development, employees, geographic markets, corporate structure, subsidiaries, company history, business strategy, recent acquisitions or divestitures",
    "Item 1A. Risk Factors": "Details about major risks and uncertainties for the business, economic risks, market risks, operational risks, financial risks, regulatory risks, cybersecurity risks, environmental risks, competition risks, litigation risks, reputational risks, supply chain risks, technological risks, geopolitical risks, pandemic-related risks",
    "Item 1B. Unresolved Staff Comments": "Any unresolved comments or issues raised by the SEC staff on the company's previous filings",
    "Item 2. Properties": "Information about property, plants, and equipment, real estate holdings, leased properties, manufacturing facilities, distribution centers, office locations, land ownership, property values, capacity utilization",
    "Item 3. Legal Proceedings": "Any ongoing legal matters or litigation, pending lawsuits, regulatory proceedings, environmental litigation, patent disputes, class action suits, settlement agreements",
    "Item 4. Mine Safety Disclosures": "Mine safety information if applicable, violations, citations, legal actions related to mine safety",
    "Item 5. Market for Registrant's Common Equity": "Stock market details, holder information, dividends, stock price history, stock repurchase programs, equity compensation plans, securities authorized for issuance, performance graph comparing stock performance to market indices",
    "Item 6. None": "This item is currently reserved by the SEC for future use",
    "Item 7. Management's Discussion and Analysis of Financial Condition and Results of Operations": "Management analysis, business overview, future outlook, key performance indicators, liquidity and capital resources, results of operations, critical accounting estimates, off-balance sheet arrangements, contractual obligations, market risk disclosures, segment reporting, trends affecting the business",
    "Item 7A. Quantitative and Qualitative Disclosures About Market Risk": "Analysis of market risks, including interest rate risk, foreign currency risk, commodity price risk, equity price risk, credit risk, hedging activities",
    "Item 8. Financial Statements and Supplementary Data": "Audited financial statements, including Balance Sheet, Income Statement, Statement of Cash Flows, Statement of Stockholders' Equity, footnotes, accounting policies, segment information, quarterly financial data, five-year financial summary",
    "Item 9. Changes in and Disagreements with Accountants": "Accounting or auditing-related changes, disagreements with previous auditors, reasons for auditor change",
    "Item 9A. Controls and Procedures": "Internal control, disclosure control procedures, management's assessment of internal controls, attestation report of the registered public accounting firm",
    "Item 9B. Other Information": "Miscellaneous or additional info not otherwise captured, subsequent events, material information not reported on Form 8-K",
    "Item 9C. Disclosure Regarding Foreign Jurisdictions that Prevent Inspections": "Information about operating in jurisdictions that prevent PCAOB inspections",
    "Item 10. Directors, Executive Officers and Corporate Governance": "Details about executives, board of directors, governance policies, code of ethics, board committees, corporate governance guidelines, director independence, executive biographies",
    "Item 11. Executive Compensation": "Information on compensation of officers and directors, salary, bonuses, stock awards, option grants, pension plans, employment agreements, compensation discussion and analysis (CD&A)",
    "Item 12. Security Ownership of Certain Beneficial Owners": "Information on major shareholders, ownership structure, beneficial ownership table, equity compensation plan information",
    "Item 13. Certain Relationships and Related Transactions": "Details of related party transactions or conflicts of interest, transactions with management or major shareholders, policies for approval of related party transactions",
    "Item 14. Principal Accountant Fees and Services": "Accounting fees, services performed by principal accountant, audit fees, audit-related fees, tax fees, all other fees, pre-approval policies for auditor services",
    "Item 15. Exhibits, Financial Statement Schedules": "Exhibits, schedules attached to the 10-K, list of subsidiaries, list of guarantor subsidiaries, consent of independent registered public accounting firm, power of attorney, certifications required under Sarbanes-Oxley Act",
    "Item 16. Form 10-K Summary": "Optional summary of the report if provided, key highlights from each section"
}

# -----------------------------
# LOGGING SETUP
# -----------------------------
def setup_logging():
    """Configure logging to both file and console with timestamps."""
    if not os.path.exists('logs'):
        os.makedirs('logs')

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f'logs/search_query_{timestamp}.log'

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    logging.info(f"Query log file: {log_file}")

# -----------------------------
# STATE DEFINITION
# -----------------------------

class AgentState(TypedDict):
    user_query: str
    company_namespace: str              # Added company namespace
    relevant_item_headings: List[str]   
    available_subheadings: Dict[str, List[str]]
    search_configuration: Optional[Dict[str, Any]]
    pinecone_search_queries: List[str]
    matched_chunks: List[str]
    final_answer: Optional[str]

# -----------------------------
# NODE DEFINITIONS
# -----------------------------

def gemini_determine_headings(state: AgentState, config: RunnableConfig) -> AgentState:
    """
    Node #1: Use Gemini to interpret the user query and map it to one or more of the standard 10-K headings.
    """
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        logging.error("Missing GEMINI_API_KEY environment variable.")
        return state

    # Configure gemini
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Build a prompt that includes the standard headings and the user query
    headings_text = "\n".join([f"{k}: {v}" for k, v in TENK_ITEM_HEADINGS.items()])
    prompt = (
        "You are a helpful AI assistant. The user is asking about 10-K information. \n"
        "Below are the standard 10-K item headings and rough descriptions:\n"
        f"{headings_text}\n\n"
        "User query:\n"
        f"{state['user_query']}\n\n"
        "Instructions:\n"
        "1. Analyze the user query and identify the TOP 3 MOST RELEVANT item headings.\n"
        "2. Return ONLY a valid JSON object with exactly this structure:\n"
        "{\n"
        '    "relevant_headings": [\n'
        '        "Item X. Exact Heading Name",\n'
        '        "Item Y. Exact Heading Name",\n'
        '        "Item Z. Exact Heading Name"\n'
        "    ]\n"
        "}\n\n"
        "Requirements:\n"
        "- Include EXACTLY 3 headings\n"
        "- Each heading must be an EXACT MATCH from the list above\n"
        "- Return ONLY the JSON object, no other text\n"
        "- Ensure the JSON is properly formatted with double quotes"
    )

    try:
        response = model.generate_content(
            contents=prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.2,
                max_output_tokens=700
            )
        )
        
        # Parse the JSON response from the text
        import json
        try:
            response_text = response.text.strip()
            # If response is wrapped in ```json and ```, remove them
            if response_text.startswith('```json'):
                response_text = response_text[7:]
            if response_text.startswith('```'):
                response_text = response_text[3:]
            if response_text.endswith('```'):
                response_text = response_text[:-3]
            
            structured_response = json.loads(response_text.strip())
            relevant_headings = structured_response.get("relevant_headings", [])
            
            # Ensure headings are recognized
            recognized_headings = [
                h.strip() for h in relevant_headings 
                if h.strip() in TENK_ITEM_HEADINGS
            ][:3]  # Limit to 3 even if somehow more are returned

            logging.info(f"\nQUERY: {state['user_query']}")
            logging.info("\nRELEVANT ITEM HEADINGS:")
            for h in recognized_headings:
                logging.info(f"- {h}")
            
            state["relevant_item_headings"] = recognized_headings
            return state
            
        except json.JSONDecodeError as je:
            logging.error(f"Failed to parse JSON response: {je}")
            return state
            
    except Exception as e:
        logging.error(f"Error during heading determination: {e}")
        return state


def retrieve_metadata_with_zero_vector(state: AgentState, config: RunnableConfig) -> AgentState:
    """
    Node #2: Use a zero vector query to retrieve available subheadings for each relevant heading.
    """
    pinecone_api_key = os.getenv("PINECONE_API_KEY")
    if not pinecone_api_key:
        logging.error("Missing PINECONE_API_KEY environment variable.")
        return state

    pc = Pinecone(api_key=pinecone_api_key)
    index = pc.Index(host="https://financialdocs-ij61u7y.svc.aped-4627-b74a.pinecone.io")
    namespace = state["company_namespace"]

    # Create a zero vector with same dimensions as our embeddings (1024 for multilingual-e5-large)
    zero_vector = [0.0] * 1024
    available_subheadings = {}

    logging.info("\nSUBHEADINGS BY ITEM:")
    # Query once per relevant heading
    for heading in state["relevant_item_headings"]:
        try:
            metadata_filter = {
                "top_level_heading": heading
            }
            
            results = index.query(
                namespace=namespace,
                vector=zero_vector,
                top_k=100,
                include_values=False,
                include_metadata=True,
                filter=metadata_filter
            )
            
            logging.info(f"\n{heading}:")
            if not results or "matches" not in results:
                logging.info("└── No subheadings found")
                available_subheadings[heading] = []
                continue

            matches = results.get("matches", [])
            subheadings = set()
            for match in matches:
                meta = match.get("metadata", {})
                subheading = meta.get("subheading", "").strip()
                if subheading:
                    subheadings.add(subheading)
            
            available_subheadings[heading] = sorted(list(subheadings))
            
            if subheadings:
                for i, sh in enumerate(sorted(subheadings), 1):
                    prefix = "└──" if i == len(subheadings) else "├──"
                    logging.info(f"{prefix} {sh}")
            else:
                logging.info("└── No subheadings found")

        except Exception as e:
            logging.error(f"Error retrieving metadata for {heading}: {e}")
            available_subheadings[heading] = []
            continue

    state["available_subheadings"] = available_subheadings
    return state

def configure_search_with_gemini(state: AgentState, config: RunnableConfig) -> AgentState:
    """
    Node #3: Use Gemini to analyze the query and available metadata to configure the search.
    The search strategy combines:
    1. First two item headings without subheading filters (for broader context)
    2. Up to two very specific heading + subheading combinations (for targeted results)
    """
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        logging.error("Missing GEMINI_API_KEY environment variable.")
        return state

    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Get first two headings for broad context searches
    broad_headings = state["relevant_item_headings"][:2]
    
    # Build context about available metadata
    metadata_context = "Available headings and subheadings:\n"
    for heading, subheadings in state["available_subheadings"].items():
        metadata_context += f"\n{heading}:\n"
        for subheading in subheadings:
            metadata_context += f"  - {subheading}\n"

    prompt = (
        "You are a search configuration expert. Given a user query and available metadata fields, "
        "determine up to TWO very specific heading + subheading combinations that are most relevant.\n\n"
        f"User Query: {state['user_query']}\n\n"
        f"{metadata_context}\n"
        "Instructions:\n"
        "1. Analyze the query and available metadata.\n"
        "2. Identify up to TWO very specific heading + subheading combinations that are HIGHLY relevant.\n"
        "3. Return a JSON object with this structure:\n"
        "{\n"
        '    "specific_searches": [\n'
        "        {\n"
        '            "heading": "Item X...",\n'
        '            "subheading": "Exact Subheading Name"\n'
        "        },\n"
        "        ...\n"
        "    ]\n"
        "}\n\n"
        "IMPORTANT:\n"
        "- Return 0-2 specific searches (only if highly confident)\n"
        "- Each subheading must EXACTLY match one from the available ones\n"
        "- Only include combinations that are HIGHLY likely to contain relevant information\n"
        "- Quality over quantity - better to return fewer, more precise matches\n"
    )

    try:
        response = model.generate_content(
            contents=prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.2,
                max_output_tokens=1000
            )
        )
        
        # Parse the JSON response
        import json
        try:
            response_text = response.text.strip()
            if response_text.startswith('```json'):
                response_text = response_text[7:]
            if response_text.startswith('```'):
                response_text = response_text[3:]
            if response_text.endswith('```'):
                response_text = response_text[:-3]
            
            specific_searches = json.loads(response_text.strip())
            
            # Build final search configuration
            search_config = {"heading_configs": []}
            
            # Add broad context searches (first two headings without subheading filters)
            for heading in broad_headings:
                search_config["heading_configs"].append({
                    "heading": heading,
                    "use_subheading_filter": False
                })
            
            # Add specific searches with subheading filters
            for specific in specific_searches.get("specific_searches", []):
                heading = specific.get("heading")
                subheading = specific.get("subheading")
                
                # Validate the combination exists in our available metadata
                if (heading in state["available_subheadings"] and 
                    subheading in state["available_subheadings"][heading]):
                    search_config["heading_configs"].append({
                        "heading": heading,
                        "use_subheading_filter": True,
                        "relevant_subheadings": [subheading]
                    })
            
            logging.info("\nSEARCH CONFIGURATION:")
            # Log broad context searches
            logging.info("\nBroad context searches:")
            for config in search_config["heading_configs"][:2]:
                logging.info(f"- {config['heading']} (no subheading filter)")
            
            # Log specific searches
            specific_searches = search_config["heading_configs"][2:]
            if specific_searches:
                logging.info("\nSpecific searches:")
                for config in specific_searches:
                    if config.get("use_subheading_filter") and config.get("relevant_subheadings"):
                        logging.info(f"- {config['heading']}")
                        logging.info(f"  Subheading: {config['relevant_subheadings'][0]}")
            
            state["search_configuration"] = search_config
            return state
            
        except json.JSONDecodeError as je:
            logging.error("Failed to parse search configuration")
            state["search_configuration"] = {"heading_configs": [
                {"heading": h, "use_subheading_filter": False}
                for h in broad_headings
            ]}
            return state
            
    except Exception as e:
        logging.error("Error during search configuration")
        state["search_configuration"] = {"heading_configs": [
            {"heading": h, "use_subheading_filter": False}
            for h in broad_headings
        ]}
        return state

def pinecone_vector_search(state: AgentState, config: RunnableConfig) -> AgentState:
    """
    Node #4: Perform semantic search in Pinecone with metadata filtering based on LLM configuration.
    """
    pinecone_api_key = os.getenv("PINECONE_API_KEY")
    if not pinecone_api_key:
        logging.error("Missing PINECONE_API_KEY environment variable.")
        return state

    pc = Pinecone(api_key=pinecone_api_key)
    index = pc.Index(host="https://financialdocs-ij61u7y.svc.aped-4627-b74a.pinecone.io")
    namespace = state["company_namespace"]

    all_chunks = []
    user_query = state["user_query"]
    search_config = state.get("search_configuration", {"heading_configs": []})

    # Create one embedding for the user query
    try:
        query_embedding_list = pc.inference.embed(
            model="multilingual-e5-large",
            inputs=[user_query],
            parameters={"input_type": "query", "truncate": "END"}
        )
    except Exception as e:
        logging.error(f"Error embedding query {user_query}: {e}")
        return state

    if not query_embedding_list or not query_embedding_list.data:
        logging.warning(f"No query embedding returned from Pinecone inference for: {user_query}")
        return state

    query_vector = query_embedding_list[0].values
    logging.info(f"Embedding generated for query: {user_query[:80]}...")

    # Search based on configuration
    for heading_config in search_config.get("heading_configs", []):
        try:
            heading = heading_config.get("heading")
            use_subheading_filter = heading_config.get("use_subheading_filter", False)
            relevant_subheadings = heading_config.get("relevant_subheadings", [])

            # Build metadata filter
            metadata_filter = {
                "top_level_heading": heading
            }

            # Add subheading filter if configured
            if use_subheading_filter and relevant_subheadings:
                metadata_filter["subheading"] = {"$in": relevant_subheadings}
                logging.info(f"Searching {heading} with subheading filter: {relevant_subheadings}")
            else:
                logging.info(f"Searching {heading} without subheading filter")
            
            results = index.query(
                namespace=namespace,
                vector=query_vector,
                top_k=5,
                include_values=False,
                include_metadata=True,
                filter=metadata_filter
            )
            
            if not results or "matches" not in results:
                logging.warning(f"No results for heading: {heading}")
                continue

            matches = results["matches"] or []
            if matches:
                logging.info(f"Found {len(matches)} matches for {heading}")
            
            for match in matches:
                meta = match.get("metadata", {})
                chunk_info = {
                    "text": meta.get("chunk_text", ""),
                    "heading": meta.get("top_level_heading", ""),
                    "subheading": meta.get("subheading", ""),
                    "score": match.get("score", 0)
                }
                if chunk_info["text"]:
                    all_chunks.append(chunk_info)

        except Exception as e:
            logging.error(f"Error during Pinecone query for heading {heading}: {e}")
            continue

    # Remove all logging except final count
    logging.info(f"\nFound {len(all_chunks)} relevant chunks")
    state["matched_chunks"] = all_chunks
    return state


def interpret_results_with_gemini(state: AgentState, config: RunnableConfig) -> AgentState:
    """
    Node #4: Now that we have matched chunks, we call Gemini to generate a final answer.
    """
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        logging.error("Missing GEMINI_API_KEY environment variable.")
        return state

    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    query_text = state["user_query"]
    matched_chunks = state["matched_chunks"]
    context_text = ""
    for i, chunk in enumerate(matched_chunks, start=1):
        context_text += (
            f"\n[CHUNK {i}]:\n"
            f"Heading: {chunk['heading']}\n"
            f"Subheading: {chunk['subheading']}\n"
            f"Content: {chunk['text']}\n"
            f"Relevance Score: {chunk['score']:.2f}\n"
        )

    prompt = (
        "You are a professional financial analyst providing detailed analysis based on 10-K filings. "
        "For the given user query, I will provide relevant sections from the company's 10-K report. "
        "\nWhen answering:\n"
        "1. Structure your response in a professional, analytical tone.\n"
        "2. Focus on concrete facts, statistics, and specific details from the source material.\n"
        "3. For each piece of information, add a reference number in square brackets [1] within the text.\n"
        "4. Present your analysis in a clear, logical flow.\n"
        "5. After your main analysis, include a 'Sources:' section that lists all references.\n\n"
        "Format your response like this:\n\n"
        "ANALYSIS:\n"
        "[Main analysis text with [1], [2], etc. as references]\n\n"
        "SOURCES:\n"
        "[1] [heading], [subheading], [...relevant quote...] \n"
        "[2] [heading], [subheading], [...relevant quote...]\n"
        "...\n\n"
        "User Query: "
        f"{query_text}\n\n"
        f"Context:\n{context_text}\n\n"
        "Remember to maintain a professional tone and ensure every significant piece of information is properly referenced."
    )

    try:
        response = model.generate_content(
            contents=prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.2,
                max_output_tokens=1700
            )
        )
        final_text = response.text
        logging.info("\nFINAL ANSWER:")
        logging.info("=" * 80)
        logging.info(final_text)
        logging.info("=" * 80)
        state["final_answer"] = final_text
        return state
    except Exception as e:
        logging.error(f"Error generating final answer: {e}")
        state["final_answer"] = "I'm sorry, I encountered an error while generating the answer."
        return state

# -----------------------------
# GRAPH BUILDING
# -----------------------------
def build_retrieval_graph() -> StateGraph:
    """
    Build the LangGraph for multi-step retrieval.
    """
    builder = StateGraph(AgentState)

    # Add nodes
    builder.add_node("gemini_determine_headings", gemini_determine_headings)
    builder.add_node("retrieve_metadata_with_zero_vector", retrieve_metadata_with_zero_vector)
    builder.add_node("configure_search_with_gemini", configure_search_with_gemini)
    builder.add_node("pinecone_vector_search", pinecone_vector_search)
    builder.add_node("interpret_results_with_gemini", interpret_results_with_gemini)

    # Build edges using START and END constants
    builder.set_entry_point("gemini_determine_headings")
    builder.add_edge("gemini_determine_headings", "retrieve_metadata_with_zero_vector")
    builder.add_edge("retrieve_metadata_with_zero_vector", "configure_search_with_gemini")
    builder.add_edge("configure_search_with_gemini", "pinecone_vector_search")
    builder.add_edge("pinecone_vector_search", "interpret_results_with_gemini")
    builder.add_edge("interpret_results_with_gemini", END)

    return builder.compile()

# -----------------------------
# MAIN
# -----------------------------
def main():
    setup_logging()

    if len(sys.argv) < 3:
        logging.error("Usage: python agent_retrieval.py \"<company_name>\" \"<query_text>\"")
        return

    company_name = sys.argv[1].strip().lower()
    user_query = sys.argv[2].strip()

    # Generate clean namespace (lowercase alphanumeric only)
    import re
    namespace = re.sub(r'[^a-z0-9]', '', company_name)[:63]  # Max 63 chars for Pinecone

    # Setup initial state
    initial_state: AgentState = {
        "user_query": user_query,
        "company_namespace": namespace,
        "relevant_item_headings": [],
        "available_subheadings": [],
        "search_configuration": None,
        "pinecone_search_queries": [],
        "matched_chunks": [],
        "final_answer": None
    }

    # Build graph and run
    graph = build_retrieval_graph()
    final_state = graph.invoke(initial_state)

    # Get the final answer
    final_answer = final_state.get("final_answer", "No final answer.")
    
    # Print a separator for better readability
    print("\n" + "="*80 + "\n" + "FINAL RESULT:" + "\n" + "="*80)
    print(final_answer)
    
    # Log the result without printing it again
    logging.info("Final result generated successfully.")

if __name__ == '__main__':
    main()