import os
from datetime import datetime
import logging
from typing import Dict, Optional

try:
    from exa_py import Exa
except ImportError:
    raise ImportError("Please install exa-py via: pip install exa-py")

def setup_logging():
    """Configure basic logging to console"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(message)s'
    )

def search_10k(company_name: str, exa_api_key: str) -> Optional[Dict[str, str]]:
    """
    Search for a company's most recent 10-K using Exa's search API.
    
    Args:
        company_name: Name of the company to search for
        exa_api_key: Exa API key for authentication
    
    Returns:
        Dictionary containing metadata about the found document:
            - company_name: Name of the company
            - fiscal_year: Fiscal year of the document
            - document_url: URL of the source document
            - document_type: Type of document (10-K)
        Returns None if no document is found or on error
    """
    try:
        # Initialize Exa client
        exa = Exa(api_key=exa_api_key)
        doc_type = "Form 10-K annual report"
        full_query = f"{company_name} {doc_type}"

        # Search for the document
        search_result = exa.search_and_contents(
            full_query,
            type="auto",
            num_results=1,
            text=False,  # We don't need the text content
            category="financial report",
            start_published_date="2023-11-30T23:00:01.000Z"  # Only recent documents
        )

        if not search_result or not search_result.results or len(search_result.results) == 0:
            logging.error(f"No 10-K found for {company_name}")
            return None

        doc = search_result.results[0]
        
        # Extract fiscal year from published date
        published_date_str = doc.published_date if doc.published_date else ""
        try:
            fiscal_year = published_date_str[:4]
            if not fiscal_year.isdigit():
                fiscal_year = "Unknown"
        except:
            fiscal_year = "Unknown"
            
        document_url = doc.url if doc.url else ""
        if not document_url:
            logging.error("No URL found in search result")
            return None

        # Construct metadata
        metadata = {
            "company_name": company_name,
            "fiscal_year": fiscal_year,
            "document_url": document_url,
            "document_type": "10-K"
        }

        # Log the search results
        logging.info("\n=== SEARCH RESULTS ===")
        for key, value in metadata.items():
            logging.info(f"{key}: {value}")
        logging.info("====================")

        return metadata

    except Exception as e:
        logging.error(f"Error during search: {str(e)}")
        return None

def main():
    """Test the search functionality with a sample company."""
    setup_logging()
    
    # Get company name from command line or prompt
    if len(sys.argv) > 1:
        company_name = sys.argv[1]
    else:
        company_name = input("Enter company name (e.g., NVIDIA, Apple, Microsoft): ").strip()

    if not company_name:
        print("Company name cannot be empty")
        return

    # Get API key from environment or prompt
    exa_api_key = os.getenv("EXA_API_KEY")
    if not exa_api_key:
        exa_api_key = input("Enter your Exa API key: ").strip()
        if not exa_api_key:
            print("No API key provided")
            return

    # Perform the search
    metadata = search_10k(company_name, exa_api_key)
    if not metadata:
        print("\nSearch failed. No document found.")

if __name__ == "__main__":
    import sys
    main() 