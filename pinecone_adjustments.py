import os
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

def init_pinecone():
    """Initialize Pinecone client."""
    api_key = os.getenv('PINECONE_API_KEY')
    if not api_key:
        raise ValueError("PINECONE_API_KEY environment variable not set")
    
    return Pinecone(api_key=api_key)

def delete_namespace_records(index_name: str, namespace: str = ""):
    """
    Delete all records in a specific namespace.
    For serverless indexes, this is a safe operation.
    For pod-based indexes, this should be done in batches.
    """
    pc = init_pinecone()
    index = pc.Index(index_name)
    
    try:
        # Delete all vectors in the namespace
        index.delete(delete_all=True, namespace=namespace)
        print(f"Successfully deleted all records in namespace '{namespace}' of index '{index_name}'")
    except Exception as e:
        print(f"Error deleting records: {str(e)}")

def delete_and_recreate_index(index_name: str, dimension: int = 1536):
    """
    Delete an existing index and recreate it.
    This is the most efficient way to remove all data from an index.
    """
    pc = init_pinecone()
    
    try:
        # Check if index exists
        if index_name in pc.list_indexes().names():
            print(f"Deleting existing index '{index_name}'...")
            pc.delete_index(index_name)
            # Wait for deletion to complete
            time.sleep(5)
        
        # Create new serverless index
        print(f"Creating new index '{index_name}'...")
        pc.create_index(
            name=index_name,
            dimension=dimension,
            metric='cosine',
            spec=ServerlessSpec(
                cloud='aws',
                region='us-west-2'
            )
        )
        print(f"Successfully recreated index '{index_name}'")
        
    except Exception as e:
        print(f"Error managing index: {str(e)}")

def check_index_stats(index_name: str):
    """
    Check the current statistics of the index.
    Useful for verifying deletion and monitoring data freshness.
    """
    pc = init_pinecone()
    index = pc.Index(index_name)
    
    try:
        stats = index.describe_index_stats()
        print("\nIndex Statistics:")
        print(f"Total vector count: {stats.total_vector_count}")
        print(f"Namespaces: {stats.namespaces}")
        return stats
    except Exception as e:
        print(f"Error checking index stats: {str(e)}")
        return None

if __name__ == "__main__":
    # Example usage
    INDEX_NAME = "sec-filings"  # Replace with your index name
    
    # Delete all records in default namespace
    delete_namespace_records(INDEX_NAME)
    
    # Check stats after deletion
    check_index_stats(INDEX_NAME)
    
    # Optionally, delete and recreate the index
    # delete_and_recreate_index(INDEX_NAME) 