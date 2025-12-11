# AI Agent Workflow Engine

## Project Overview
This project is a lightweight, backend-only AI Workflow Engine built using Python and FastAPI. It is designed to orchestrate agentic workflows where tasks are defined as **Nodes** (functions) and the flow is controlled by **Edges** (transitions).

Unlike linear pipelines, this engine supports **State Management**, **Conditional Branching**, and **Looping**, allowing for self-correcting agent behaviors (e.g., "review code until quality score > 80").

## Features
* **Graph-Based Architecture:** Define workflows as a sequence of connected steps.
* **Shared State:** A dictionary-based state that persists and evolves as it passes through nodes.
* **Cyclic Execution:** Supports loops for iterative refinement (e.g., Refine -> Check -> Refine).
* **Tool Registry:** Modular function definitions that serve as the "tools" for the agent.
* **FastAPI Interface:** Exposes REST endpoints to create, run, and inspect workflows.

## Tech Stack
* **Language:** Python 3.9+
* **Framework:** FastAPI
* **Server:** Uvicorn
* **Validation:** Pydantic

## Project Structure
```text
/app
  ├── engine.py       # Core logic (Graph, Nodes, State handling)
  ├── workflow.py     # Sample implementation (Code Review Agent)
  ├── main.py         # API Endpoints
  ├── models.py       # Pydantic data models
```

## 1. How to run
**Prerequisites:** Python 3.8+

1.  **Install Dependencies:**
    ```bash
    pip install fastapi uvicorn pydantic
    ```

2.  **Start the Server:**
    Run this command from the project root:
    ```bash
    uvicorn app.main:app --reload
    ```

3.  **Test the Workflow:**
    Send a `POST` request to trigger the sample "Code Review" agent.
    
    * **Endpoint:** `http://127.0.0.1:8000/graph/run`
    * **Body (JSON):**
        ```json
        {
          "initial_state": {
            "code": "def example(): pass",
            "iteration": 0
          }
        }
        ```
    * *Alternatively, use the interactive Swagger UI at `http://127.0.0.1:8000/docs`.*

---

## 2. What the workflow engine supports
This engine implements a simplified directed cyclic graph (DCG) architecture that includes:

* **Nodes & Edges:** Defines workflows as Python functions (nodes) connected by transitions (edges).
* **Shared State:** Passes a state dictionary through every node, allowing data to persist and evolve across the workflow.
* **Conditional Branching:** Supports dynamic routing (e.g., if `quality_score < threshold`, route to a refinement node).
* **Looping:** Allows cycles in the graph, enabling agents to retry tasks recursively until a specific condition is met.
* **Tool Registry:** Nodes function as tools that can perform specific logic (e.g., analysis, extraction).

---

## 3. Future Improvements(What I would improve with more time)
* **Persistence:** Currently, state and history are stored in-memory. I would add SQLite or PostgreSQL integration to persist graph runs and query past states.
* **Async/Background Execution:** For long-running agent tasks, I would move execution to background workers to prevent blocking the HTTP response.
* **Streaming Logs via WebSockets:** I would implement a WebSocket endpoint to stream execution logs to the client in real-time.
