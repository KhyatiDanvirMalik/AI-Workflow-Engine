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
