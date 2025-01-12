import os
import sys
from typing import List, Dict, Any
from datetime import datetime
from import_2_chunking import process_and_save_chunks

try:
    from pinecone import Pinecone
except ImportError:
    raise ImportError("Please install Pinecone via: pip install pinecone")

def embed_and_upsert(
    text_content: str,
    metadata: Dict[str, str],
    api_key: str,
    save_chunks: bool = True,
    namespace: str = ""
) -> bool:
    """
    Embed chunks of text and upsert them to Pinecone.
    
    Args:
        text_content: The text content to process and embed
        metadata: Document metadata to include with each chunk
        api_key: Pinecone API key
        save_chunks: Whether to save chunks to a file
        namespace: Pinecone namespace to use (company-specific)
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        from pinecone import Pinecone
    except ImportError:
        print("Please install pinecone-client: pip install pinecone-client")
        return False

    # Initialize Pinecone
    pc = Pinecone(api_key=api_key)
    
    # Get the index name from environment variables
    index_name = os.getenv("PINECONE_INDEX_NAME", "financialdocs")
    
    # Get the index
    index = pc.Index(index_name)
    
    # Process text into chunks
    chunks = process_and_save_chunks(text_content)
    if not chunks:
        print("No chunks generated")
        return False
    
    print(f"\nEmbedding and upserting {len(chunks)} chunks to namespace: {namespace}")
    print(f"Using index: {index_name}")
    
    # Prepare vectors for batch upsert
    vectors = []
    for i, chunk in enumerate(chunks):
        # Generate embedding
        try:
            embedding_list = pc.inference.embed(
                model="multilingual-e5-large",
                inputs=[chunk['text']],
                parameters={"input_type": "passage", "truncate": "END"}
            )
            if not embedding_list or not embedding_list.data:
                print(f"Warning: No embedding generated for chunk {i}")
                continue
                
            embedding = embedding_list[0].values
            
            # Combine document metadata with chunk metadata
            chunk_metadata = {
                "company_name": metadata.get("company_name", ""),
                "fiscal_year": metadata.get("fiscal_year", ""),
                "document_type": metadata.get("document_type", ""),
                "document_url": metadata.get("document_url", ""),
                "top_level_heading": chunk.get("heading") or "",
                "subheading": chunk.get("subheading") or "",
                "chunk_text": chunk.get("text") or ""
            }
            
            # Add to vectors list
            vectors.append({
                "id": f"{metadata.get('company_name', 'unknown')}_{metadata.get('fiscal_year', 'unknown')}_{i}",
                "values": embedding,
                "metadata": chunk_metadata
            })
            
        except Exception as e:
            print(f"Error processing chunk {i}: {str(e)}")
            continue
    
    if not vectors:
        print("No vectors generated")
        return False
    
    # Batch upsert to Pinecone
    try:
        # Upsert in batches of 100
        batch_size = 100
        for i in range(0, len(vectors), batch_size):
            batch = vectors[i:i + batch_size]
            index.upsert(vectors=batch, namespace=namespace)
            print(f"Upserted batch {i//batch_size + 1} of {(len(vectors) + batch_size - 1)//batch_size}")
        
        print(f"Successfully indexed {len(vectors)} vectors in namespace: {namespace}")
        return True
        
    except Exception as e:
        print(f"Error upserting to Pinecone: {str(e)}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python indexing.py <input_file> [--metadata key=value ...]")
        return

    input_file = sys.argv[1]
    
    # Parse metadata from command line arguments
    metadata = {}
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--metadata" and i + 1 < len(sys.argv):
            key_value = sys.argv[i + 1].split("=")
            if len(key_value) == 2:
                metadata[key_value[0]] = key_value[1]
            i += 2
        else:
            i += 1

    # Ensure required metadata fields
    required_fields = ['company_name', 'fiscal_year', 'document_type']
    missing_fields = [field for field in required_fields if field not in metadata]
    
    if missing_fields:
        print(f"Missing required metadata fields: {', '.join(missing_fields)}")
        print("Please provide all required metadata using --metadata key=value")
        return

    # Get API key
    api_key = os.getenv("PINECONE_API_KEY")
    if not api_key:
        api_key = input("Enter your Pinecone API key: ").strip()
        if not api_key:
            print("No API key provided. Aborting.")
            return

    try:
        # Read the input file
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Process and index the content
        embed_and_upsert(content, metadata, api_key)
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
    except Exception as e:
        print(f"Error processing file: {str(e)}")

if __name__ == "__main__":
    main()