import os
from typing import Optional, Dict
from datetime import datetime
import re
from env_setup import load_import_variables

# Ensure required packages are installed
required_packages = {
    'python-dotenv': 'python-dotenv',
    'exa-py': 'exa-py',
    'llama-parse': 'llama-parse',
    'pinecone-client': 'pinecone-client'
}

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
    
    try:
        # Load all required environment variables
        env_vars = load_import_variables()
        
        # Generate namespace for this company
        namespace = generate_namespace(company_name)
        print(f"Using namespace: {namespace}")

        # Step 1: Search for 10-K
        print("\n=== STEP 1: Searching for 10-K ===")
        metadata = search_10k(company_name, env_vars["EXA_API_KEY"])
        if not metadata:
            print("Failed to find 10-K document. Pipeline stopped.")
            return False
        
        # Step 2: Download and Parse
        print("\n=== STEP 2: Downloading and Parsing PDF ===")
        pdf_path = download_sec_filing_pdf(metadata["document_url"], env_vars["SEC_API_KEY"])
        if not pdf_path:
            print("Failed to download PDF. Pipeline stopped.")
            return False
            
        markdown_path = parse_pdf_to_markdown(pdf_path, env_vars["LLAMA_CLOUD_API_KEY"])
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
            api_key=env_vars["PINECONE_API_KEY"],
            save_chunks=True,
            namespace=namespace
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