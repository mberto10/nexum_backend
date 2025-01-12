import os
from typing import Optional, Dict
from datetime import datetime
from dotenv import load_dotenv
import re

# Ensure required packages are installed
required_packages = {
    'python-dotenv': 'python-dotenv',
    'exa-py': 'exa-py',
    'llama-parse': 'llama-parse',
    'pinecone-client': 'pinecone-client'
}

def check_and_install_packages():
    import subprocess
    import sys
    
    for package, pip_name in required_packages.items():
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            print(f"Installing required package: {package}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])

# Install required packages
check_and_install_packages()

# Import our pipeline components
from import_0_search import search_10k, setup_logging
from import_1_parse import download_sec_filing_pdf, parse_pdf_to_markdown
from import_2_chunking import process_and_save_chunks
from import_3_indexing import embed_and_upsert

def generate_namespace(company_name: str) -> str:
    """
    Generate a clean namespace name from company name.
    Follows Pinecone's namespace naming conventions:
    - Lowercase alphanumeric characters and hyphens only
    - Must start with a letter
    - Maximum length of 63 characters
    """
    # Convert to lowercase and replace spaces/special chars with hyphens
    namespace = re.sub(r'[^a-zA-Z0-9-]', '-', company_name.lower())
    # Remove consecutive hyphens
    namespace = re.sub(r'-+', '-', namespace)
    # Remove leading/trailing hyphens
    namespace = namespace.strip('-')
    # Ensure it starts with a letter
    if not namespace[0].isalpha():
        namespace = 'company-' + namespace
    # Truncate to 63 characters if needed
    return namespace[:63]

def run_pipeline(company_name: str) -> bool:
    """
    Run the full document retrieval and processing pipeline:
    1. Search for company's 10-K using Exa
    2. Download PDF from SEC and parse to markdown
    3. Process markdown into chunks
    4. Embed and index chunks in Pinecone using company-specific namespace
    
    Args:
        company_name: Name of the company to process
    
    Returns:
        bool: True if pipeline completed successfully, False otherwise
    """
    # Setup logging
    setup_logging()
    print(f"\nStarting pipeline for company: {company_name}")
    
    # Load environment variables
    load_dotenv()
    
    # Get required API keys
    exa_api_key = os.getenv("EXA_API_KEY")
    sec_api_key = os.getenv("SEC_API_KEY")
    llama_api_key = os.getenv("LLAMA_CLOUD_API_KEY")
    pinecone_api_key = os.getenv("PINECONE_API_KEY")
    
    # Validate API keys
    missing_keys = []
    if not exa_api_key: missing_keys.append("EXA_API_KEY")
    if not sec_api_key: missing_keys.append("SEC_API_KEY")
    if not llama_api_key: missing_keys.append("LLAMA_CLOUD_API_KEY")
    if not pinecone_api_key: missing_keys.append("PINECONE_API_KEY")
    
    if missing_keys:
        print(f"Missing required API keys: {', '.join(missing_keys)}")
        print("Please add them to your .env file")
        return False
    
    # Generate namespace for this company
    namespace = generate_namespace(company_name)
    print(f"Using namespace: {namespace}")

    try:
        # Step 1: Search for 10-K
        print("\n=== STEP 1: Searching for 10-K ===")
        metadata = search_10k(company_name, exa_api_key)
        if not metadata:
            print("Failed to find 10-K document. Pipeline stopped.")
            return False
        
        # Step 2: Download and Parse
        print("\n=== STEP 2: Downloading and Parsing PDF ===")
        pdf_path = download_sec_filing_pdf(metadata["document_url"], sec_api_key)
        if not pdf_path:
            print("Failed to download PDF. Pipeline stopped.")
            return False
            
        markdown_path = parse_pdf_to_markdown(pdf_path, llama_api_key)
        if not markdown_path:
            print("Failed to parse PDF to markdown. Pipeline stopped.")
            return False
            
        # Step 3: Process into chunks
        print("\n=== STEP 3: Processing into chunks ===")
        with open(markdown_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
            
        # Generate output filename for chunks
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        chunks_file = f"chunking_results/{company_name}_chunks_{timestamp}.md"
        
        chunks = process_and_save_chunks(markdown_content, chunks_file)
        if not chunks:
            print("Failed to process chunks. Pipeline stopped.")
            return False
            
        print(f"Successfully processed {len(chunks)} chunks")
        
        # Step 4: Embed and Index
        print("\n=== STEP 4: Embedding and Indexing ===")
        embed_and_upsert(
            text_content=markdown_content,
            metadata=metadata,
            api_key=pinecone_api_key,
            save_chunks=True,
            namespace=namespace  # Add company-specific namespace
        )
        
        print("\n=== Pipeline completed successfully! ===")
        print(f"- PDF saved to: {pdf_path}")
        print(f"- Markdown saved to: {markdown_path}")
        print(f"- Chunks saved to: {chunks_file}")
        print(f"- Data indexed in Pinecone namespace: {namespace}")
        
        return True
        
    except Exception as e:
        print(f"\nError in pipeline: {str(e)}")
        return False

def main():
    """Run the pipeline with command line arguments or prompt."""
    import sys
    
    if len(sys.argv) > 1:
        company_name = sys.argv[1]
    else:
        company_name = input("Enter company name (e.g., NVIDIA, Apple, Microsoft): ").strip()
    
    if not company_name:
        print("Company name cannot be empty")
        return
        
    success = run_pipeline(company_name)
    if not success:
        print("\nPipeline failed. Check the error messages above.")
    
if __name__ == "__main__":
    main() 