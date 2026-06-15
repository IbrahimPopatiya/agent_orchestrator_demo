# Agent Orchestrator Demo

A small multi-agent orchestration system written in Python. A central `Orchestrator` routes user input to specialized agents (research, calculator, writer), each backed by a shared `Memory` store for context across interactions.

## Components

- **Orchestrator** – routes incoming requests to the appropriate agent.
- **Research Agent** – handles research-style queries.
- **Calculator Agent** – handles arithmetic/calculation queries.
- **Writer Agent** – handles content-generation queries.
- **Memory** – shared state/context store used across agents.

## Running

```bash
python main.py
```

Type queries at the `>>` prompt; type `exit` to quit.

## Setup

Create a `.env` file with any required API keys (not committed to version control).
