![Agent Orchestrator Demo](https://placehold.co/1200x300/1e293b/ffffff?text=Agent+Orchestrator+Demo)

# 🤖 Agent Orchestrator Demo

> A lightweight multi-agent orchestration system in Python — route user requests to specialized agents (research, calculator, writer) backed by shared memory.

---

## ✨ Features

- 🧠 **Central Orchestrator** that intelligently routes user input to the right agent
- 🔎 **Research Agent** for search/lookup-style queries
- ➗ **Calculator Agent** for arithmetic and numeric queries
- ✍️ **Writer Agent** for general content-generation tasks
- 💾 **Shared Memory** store for context across all agents
- 🖥️ Simple interactive CLI loop (`>>` prompt)

---

## 🧩 Architecture / How It Works

```
                ┌─────────────────┐
   User Input → │   Orchestrator   │
                └────────┬─────────┘
                          │ routes based on
                          │ keywords/content
        ┌─────────────────┼─────────────────┐
        ▼                  ▼                  ▼
 ┌─────────────┐   ┌──────────────┐   ┌──────────────┐
 │ Research     │   │ Calculator   │   │ Writer       │
 │ Agent        │   │ Agent        │   │ Agent        │
 └──────┬───────┘   └──────┬───────┘   └──────┬───────┘
        │                  │                  │
        └──────────────────┼──────────────────┘
                            ▼
                     ┌─────────────┐
                     │   Memory    │
                     └─────────────┘
```

- **Orchestrator** (`orchestrator.py`) — Inspects each incoming message and decides which agent should handle it:
  - Contains digits or the word "calculate" → 🧮 **Calculator Agent**
  - Contains "search" or "find" → 🔎 **Research Agent**
  - Otherwise → ✍️ **Writer Agent**
- **Research Agent** (`research_agent.py`) — Handles research/lookup-style queries.
- **Calculator Agent** (`calculator_agent.py`) — Handles arithmetic and numeric calculations.
- **Writer Agent** (`writer_agent.py`) — Handles general content-generation requests.
- **Memory** (`memory.py`) — A shared store that all agents read from / write to, giving the system context across interactions.

---

## 📂 Project Structure

```
agent_orchestrator_demo/
├── main.py              # Entry point - interactive CLI loop
├── orchestrator.py       # Routes requests to the correct agent
├── research_agent.py     # Research/search agent
├── calculator_agent.py   # Arithmetic/calculation agent
├── writer_agent.py        # Content-generation agent
├── memory.py              # Shared memory/context store
├── .env                   # Environment variables (not committed)
└── README.md
```

---

## 🖼️ Screenshots / Demo

![Demo](https://placehold.co/800x400?text=Demo+Screenshot)

![Demo 2](https://placehold.co/800x400?text=CLI+Walkthrough)

> 📝 Add your own screenshots here to showcase the orchestrator in action.

---

## 🛠️ Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/IbrahimPopatiya/agent_orchestrator_demo.git
   cd agent_orchestrator_demo
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Create a `.env` file in the project root with any required API keys (not committed to version control):

   ```env
   API_KEY=your_api_key_here
   ```

---

## 🚀 Run

Start the orchestrator:

```bash
python main.py
```

### Example usage

```
>> calculate 12 * 4
Response: 48

>> search latest AI news
Response: ...

>> write a short poem about the ocean
Response: ...

>> exit
```
