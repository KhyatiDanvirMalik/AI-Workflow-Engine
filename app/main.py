from fastapi import FastAPI, HTTPException
from .engine import WorkflowEngine
from .workflow import create_code_review_workflow
from .models import RunInput, GraphInput
import uuid

app = FastAPI(title="AI Agent Workflow Engine")
 
GRAPH_REGISTRY = {
    "default_code_review": create_code_review_workflow()
}
RUN_HISTORY = {}

@app.get("/")
def home():
    return {"message": "Workflow Engine is Running"}

@app.post("/graph/create")
def create_graph(data: GraphInput):
    graph_id = str(uuid.uuid4())
    return {"graph_id": graph_id, "message": "Graph structure registered (mock)."}

@app.post("/graph/run")
async def run_graph(payload: RunInput, graph_id: str = "default_code_review"):
    workflow = GRAPH_REGISTRY.get(graph_id)
    
    if not workflow:
        raise HTTPException(status_code=404, detail="Graph not found")
    try:
        result = await workflow.run(payload.initial_state)
        
        run_id = str(uuid.uuid4())
        RUN_HISTORY[run_id] = result
        
        return {
            "run_id": run_id,
            "final_state": result["final_state"],
            "execution_log": result["log"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/graph/state/{run_id}")
def get_run_state(run_id: str):
    if run_id not in RUN_HISTORY:
        raise HTTPException(status_code=404, detail="Run ID not found")
    
    return RUN_HISTORY[run_id]