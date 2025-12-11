import inspect
from typing import Callable, Dict, Any, List, Optional

class WorkflowEngine:
    def __init__(self):
        self.nodes: Dict[str, Callable] = {}
        self.edges: Dict[str, Any] = {}  
        self.entry_point: str = ""

    def add_node(self, name: str, func: Callable):
        self.nodes[name] = func

    def set_entry_point(self, name: str):
        self.entry_point = name

    def add_edge(self, from_node: str, to_node: str):
        self.edges[from_node] = to_node

    def add_conditional_edge(self, from_node: str, condition_func: Callable, mapping: Dict[Any, str]):
        self.edges[from_node] = (condition_func, mapping)

    async def run(self, initial_state: Dict[str, Any]):
        state = initial_state.copy()
        current_node_name = self.entry_point
        execution_log = []

        if not current_node_name:
            raise ValueError("No entry point defined.")

        while current_node_name:
            execution_log.append(f"Executing: {current_node_name}")
          
            node_func = self.nodes.get(current_node_name)
            if not node_func:
                break 
            result = node_func(state)
            if result:
                state.update(result)

            edge_info = self.edges.get(current_node_name)

            if edge_info is None:
                current_node_name = None
            elif isinstance(edge_info, str):
                current_node_name = edge_info
            elif isinstance(edge_info, tuple):
                condition_func, mapping = edge_info
                outcome = condition_func(state)
                current_node_name = mapping.get(outcome)
            else:
                current_node_name = None

        return {"final_state": state, "log": execution_log}
