import random
from .engine import WorkflowEngine

def extract_functions(state):
    code = state.get("code", "")
    func_count = code.count("def ")
    return {"function_count": func_count, "analysis_step": "extraction_complete"}

def check_complexity(state):
    current_score = random.randint(1, 100) 
    return {"quality_score": current_score}

def detect_issues(state):
    score = state.get("quality_score", 0)
    issues = []
    if score < 50:
        issues.append("Complexity too high")
        issues.append("Missing docstrings")
    elif score < 80:
        issues.append("Variable naming could be better")
    
    return {"issues": issues}

def suggest_improvements(state):
    return {"status": "improvements_applied", "iteration": state.get("iteration", 0) + 1}

def quality_gate(state):
    score = state.get("quality_score", 0)
    iteration = state.get("iteration", 0)
    
    if iteration > 3:
        return "pass"

    if score >= 80:
        return "pass"
    else:
        return "fail"

def create_code_review_workflow():
    workflow = WorkflowEngine()

    workflow.add_node("extract", extract_functions)
    workflow.add_node("complexity", check_complexity)
    workflow.add_node("issues", detect_issues)
    workflow.add_node("improve", suggest_improvements)
    
    workflow.set_entry_point("extract")
    workflow.add_edge("extract", "complexity")
    workflow.add_edge("complexity", "issues")
    
    workflow.add_conditional_edge(
        "issues",
        quality_gate,
        {
            "fail": "improve",
            "pass": None # End
        }
    )

    workflow.add_edge("improve", "complexity")
    
    return workflow