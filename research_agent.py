# research_agent.py
from base_agent import BaseAgent

def fake_search(query):
    return f"Search result for: {query}"

class ResearchAgent(BaseAgent):
    def __init__(self, memory):
        super().__init__(
            name="ResearchAgent",
            system_prompt="""
You are a research agent.
You gather and summarize information clearly.
""",
            tools={"search": fake_search},
            memory=memory
        )