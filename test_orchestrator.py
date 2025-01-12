import logging
import sys
from analysis_module_1_orchestrator import run_orchestration

# Configure logging with more detail
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('orchestrator_test.log')
    ]
)

# Test case: Comprehensive analysis plan for NVIDIA
test_plan = {
    "analysisType": "Growth and Competition Analysis",
    "company_namespace": "nvidia",
    "informationNeeds": [
        {
            "summary": "Revenue Growth Trends",
            "description": "Extract and analyze NVIDIA's revenue growth patterns, focusing on segment performance and quarterly trends",
            "tag": "financial",
            "dataSource": "10k",
            "stored": "revenue_growth"
        },
        {
            "summary": "Market Competition Analysis",
            "description": "Analyze NVIDIA's competitive position in the AI chip market, including market share and competitor movements",
            "tag": "competition",
            "dataSource": "web",
            "stored": "market_competition"
        },
        {
            "summary": "Product Innovation",
            "description": "Identify key developments in NVIDIA's AI and GPU product lines, including new releases and technological advances",
            "tag": "product",
            "dataSource": "web",
            "stored": "product_innovation"
        },
        {
            "summary": "Risk Assessment",
            "description": "Evaluate key risk factors, particularly related to semiconductor supply chain and market competition",
            "tag": "risk",
            "dataSource": "10k",
            "stored": "risk_factors"
        }
    ],
    "executionPlan": [
        {
            "stepName": "Financial Performance Analysis",
            "actions": [
                "Analyze revenue growth trends across segments",
                "Calculate key growth metrics",
                "Visualize quarterly performance trends"
            ]
        },
        {
            "stepName": "Competitive Position Evaluation",
            "actions": [
                "Assess market share data",
                "Compare with competitor movements",
                "Identify competitive advantages"
            ]
        },
        {
            "stepName": "Innovation Impact Analysis",
            "actions": [
                "Evaluate product development timeline",
                "Assess technological advantages",
                "Map innovation to market impact"
            ]
        },
        {
            "stepName": "Risk and Opportunity Synthesis",
            "actions": [
                "Synthesize key risks",
                "Identify growth opportunities",
                "Provide strategic recommendations"
            ]
        }
    ]
}

def main():
    try:
        logging.info("Starting orchestration test...")
        logging.info("Running with test plan for NVIDIA analysis")
        
        final_state = run_orchestration(test_plan)
        
        # Print execution results
        print("\n=== Execution Results ===")
        if isinstance(final_state["execution_output"], dict):
            print("\nDetailed Analysis:")
            print("-" * 50)
            detailed = final_state["execution_output"].get("detailed", "No detailed output available")
            print(detailed)
            
            print("\nSummary:")
            print("-" * 50)
            summary = final_state["execution_output"].get("summary", "No summary available")
            print(summary)
            
            # Also log to file
            logging.info("Analysis completed successfully")
            logging.info(f"Generated report length: {len(detailed)} characters")
            
            # Check if report was generated
            if len(detailed) < 100:  # Arbitrary threshold
                logging.warning("Generated report seems unusually short")
        else:
            error_msg = f"Unexpected execution output format: {final_state['execution_output']}"
            logging.error(error_msg)
            print(error_msg)
            
    except KeyboardInterrupt:
        logging.error("Process interrupted by user")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Orchestration test failed: {str(e)}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main() 