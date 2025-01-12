<user_instructions>

Help me write this into a structured architecture document for referencing my planned agent architecture. It should be very comprehensive and include details on the functionality of each module and how they interact with each other, as well as notes on the optimal design choice and implementation. 

## Core Modules

1. Import Pipeline (details in @import_pipeline.py and @import_0_search.py, @import_1_retrieval.py, @import_2_parsing.py, @import_3_indexing.py)
2. Analysis Pipeline (initial draftdetails in @analysis_module_plan.py and @analysis_module_infogathering_orchestrator.py, sub-graph vector search in @analysis_module_vectordb.py and analysis_module_web_search.py)
3. Execution Pipeline (intiial draft details in @analysis_module_execution.py)

# Functionality
Import Pipeline findes, downloads, chunks and indexes the 10k financial documents.

Analysis Pipeline:
1. First, user query is analyzed and a plan is created
2. Orchestrator parses the plan and passes it (in parallel) into the information gathering sub-graphs
3. Each Subgraph (vector search, web search, etc) will receive information needs, choose a search plan and transform the information needs into queries, then execute the search and return the results to the orchestrator
4. Orchestrator will evaluate if the information gathered is enough to answer the user query, if not, it will refine the plan and pass it again into the information gathering sub-graphs
5. Once the information is enough, the orchestrator will pass the plan into the execution sub-graph
6. Execution sub-graph will parse the plan and the information gathered and if necessary re-fine the plan.
7. Execution will go step-by-step, each step receiving instructions, information gathered and the results and reasoning of the previous step (if any).
9. The executor will format the results and return the final answer to the user

</user_instructions>
