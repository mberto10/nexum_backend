
from api_service import app
import uvicorn
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    print("Starting server on http://0.0.0.0:3000")
    uvicorn.run(app, host="0.0.0.0", port=3000, log_level="info")
