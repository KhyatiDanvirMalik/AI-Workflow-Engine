# AI Agent Workflow Engine (Mini-LangGraph)

## Project Overview
This project is a lightweight, backend-only AI Workflow Engine built using Python and FastAPI. [cite_start]It is designed to orchestrate agentic workflows where tasks are defined as **Nodes** (functions) and the flow is controlled by **Edges** (transitions)[cite: 10, 11].

[cite_start]Unlike linear pipelines, this engine supports **State Management**, **Conditional Branching**, and **Looping**, allowing for self-correcting agent behaviors (e.g., "review code until quality score > 80")[cite: 20, 21].

## Features
* [cite_start]**Graph-Based Architecture:** Define workflows as a sequence of connected steps[cite: 11].
* [cite_start]**Shared State:** A dictionary-based state that persists and evolves as it passes through nodes[cite: 17].
* [cite_start]**Cyclic Execution:** Supports loops for iterative refinement (e.g., Refine -> Check -> Refine)[cite: 21].
* [cite_start]**Tool Registry:** Modular function definitions that serve as the "tools" for the agent[cite: 24].
* [cite_start]**FastAPI Interface:** Exposes REST endpoints to create, run, and inspect workflows[cite: 29].

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
    
    * [cite_start]**Endpoint:** `http://127.0.0.1:8000/graph/run` [cite: 34]
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

* [cite_start]**Nodes & Edges:** Defines workflows as Python functions (nodes) connected by transitions (edges)[cite: 16, 19].
* [cite_start]**Shared State:** Passes a state dictionary through every node, allowing data to persist and evolve across the workflow[cite: 17].
* [cite_start]**Conditional Branching:** Supports dynamic routing (e.g., if `quality_score < threshold`, route to a refinement node)[cite: 20].
* [cite_start]**Looping:** Allows cycles in the graph, enabling agents to retry tasks recursively until a specific condition is met[cite: 21].
* [cite_start]**Tool Registry:** Nodes function as tools that can perform specific logic (e.g., analysis, extraction)[cite: 24].

---

## 3. Future improvements 
* **Persistence:** Currently, state and history are stored in-memory. [cite_start]I would add SQLite or PostgreSQL integration to persist graph runs and query past states[cite: 39].
* [cite_start]**Async/Background Execution:** For long-running agent tasks, I would move execution to background workers to prevent blocking the HTTP response[cite: 42].
* [cite_start]**Streaming Logs via WebSockets:** I would implement a WebSocket endpoint to stream execution logs to the client in real-time[cite: 41].
