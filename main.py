
from api_service import app
import uvicorn
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    print("\n" + "="*50)
    print("Starting API server on http://0.0.0.0:3000")
    print("="*50 + "\n")
    uvicorn.run(app, host="0.0.0.0", port=3000, log_level="debug", forwarded_allow_ips="*")
