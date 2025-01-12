import os
from typing import List, Dict
from dotenv import load_dotenv

def load_env_variables(required_vars: List[str] = None) -> Dict[str, str]:
    """
    Load environment variables from .env file or Replit secrets.
    Args:
        required_vars: List of required environment variable names
    Returns:
        Dict of loaded environment variables
    Raises:
        ValueError if any required variables are missing
    """
    # First try loading from .env file
    load_dotenv()
    
    # If running in Replit, secrets are automatically loaded into os.environ
    
    if required_vars:
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        if missing_vars:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing_vars)}\n"
                "Please set these in your Replit secrets or .env file."
            )
    
    # Return all loaded variables
    return {
        var: os.getenv(var)
        for var in (required_vars if required_vars else os.environ)
    }

# Core variables needed across modules
CORE_VARIABLES = [
    "GEMINI_API_KEY",
    "PINECONE_API_KEY"
]

# Import pipeline specific variables
IMPORT_VARIABLES = [
    "EXA_API_KEY",
    "SEC_API_KEY",
    "LLAMA_CLOUD_API_KEY"
]

def load_core_variables():
    """Load core variables required for analysis modules."""
    return load_env_variables(CORE_VARIABLES)

def load_import_variables():
    """Load variables required for import pipeline."""
    return load_env_variables(CORE_VARIABLES + IMPORT_VARIABLES) 