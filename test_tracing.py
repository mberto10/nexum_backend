from analysis_module_0_plan import run_planning_workflow
import os
from dotenv import load_dotenv
from langsmith import Client

# Load environment variables
load_dotenv()

# Initialize LangSmith client
client = Client()

def test_planning_workflow():
    # Test query
    test_query = "Analyze Amazon's revenue growth and profit margins for the last 3 years"
    test_company = "Amazon"
    
    print("Starting test planning workflow...")
    print(f"Query: {test_query}")
    print(f"Company: {test_company}")
    print(f"Project: {os.getenv('LANGCHAIN_PROJECT')}")
    
    try:
        # Run the workflow
        result = run_planning_workflow(test_query, test_company)
        
        # Print metrics
        print("\nExecution Metrics:")
        if "metrics" in result:
            metrics = result["metrics"]
            print(f"Latency: {metrics['latency']:.2f} seconds")
            print(f"Token Usage: {metrics['token_usage']}")
        
        # Print analysis plan
        print("\nAnalysis Plan:")
        print(f"Type: {result.get('analysis_type')}")
        print("\nInformation Needs:")
        for need in result.get('information_needs', []):
            print(f"- {need.get('summary')}")
        
        print("\nView traces at:")
        print("https://smith.langchain.com/")
        print(f"Project: {os.getenv('LANGCHAIN_PROJECT')}")
        print("Tags: planning, gemini")
        
    except Exception as e:
        print(f"Error during execution: {str(e)}")

if __name__ == "__main__":
    test_planning_workflow() 