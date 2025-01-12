import os
import json
import logging
from datetime import datetime
from typing import TypedDict, Optional, List, Dict, Any
import google.generativeai as genai
from pinecone import Pinecone

# Configure logging to write to both file and console
def setup_logging():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"logs/vectordb_analysis_{timestamp}.log"
    
    # Create a formatter that includes timestamp and level
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
    
    # Get the root logger and set its level
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    
    # Remove any existing handlers and add our new ones
    root_logger.handlers = []
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
    
    logging.info(f"Logging initialized. Log file: {log_filename}")

from langgraph.graph.state import StateGraph, START, END
from langchain_core.runnables import RunnableConfig
from langgraph.types import Send, Command

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

"""
This module sets up a graph that:
1) Takes a single 'raw_information_needs' string from the planning module,
   parses multiple info needs, then for each info need runs a pipeline of:
   - gemini_determine_headings
   - retrieve_metadata_with_zero_vector
   - configure_search_with_gemini
   - pinecone_vector_search
   (all in parallel for each info need)
2) Once all parallel tasks are done, interpret_results_with_gemini is invoked
   to produce final_interpretation, with one paragraph per info need.

"""

###############################################################################
# State Definitions
###############################################################################

class InfoNeedItem(TypedDict):
    info_need: str
    headings: List[str]
    metadata: Dict[str, Any]        # from zero-vector retrieval
    search_config: Dict[str, Any]   # from configure search
    search_results: List[Dict[str, Any]]  # from pinecone search

class AnalysisVectorDBState(TypedDict):
    """State definition for the vectordb retrieval sub-graph."""
    analysis_plan: Dict[str, Any]           # from orchestrator
    information_needs: List[Dict[str, str]] # from orchestrator
    company_namespace: str                  # from orchestrator
    
    # Internal state
    info_need_items: List[Dict[str, Any]]   # processed items with search results
    error_states: Dict[int, List[str]]      # track errors by item index
    retrieved_text: Dict[str, str]          # final output format
    search_logs: Dict[str, List[Dict[str, Any]]]  # detailed search process logs

###############################################################################
# Node 0: validate_credentials
###############################################################################
def validate_credentials(
    state: AnalysisVectorDBState,
    config: RunnableConfig
) -> Any:
    """
    Node #0: Validate all required API keys and credentials before starting the pipeline.
    """
    required_credentials = {
        "GEMINI_API_KEY": os.getenv("GEMINI_API_KEY"),
        "PINECONE_API_KEY": os.getenv("PINECONE_API_KEY")
    }
    
    missing_credentials = [
        key for key, value in required_credentials.items()
        if not value
    ]
    
    if missing_credentials:
        error_msg = f"Missing required credentials: {', '.join(missing_credentials)}"
        logging.error(error_msg)
        state["credentials_valid"] = False
        state["credentials_error"] = error_msg
        return Command(
            update={},
            goto=END
        )
    
    # Store validated credentials in state for reuse
    state["credentials_valid"] = True
    state["credentials"] = required_credentials
    
    # Preserve the company namespace in the state update
    return Command(
        update={
            "credentials_valid": True,
            "credentials": required_credentials,
            "company_namespace": state.get("company_namespace")
        },
        goto="parse_information_needs"
    )

###############################################################################
# Node 1: parse_information_needs
###############################################################################
def parse_information_needs(
    state: AnalysisVectorDBState,
    config: RunnableConfig
) -> Any:
    """
    Splits the information needs into individual items for processing.
    Then populates state['info_need_items'] = [ {info_need: <need>} ... ]
    """
    logging.info("Parsing information needs from analysis plan.")
    
    info_need_items = []
    for i, need in enumerate(state["information_needs"]):
        # Initialize each item with empty collections
        info_need_items.append({
            "info_need": need["description"],
            "headings": [],
            "metadata": {},
            "search_config": {"heading_configs": []},
            "search_results": []
        })
        # Initialize tracking for this item
        state["parallel_status"][i] = "pending"
        state["error_states"][i] = []

    state["info_need_items"] = info_need_items
    state["done_count"] = 0  # reset
    
    n_items = len(info_need_items)
    logging.info(f"Found {n_items} information needs to process:")
    for i, item in enumerate(info_need_items):
        logging.info(f"\n{i+1}. {item['info_need'][:100]}...")

    if n_items == 0:
        # If none, we can jump directly to structure_and_save_results
        return Command(
            update={"info_need_items": []},
            goto="structure_and_save_results"
        )

    # Return command to continue to next node
    return Command(
        update={
            "info_need_items": info_need_items,
            "company_namespace": state.get("company_namespace")  # Preserve namespace
        },
        goto="gemini_determine_headings"
    )

###############################################################################
# Node 2: gemini_determine_headings
###############################################################################
def gemini_determine_headings(
    state: AnalysisVectorDBState,
    config: RunnableConfig
) -> Any:
    """
    Node #2: Use Gemini to interpret each info need and map it to relevant 10-K headings.
    We'll store them in info_need_items[item_index]["headings"].
    """
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        logging.error("Missing GEMINI_API_KEY environment variable.")
        # Mark all as failed and continue
        for i in range(len(state["info_need_items"])):
            state["error_states"][i].append("Missing GEMINI_API_KEY")
        return Command(
            update={},
            goto="retrieve_metadata_with_zero_vector"
        )

    # Configure gemini
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Process each info need
    for item_index, item in enumerate(state["info_need_items"]):
        info_need = item["info_need"]
        logging.info(f"\nProcessing info need {item_index + 1}: {info_need[:100]}...")

        # Build a prompt that includes the standard headings and the info need
        headings_text = "\n".join([f"{k}: {v}" for k, v in TENK_ITEM_HEADINGS.items()])
        prompt = (
            "You are a helpful AI assistant. The user is asking about 10-K information. \n"
            "Below are the standard 10-K item headings and rough descriptions:\n"
            f"{headings_text}\n\n"
            "User query:\n"
            f"{info_need}\n\n"
            "Instructions:\n"
            "1. Analyze the query and identify the TOP 3 MOST RELEVANT item headings.\n"
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

                logging.info("\nRELEVANT ITEM HEADINGS:")
                for h in recognized_headings:
                    logging.info(f"- {h}")
                
                state["info_need_items"][item_index]["headings"] = recognized_headings
                
            except json.JSONDecodeError as je:
                logging.error(f"Failed to parse JSON response for item {item_index}: {je}")
                state["error_states"][item_index].append(f"JSON parse error: {je}")
                state["info_need_items"][item_index]["headings"] = []
                
        except Exception as e:
            logging.error(f"Error during heading determination for item {item_index}: {e}")
            state["error_states"][item_index].append(f"Gemini error: {e}")
            state["info_need_items"][item_index]["headings"] = []

    return Command(
        update={
            "info_need_items": state["info_need_items"],
            "company_namespace": state.get("company_namespace")  # Preserve namespace
        },
        goto="retrieve_metadata_with_zero_vector"
    )

###############################################################################
# Node 3: retrieve_metadata_with_zero_vector
###############################################################################
def retrieve_metadata_with_zero_vector(
    state: AnalysisVectorDBState,
    config: RunnableConfig
) -> Any:
    """
    Node #3: Use a zero vector query to retrieve available subheadings for each relevant heading.
    We'll store the result in info_need_items[item_index]["metadata"].
    """
    pinecone_api_key = os.getenv("PINECONE_API_KEY")
    if not pinecone_api_key:
        logging.error("Missing PINECONE_API_KEY environment variable.")
        # Mark all as failed and continue
        for i in range(len(state["info_need_items"])):
            state["error_states"][i].append("Missing PINECONE_API_KEY")
            state["info_need_items"][i]["metadata"] = {}
        return Command(
            update={},
            goto="configure_search_with_gemini"
        )

    pc = Pinecone(api_key=pinecone_api_key)
    index = pc.Index(host="https://financialdocs-ij61u7y.svc.aped-4627-b74a.pinecone.io")
    
    # Debug logging for state inspection
    logging.info("\nState contents:")
    for key, value in state.items():
        if key != "info_need_items":  # Skip long arrays
            logging.info(f"- {key}: {value}")
    
    # Get the namespace from the state - it should be set in the test case
    namespace = state.get("company_namespace")
    if not namespace:
        logging.error("No company namespace found in state")
        logging.error(f"Available state keys: {list(state.keys())}")
        # Mark all as failed and continue
        for i in range(len(state["info_need_items"])):
            state["error_states"][i].append("Missing company namespace")
            state["info_need_items"][i]["metadata"] = {}
        return Command(
            update={},
            goto="configure_search_with_gemini"
        )

    # Create a zero vector with same dimensions as our embeddings (1024 for multilingual-e5-large)
    zero_vector = [0.0] * 1024

    # Process each info need
    for item_index, item in enumerate(state["info_need_items"]):
        logging.info(f"\nRetrieving metadata for info need {item_index + 1}")
        available_subheadings = {}
        headings = item["headings"]

        logging.info("\nSUBHEADINGS BY ITEM:")
        for heading in headings:
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
                state["error_states"][item_index].append(f"Metadata error for {heading}: {e}")
                available_subheadings[heading] = []
                continue

        # Store the metadata in the state
        state["info_need_items"][item_index]["metadata"] = {
            "available_subheadings": available_subheadings,
            "retrieved_for_headings": headings
        }

    return Command(
        update={},
        goto="configure_search_with_gemini"
    )

###############################################################################
# Node 4: configure_search_with_gemini
###############################################################################
def configure_search_with_gemini(
    state: AnalysisVectorDBState,
    config: RunnableConfig
) -> Any:
    """
    Node #4: Use Gemini to analyze each query and available metadata to configure the search.
    The search strategy combines:
    1. First two item headings without subheading filters (for broader context)
    2. Up to two very specific heading + subheading combinations (for targeted results)
    """
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        logging.error("Missing GEMINI_API_KEY environment variable.")
        # Mark all as failed and continue with basic config
        for i, item in enumerate(state["info_need_items"]):
            state["error_states"][i].append("Missing GEMINI_API_KEY")
            state["info_need_items"][i]["search_config"] = {
                "heading_configs": [
                    {"heading": h, "use_subheading_filter": False}
                    for h in item["headings"][:2]
                ]
            }
        return Command(
            update={},
            goto="pinecone_vector_search"
        )

    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Process each info need
    for item_index, item in enumerate(state["info_need_items"]):
        logging.info(f"\nConfiguring search for info need {item_index + 1}")
        
        # Get first two headings for broad context searches
        broad_headings = item["headings"][:2]
        
        # Build context about available metadata
        metadata = item["metadata"]
        available_subheadings = metadata.get("available_subheadings", {})
        
        metadata_context = "Available headings and subheadings:\n"
        for heading, subheadings in available_subheadings.items():
            metadata_context += f"\n{heading}:\n"
            for subheading in subheadings:
                metadata_context += f"  - {subheading}\n"

        info_need = item["info_need"]
        prompt = (
            "You are a search configuration expert. Given a user query and available metadata fields, "
            "determine up to TWO very specific heading + subheading combinations that are most relevant.\n\n"
            f"User Query: {info_need}\n\n"
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
                    if (heading in available_subheadings and 
                        subheading in available_subheadings[heading]):
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
                
                state["info_need_items"][item_index]["search_config"] = search_config
                
            except json.JSONDecodeError as je:
                logging.error(f"Failed to parse search configuration for item {item_index}")
                state["error_states"][item_index].append(f"JSON parse error: {je}")
                state["info_need_items"][item_index]["search_config"] = {
                    "heading_configs": [
                        {"heading": h, "use_subheading_filter": False}
                        for h in broad_headings
                    ]
                }
                
        except Exception as e:
            logging.error(f"Error during search configuration for item {item_index}")
            state["error_states"][item_index].append(f"Gemini error: {e}")
            state["info_need_items"][item_index]["search_config"] = {
                "heading_configs": [
                    {"heading": h, "use_subheading_filter": False}
                    for h in broad_headings
                ]
            }

    return Command(
        update={
            "info_need_items": state["info_need_items"],
            "company_namespace": state.get("company_namespace")  # Preserve namespace
        },
        goto="pinecone_vector_search"
    )

###############################################################################
# Node 5: pinecone_vector_search
###############################################################################
def pinecone_vector_search(
    state: AnalysisVectorDBState,
    config: RunnableConfig
) -> Any:
    """
    Node #5: Perform semantic search in Pinecone with metadata filtering based on LLM configuration.
    We'll store the results in info_need_items[item_index]["search_results"].
    """
    pinecone_api_key = os.getenv("PINECONE_API_KEY")
    if not pinecone_api_key:
        logging.error("Missing PINECONE_API_KEY environment variable.")
        # Mark all as failed and continue
        for i in range(len(state["info_need_items"])):
            state["error_states"][i].append("Missing PINECONE_API_KEY")
            state["info_need_items"][i]["search_results"] = []
        return Command(
            update={},
            goto="subgraph_item_done"
        )

    pc = Pinecone(api_key=pinecone_api_key)
    index = pc.Index(host="https://financialdocs-ij61u7y.svc.aped-4627-b74a.pinecone.io")
    
    # Get the namespace from the state - it should be set in the test case
    namespace = state.get("company_namespace")
    if not namespace:
        logging.error("No company namespace found in state")
        # Mark all as failed and continue
        for i in range(len(state["info_need_items"])):
            state["error_states"][i].append("Missing company namespace")
            state["info_need_items"][i]["search_results"] = []
        return Command(
            update={},
            goto="subgraph_item_done"
        )

    # Process each info need
    for item_index, item in enumerate(state["info_need_items"]):
        logging.info(f"\nPerforming vector search for info need {item_index + 1}")
        all_chunks = []
        info_need = item["info_need"]
        search_config = item.get("search_config", {"heading_configs": []})

        # Create one embedding for the user query
        try:
            query_embedding_list = pc.inference.embed(
                model="multilingual-e5-large",
                inputs=[info_need],
                parameters={"input_type": "query", "truncate": "END"}
            )
        except Exception as e:
            logging.error(f"Error embedding query for item {item_index}: {e}")
            state["error_states"][item_index].append(f"Embedding error: {e}")
            state["info_need_items"][item_index]["search_results"] = []
            continue

        if not query_embedding_list or not query_embedding_list.data:
            logging.warning(f"No query embedding returned for item {item_index}")
            state["error_states"][item_index].append("No embedding returned")
            state["info_need_items"][item_index]["search_results"] = []
            continue

        query_vector = query_embedding_list[0].values
        logging.info(f"Embedding generated for query: {info_need[:80]}...")

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
                logging.error(f"Error during Pinecone query for heading {heading} in item {item_index}: {e}")
                state["error_states"][item_index].append(f"Search error for {heading}: {e}")
                continue

        # Store results for this item
        logging.info(f"\nFound {len(all_chunks)} relevant chunks for item {item_index}")
        state["info_need_items"][item_index]["search_results"] = all_chunks

    # Update completion status
    state["done_count"] = len(state["info_need_items"])
    for i in range(len(state["info_need_items"])):
        state["parallel_status"][i] = "completed"

    return Command(
        update={
            "info_need_items": state["info_need_items"],
            "done_count": len(state["info_need_items"]),
            "parallel_status": state["parallel_status"],
            "company_namespace": state.get("company_namespace")  # Preserve namespace
        },
        goto="subgraph_item_done"
    )

###############################################################################
# Node 6: subgraph_item_done
###############################################################################
def subgraph_item_done(
    state: AnalysisVectorDBState,
    config: RunnableConfig
) -> Any:
    """
    Called after processing all items. We check if there were any errors
    and proceed to interpret_results_with_gemini.
    """
    # Log completion status
    logging.info("\nProcessing complete:")
    logging.info(f"Total items processed: {len(state['info_need_items'])}")
    
    # Check for errors
    items_with_errors = [
        i for i, errors in state["error_states"].items()
        if errors
    ]
    if items_with_errors:
        logging.warning(f"\nItems with errors: {len(items_with_errors)}")
        for item_index in items_with_errors:
            logging.warning(f"\nItem {item_index + 1} errors:")
            for error in state["error_states"][item_index]:
                logging.warning(f"- {error}")
    
    # Always proceed to interpretation
    return Command(
        update={
            "info_need_items": state["info_need_items"],
            "done_count": state["done_count"],
            "parallel_status": state["parallel_status"],
            "error_states": state["error_states"],
            "company_namespace": state.get("company_namespace")  # Preserve namespace
        },
        goto="interpret_results_with_gemini"
    )

###############################################################################
# Node 7: interpret_results_with_gemini
###############################################################################
def interpret_results_with_gemini(
    state: AnalysisVectorDBState,
    config: RunnableConfig
) -> AnalysisVectorDBState:
    """
    Once all items are done, we produce final_interpretation with one paragraph per info need
    referencing the search results, headings, etc.
    """
    logging.info("interpret_results_with_gemini: combining results into final text.")

    paragraphs = []
    for i, item in enumerate(state["info_need_items"]):
        info_need = item["info_need"]
        results = item["search_results"]
        headings = item["headings"]
        metadata = item["metadata"]
        search_config = item["search_config"]
        errors = state["error_states"].get(i, [])

        # Build a comprehensive summary
        summary_lines = [
            f"Information Need {i+1}: {info_need}",
            f"\nStatus:",
            f"- Relevant headings identified: {len(headings)}",
            f"- Search configurations created: {len(search_config.get('heading_configs', []))}",
            f"- Results found: {len(results)}",
        ]

        if errors:
            summary_lines.append("\nErrors encountered:")
            for error in errors:
                summary_lines.append(f"- {error}")

        if headings:
            summary_lines.append("\nRelevant headings:")
            for h in headings:
                summary_lines.append(f"- {h}")

        if results:
            summary_lines.append("\nTop search results:")
            for j, result in enumerate(results[:3], 1):  # Show top 3 results
                summary_lines.extend([
                    f"\nResult {j}:",
                    f"Heading: {result['heading']}",
                    f"Subheading: {result['subheading']}",
                    f"Score: {result['score']:.3f}",
                    f"Text: {result['text'][:200]}..."  # Show first 200 chars
                ])
        else:
            summary_lines.append("\nNo search results found.")

        paragraphs.append("\n".join(summary_lines))

    final_text = "\n\n" + "="*80 + "\n\n".join(paragraphs)
    state["final_interpretation"] = final_text
    return state

def structure_and_save_results(
    state: AnalysisVectorDBState,
    config: RunnableConfig
) -> AnalysisVectorDBState:
    """
    Final node that structures the results for each information need and saves them
    for potential use in other sub-graphs.
    """
    logging.info("Structuring and saving search results.")
    
    # Convert structured results into a format similar to web module's retrieved_text
    retrieved_text = {}
    
    # Save detailed search process information
    search_details = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "company_namespace": state.get("company_namespace"),
        "search_logs": state["search_logs"],  # Include all search logs
        "information_needs": []
    }
    
    for i, item in enumerate(state["info_need_items"]):
        info_need = item["info_need"]
        results = item["search_results"]
        headings = item["headings"]
        errors = state["error_states"].get(i, [])
        
        # Find the matching information need to get the stored key
        matching_need = next(
            (need for need in state["information_needs"] if need["description"] == info_need),
            None
        )
        
        # Record search details for this need
        need_details = {
            "info_need": info_need,
            "relevant_headings": headings,
            "search_config": item.get("search_config", {}),
            "total_results": len(results),
            "errors": errors,
            "results_preview": []
        }
        
        if matching_need and results:
            stored_key = matching_need["stored"]
            # Format chunks into a single text
            chunks_text = []
            
            for chunk in results:
                formatted_chunk = f"""[{chunk['heading']} - {chunk['subheading']}]
Score: {chunk['score']:.3f}
{chunk['text']}
"""
                chunks_text.append(formatted_chunk)
                
                # Add to search details
                need_details["results_preview"].append({
                    "heading": chunk["heading"],
                    "subheading": chunk["subheading"],
                    "score": chunk["score"],
                    "text_preview": chunk["text"][:200] + "..."
                })
            
            # Join all chunks with separators
            retrieved_text[stored_key] = "\n\n---\n\n".join(chunks_text)
            
            # Log summary for this item
            logging.info(f"\nInformation Need {i+1}:")
            logging.info(f"Query: {info_need[:100]}...")
            logging.info(f"Total chunks found: {len(results)}")
        else:
            if matching_need:
                stored_key = matching_need["stored"]
                retrieved_text[stored_key] = "No relevant chunks found."
                need_details["results_preview"] = []
            
        if errors:
            logging.info("Errors encountered:")
            for error in errors:
                logging.info(f"- {error}")
        
        search_details["information_needs"].append(need_details)
    
    # Save results to state
    state["retrieved_text"] = retrieved_text
    state["search_details"] = search_details  # Store full details in state
    
    # Save detailed results to file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = "vectordb_results"
    os.makedirs(output_dir, exist_ok=True)
    
    # Save the search details
    details_file = os.path.join(output_dir, f"search_details_{timestamp}.json")
    with open(details_file, "w") as f:
        json.dump(search_details, f, indent=2)
    
    # Save the retrieved text
    results_file = os.path.join(output_dir, f"search_results_{timestamp}.json")
    with open(results_file, "w") as f:
        json.dump({
            "timestamp": timestamp,
            "company_namespace": state.get("company_namespace"),
            "results": retrieved_text
        }, f, indent=2)
    
    logging.info(f"\nStructured results saved to: {results_file}")
    logging.info(f"Search details saved to: {details_file}")
    
    return state

###############################################################################
# Graph Construction
###############################################################################
def build_vectordb_retrieval_graph() -> StateGraph:
    """
    Build the graph for vectordb-based retrieval:
    1. Parse info needs and get metadata
    2. Configure search for each need
    3. Execute vector search
    4. Structure and save results
    """
    builder = StateGraph(AnalysisVectorDBState)
    
    # Add nodes
    builder.add_node("parse_info_needs_and_get_metadata", parse_info_needs_and_get_metadata)
    builder.add_node("configure_search_for_info_needs", configure_search_for_info_needs)
    builder.add_node("execute_vector_search", execute_vector_search)
    builder.add_node("structure_and_save_results", structure_and_save_results)
    
    # Add edges
    builder.add_edge(START, "parse_info_needs_and_get_metadata")
    builder.add_edge("parse_info_needs_and_get_metadata", "configure_search_for_info_needs")
    builder.add_edge("configure_search_for_info_needs", "execute_vector_search")
    builder.add_edge("execute_vector_search", "structure_and_save_results")
    builder.add_edge("structure_and_save_results", END)
    
    return builder.compile()


###############################################################################
# Quick test
###############################################################################
if __name__ == "__main__":
    # Initialize logging with our custom setup
    setup_logging()
    
    logging.info("Starting VectorDB Analysis Test Run")
    logging.info("====================================")

    # Test case configuration
    company_name = "amazon"
    # Generate clean namespace (lowercase alphanumeric only)
    import re
    namespace = re.sub(r'[^a-z0-9]', '', company_name.lower())[:63]  # Max 63 chars for Pinecone

    logging.info(f"Company: {company_name}")
    logging.info(f"Namespace: {namespace}")
    logging.info("====================================")

    # Example plan matching orchestrator format
    test_plan = {
        "analysisType": "Financial Growth Analysis",
        "informationNeeds": [
            {
                "summary": "Amazon's Revenue Streams",
                "description": "Identify and quantify Amazon's main revenue streams (e.g., North America e-commerce, International e-commerce, AWS, etc.) from the 10-K. Include data for the last 3 years.",
                "tag": "factual",
                "dataSource": "10k",
                "stored": "revenueStreamsData"
            },
            {
                "summary": "Amazon's Growth Projections",
                "description": "Extract any statements or projections regarding future growth potential from the Management Discussion and Analysis (MD&A) section of the 10-K.",
                "tag": "broad",
                "dataSource": "10k",
                "stored": "growthProjections"
            }
        ]
    }

    # Build state matching orchestrator's format
    initial_state: AnalysisVectorDBState = {
        "analysis_plan": test_plan,
        "information_needs": test_plan["informationNeeds"],
        "info_need_items": [],
        "done_count": 0,
        "structured_results": [],
        "credentials_valid": False,
        "credentials_error": None,
        "credentials": {},
        "parallel_status": {},
        "error_states": {},
        "stream_events": [],
        "company_namespace": namespace
    }

    # Build and invoke graph
    logging.info("Building and invoking analysis graph...")
    graph = build_vectordb_retrieval_graph()
    
    try:
        final_state = graph.invoke(initial_state)
        logging.info("\nAnalysis completed successfully.")
    except Exception as e:
        logging.error(f"Analysis failed with error: {str(e)}", exc_info=True)
        raise

    logging.info("\n===== Structured Results =====\n")
    if final_state.get("structured_results"):
        print(json.dumps(final_state["structured_results"], indent=2))
    logging.info("\n====================================")
    logging.info("Test run completed.")

###############################################################################
# Utility Functions
###############################################################################
def parse_llm_json_response(response_text: str) -> dict:
    """
    Utility function to parse JSON from LLM responses, handling common formats
    like markdown code blocks.
    """
    text = response_text.strip()
    
    # Remove markdown code blocks if present
    if text.startswith('```json'):
        text = text[7:]
    elif text.startswith('```'):
        text = text[3:]
    if text.endswith('```'):
        text = text[:-3]
    
    # Parse and validate JSON
    try:
        return json.loads(text.strip())
    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse JSON response: {e}")
        logging.debug(f"Raw response text: {text}")
        raise

def parse_info_needs_and_get_metadata(
    state: AnalysisVectorDBState,
    config: RunnableConfig
) -> AnalysisVectorDBState:
    """Parse information needs and get metadata for each."""
    logging.info("Parsing information needs from analysis plan.")
    
    # Initialize tracking
    state["info_need_items"] = []
    state["error_states"] = {}
    state["search_logs"] = {
        "metadata_queries": [],
        "search_configurations": [],
        "vector_searches": [],
        "final_results": []
    }
    state["retrieved_text"] = {}  # Initialize retrieved_text
    
    # Process each information need
    for i, need in enumerate(state["information_needs"]):
        info_need = need["description"]
        logging.info(f"\nProcessing info need {i+1}: {info_need[:100]}...")
        
        try:
            # Initialize Pinecone
            pinecone_api_key = os.getenv("PINECONE_API_KEY")
            if not pinecone_api_key:
                raise ValueError("Missing PINECONE_API_KEY environment variable")
            
            pc = Pinecone(api_key=pinecone_api_key)
            index = pc.Index(host="https://financialdocs-ij61u7y.svc.aped-4627-b74a.pinecone.io")
            
            namespace = state.get("company_namespace", "")
            
            # Query with zero vector to get metadata
            zero_vector = [0.0] * 1024  # Dimension size for multilingual-e5-large
            results = index.query(
                vector=zero_vector,
                namespace=namespace,
                top_k=100,
                include_metadata=True
            )
            
            # Log metadata query
            state["search_logs"]["metadata_queries"].append({
                "info_need": info_need,
                "namespace": namespace,
                "query_type": "zero_vector",
                "top_k": 100,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            
            # Extract unique headings from top_level_heading field
            headings = sorted(list(set(
                match.metadata.get("top_level_heading", "")
                for match in results.matches
                if match.metadata.get("top_level_heading")
            )))
            
            logging.info("\nRELEVANT ITEM HEADINGS:")
            for heading in headings:
                logging.info(f"- {heading}")
            
            # Store processed item
            state["info_need_items"].append({
                "info_need": info_need,
                "headings": headings,
                "search_results": []
            })
            
        except Exception as e:
            error_msg = f"Error processing info need {i}: {str(e)}"
            logging.error(error_msg)
            state["error_states"][i] = [error_msg]
            state["info_need_items"].append({
                "info_need": info_need,
                "headings": [],
                "search_results": []
            })
    
    return state

def configure_search_for_info_needs(
    state: AnalysisVectorDBState,
    config: RunnableConfig
) -> AnalysisVectorDBState:
    """Configure search parameters for each information need."""
    for i, item in enumerate(state["info_need_items"]):
        info_need = item["info_need"]
        headings = item["headings"]
        
        logging.info(f"\nConfiguring search for info need {i+1}")
        logging.info("\nSEARCH CONFIGURATION:")
        
        # Define search configuration based on info need type
        if "revenue" in info_need.lower() or "financial" in info_need.lower():
            # For revenue/financial queries, focus on MD&A and Financial Statements
            relevant_items = [
                "Item 7. Management's Discussion and Analysis of Financial Condition and Results of Operations",
                "Item 8. Financial Statements and Supplementary Data"
            ]
            specific_subheadings = [
                "Consolidated Statements of Income",
                "Reportable segment operating income"
            ]
        elif "risk" in info_need.lower():
            # For risk queries, focus on Risk Factors and relevant MD&A sections
            relevant_items = [
                "Item 1A. Risk Factors",
                "Item 7. Management's Discussion and Analysis of Financial Condition and Results of Operations"
            ]
            specific_subheadings = [
                "Risks Related to Our Industry and Markets",
                "Demand and Supply, Product Transitions, and New Products and Business Models"
            ]
        else:
            # Default to broad search across all items
            relevant_items = headings
            specific_subheadings = []
        
        # Store search configuration
        search_config = {
            "broad_items": relevant_items,
            "specific_subheadings": specific_subheadings
        }
        item["search_config"] = search_config
        
        # Log configuration
        state["search_logs"]["search_configurations"].append({
            "info_need": info_need,
            "configuration": search_config,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        logging.info("\nBroad context searches:")
        for item in relevant_items:
            logging.info(f"- {item} (no subheading filter)")
        
        if specific_subheadings:
            logging.info("\nSpecific searches:")
            for item in relevant_items:
                for subheading in specific_subheadings:
                    logging.info(f"- {item}")
                    logging.info(f"  Subheading: {subheading}")
    
    return state

def execute_vector_search(
    state: AnalysisVectorDBState,
    config: RunnableConfig
) -> AnalysisVectorDBState:
    """Execute vector search for each information need."""
    for i, item in enumerate(state["info_need_items"]):
        info_need = item["info_need"]
        search_config = item.get("search_config", {})
        
        logging.info(f"\nPerforming vector search for info need {i+1}")
        
        search_log = {
            "info_need": info_need,
            "searches": [],
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        try:
            # Initialize Pinecone
            pinecone_api_key = os.getenv("PINECONE_API_KEY")
            if not pinecone_api_key:
                raise ValueError("Missing PINECONE_API_KEY environment variable")
            
            pc = Pinecone(api_key=pinecone_api_key)
            index = pc.Index(host="https://financialdocs-ij61u7y.svc.aped-4627-b74a.pinecone.io")
            
            # Generate embedding for the query
            query_embedding = pc.inference.embed(
                model="multilingual-e5-large",
                inputs=[info_need],
                parameters={"input_type": "query", "truncate": "END"}
            )[0].values
            
            logging.info(f"Embedding generated for query: {info_need[:100]}...")
            
            # Initialize results list
            all_results = []
            
            # Search across broad items
            for heading in search_config.get("broad_items", []):
                results = index.query(
                    vector=query_embedding,
                    namespace=state["company_namespace"],
                    top_k=5,
                    include_metadata=True,
                    filter={"top_level_heading": {"$eq": heading}}
                )
                
                # Log search
                search_log["searches"].append({
                    "type": "broad",
                    "heading": heading,
                    "filter": {"top_level_heading": {"$eq": heading}},
                    "results_found": len(results.matches)
                })
                
                logging.info(f"Found {len(results.matches)} matches for {heading}")
                for match in results.matches:
                    meta = match.metadata
                    chunk_info = {
                        "text": meta.get("chunk_text", ""),
                        "heading": meta.get("top_level_heading", ""),
                        "subheading": meta.get("subheading", ""),
                        "score": match.score
                    }
                    if chunk_info["text"]:
                        all_results.append(chunk_info)
            
            # Search with specific subheading filters
            for heading in search_config.get("broad_items", []):
                for subheading in search_config.get("specific_subheadings", []):
                    results = index.query(
                        vector=query_embedding,
                        namespace=state["company_namespace"],
                        top_k=5,
                        include_metadata=True,
                        filter={
                            "top_level_heading": {"$eq": heading},
                            "subheading": {"$eq": subheading}
                        }
                    )
                    
                    # Log search
                    search_log["searches"].append({
                        "type": "specific",
                        "heading": heading,
                        "subheading": subheading,
                        "filter": {
                            "top_level_heading": {"$eq": heading},
                            "subheading": {"$eq": subheading}
                        },
                        "results_found": len(results.matches)
                    })
                    
                    logging.info(f"Found {len(results.matches)} matches for {heading}")
                    for match in results.matches:
                        meta = match.metadata
                        chunk_info = {
                            "text": meta.get("chunk_text", ""),
                            "heading": meta.get("top_level_heading", ""),
                            "subheading": meta.get("subheading", ""),
                            "score": match.score
                        }
                        if chunk_info["text"]:
                            all_results.append(chunk_info)
            
            # Store results
            item["search_results"] = all_results
            logging.info(f"\nFound {len(all_results)} relevant chunks for item {i}")
            
            # Add to search logs
            state["search_logs"]["vector_searches"].append(search_log)
            
        except Exception as e:
            error_msg = f"Error executing search for info need {i}: {str(e)}"
            logging.error(error_msg)
            if i not in state["error_states"]:
                state["error_states"][i] = []
            state["error_states"][i].append(error_msg)
            
            # Log error in search logs
            search_log["error"] = error_msg
            state["search_logs"]["vector_searches"].append(search_log)
    
    return state