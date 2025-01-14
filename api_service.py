import os
import sys
import logging

# Configure logging
# Ensure logs directory exists
os.makedirs('logs', exist_ok=True)

# Configure logging with absolute path
log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs', 'api_service.log')
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ],
    force=True  # Force configuration even if already configured
)

# Add immediate log message to verify logging is working
logging.info("API Service logging initialized")
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import analysis_module_0_plan as analysis_planner
from env_setup import load_core_variables

# Load environment variables at startup
env_vars = load_core_variables()

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://2c9e21e6-fd5d-45b4-8580-84b7305a5ae4-00-h4gay4hmypih.kirk.replit.dev",
        "https://*.replit.dev",
        "https://*.repl.co"
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
    max_age=3600
)

# Request/Response Models
class SearchRequest(BaseModel):
    query: str

class Company(BaseModel):
    name: str
    ticker: str
    lastUpdated: str

class SearchResponse(BaseModel):
    companies: List[Company]

class CommandRequest(BaseModel):
    command: str
    type: str
    entryId: str

class CommandResponse(BaseModel):
    content: str

# Error handler
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": True,
            "message": str(exc.detail),
            "status": exc.status_code
        }
    )

# Routes
@app.get("/")
async def root():
    return {"message": "Welcome to the API Service"}

@app.post("/api/search")
async def search(request: SearchRequest) -> SearchResponse:
    try:
        # Mock company search for now - replace with actual implementation
        companies = [
            Company(
                name="NVIDIA",
                ticker="NVDA",
                lastUpdated=datetime.now().isoformat()
            )
        ]
        return SearchResponse(companies=companies)
    except Exception as e:
        logging.error(f"Error during search: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/command")
async def execute_command(request: CommandRequest) -> CommandResponse:
    try:
        logging.info("\n=== New API Command Request ===")
        logging.info(f"Type: {request.type}")
        logging.info(f"Command: {request.command}")
        logging.info(f"EntryId: {request.entryId}")
        
        if not request.command or not request.type or not request.entryId:
            raise HTTPException(status_code=400, detail="Missing required fields")
            
        # Return test response
        response_content = "it worked"
        logging.info(f"Sending response: {response_content}")
        return CommandResponse(content=response_content)
        
    except Exception as e:
        logging.error(f"Error processing command: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 3000))
    uvicorn.run(app, host="0.0.0.0", port=port, forwarded_allow_ips="*")