import os
from datetime import datetime
import requests
from dotenv import load_dotenv
from llama_parse import LlamaParse

def download_sec_filing_pdf(url: str, sec_api_key: str) -> str:
    """Download a SEC filing as PDF using the SEC API."""
    
    # Construct the SEC API URL
    api_url = "https://api.sec-api.io/filing-reader"
    params = {
        "token": sec_api_key,
        "url": url
    }
    
    print(f"Downloading PDF from SEC API for URL: {url}")
    response = requests.get(api_url, params=params)
    
    if response.status_code != 200:
        raise Exception(f"Failed to download PDF: {response.status_code} - {response.text}")
    
    # Save the PDF
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = "sec_pdfs"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    company_name = url.split('/')[-1].split('-')[0].upper()
    pdf_path = os.path.join(output_dir, f"{company_name}_10k_{timestamp}.pdf")
    
    with open(pdf_path, "wb") as f:
        f.write(response.content)
    
    print(f"PDF saved to: {pdf_path}")
    return pdf_path

def parse_pdf_to_markdown(pdf_path: str, llama_api_key: str) -> str:
    """Parse PDF to markdown using LlamaParse."""
    
    print("\n--- Starting LlamaParse parsing ---")
    
    # Initialize parser with markdown-optimized configuration
    parser = LlamaParse(
        api_key=llama_api_key,
        result_type="markdown",  # Use markdown format
        verbose=True,
        language="en",
        fast_mode=False,  # Disable fast mode for better accuracy
        split_by_page=False,  # Don't split content by page
        num_workers=1,  # Sequential processing for reliability
        do_not_unroll_columns=False,  # Better for financial tables
        skip_diagonal_text=True,  # Skip diagonal text which might be artifacts
        parsing_instructions="""
        1. Preserve all headings and subheadings in markdown format
        2. Use # for top-level headings (e.g., PART I, ITEM 1)
        3. Use ## for second-level headings
        4. Use ### for third-level headings and below
        5. Maintain the original heading text and formatting
        6. Ensure all headings start on a new line
        7. Preserve table formatting in markdown
        """
    )
    
    try:
        # Parse the PDF file
        documents = parser.load_data(pdf_path)
        
        if not documents or len(documents) == 0:
            raise Exception("No parsed content returned from LlamaParse")
            
        # Combine all document parts if multiple were returned
        parsed_output = ""
        for doc in documents:
            doc_text = doc.text if hasattr(doc, 'text') else str(doc)
            parsed_output += doc_text + "\n\n"
            
        # Save the markdown output
        output_dir = "parsed_results"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        company_name = os.path.basename(pdf_path).split('_')[0]
        output_filename = os.path.join(output_dir, f"{company_name}_parsed_{timestamp}.md")
        
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(parsed_output)
            
        print(f"Parsed markdown saved to: {output_filename}")
        return output_filename
            
    except Exception as e:
        print(f"Error parsing with LlamaParse: {e}")
        return ""

def test_sec_download():
    """Test downloading a 10-K filing as PDF and parsing to markdown."""
    
    # Load environment variables
    load_dotenv()
    
    # Get API keys
    sec_api_key = os.getenv("SEC_API_KEY")
    llama_api_key = os.getenv("LLAMA_CLOUD_API_KEY")
    
    if not sec_api_key:
        raise ValueError("SEC_API_KEY not found in environment variables")
    if not llama_api_key:
        raise ValueError("LLAMA_CLOUD_API_KEY not found in environment variables")
    
    # Test URL - using Palantir's 10-K URL
    test_url = "https://www.sec.gov/Archives/edgar/data/1321655/000132165524000022/pltr-20231231.htm"
    
    try:
        # Step 1: Download the PDF
        pdf_path = download_sec_filing_pdf(test_url, sec_api_key)
        print(f"\nSuccessfully downloaded PDF to: {pdf_path}")
        
        # Step 2: Parse PDF to markdown
        markdown_path = parse_pdf_to_markdown(pdf_path, llama_api_key)
        if markdown_path:
            print(f"\nSuccessfully parsed PDF to markdown: {markdown_path}")
        else:
            print("\nFailed to parse PDF to markdown")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        if hasattr(e, 'response'):
            print(f"Response details: {e.response.text if hasattr(e.response, 'text') else 'No response text'}")

if __name__ == "__main__":
    test_sec_download() 