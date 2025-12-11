from pydantic import BaseModel
from typing import Dict, Any, Optional, List

class GraphInput(BaseModel):
    nodes: List[str]
    edges: Dict[str, str]

class RunInput(BaseModel):
    initial_state: Dict[str, Any]