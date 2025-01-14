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
origins = ["*"]  # Allow all origins in development

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
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
    print("\n")
    print("="*50)
    print("INCOMING API REQUEST")
    print("="*50)
    print(f"COMMAND: {request.command}")
    print(f"TYPE: {request.type}")
    print(f"ENTRY ID: {request.entryId}")
    print("="*50)
    
    logging.info("\n=== New API Command Request ===")
    logging.info(f"Type: {request.type}")
    logging.info(f"Command: {request.command}")
    logging.info(f"EntryId: {request.entryId}")

    try:
        if request.type == "analysis":
            logging.info("Executing analysis workflow...")
            # Execute analysis using the planner module
            result = analysis_planner.run_planning_workflow(
                user_query=request.command,
                company_name=request.entryId,
                use_context_cache=True
            )

            # Save the plan and get the markdown file path
            output_file = analysis_planner.save_plan_as_markdown(result)

            # Read the markdown content
            with open(output_file, 'r') as f:
                content = f.read()

            logging.info(f"Analysis completed successfully, generated file: {output_file}")
            return CommandResponse(content=content)
        elif request.type == "auto":
            # Handle auto type commands
            logging.info(f"Executing auto command: {request.command}")
            response_content = f"Executed {request.command} with {request.type} (ID: {request.entryId})"
            logging.info(f"Auto command completed: {response_content}")
            return CommandResponse(content=response_content)
        else:
            error_msg = f"Unsupported command type: {request.type}"
            logging.error(error_msg)
            raise HTTPException(status_code=400, detail=error_msg)
    except Exception as e:
        error_msg = f"Error executing command: {str(e)}"
        logging.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 3000))
    uvicorn.run(app, host="0.0.0.0", port=port, forwarded_allow_ips="*")