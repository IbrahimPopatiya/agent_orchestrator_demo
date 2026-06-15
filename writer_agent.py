# writer_agent.py
from base_agent import BaseAgent

class WriterAgent(BaseAgent):
    def __init__(self, memory):
        super().__init__(
            name="WriterAgent",
            system_prompt="""
You are a writer agent.
Write clean, structured responses.
""",
            tools={},
            memory=memory
        )