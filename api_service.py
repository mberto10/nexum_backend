import logging
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
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
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
        if request.type == "analysis":
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

            return CommandResponse(content=content)
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Unsupported command type: {request.type}"
            )
    except Exception as e:
        logging.error(f"Error executing command: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)