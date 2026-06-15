# calculator_agent.py
from base_agent import BaseAgent

def calculator(expr):
    try:
        expr = expr.lower().replace("calculate", "").strip()
        return str(eval(expr))
    except:
        return "error"

class CalculatorAgent(BaseAgent):
    def __init__(self, memory):
        super().__init__(
            name="CalculatorAgent",
            system_prompt="""
You are a math agent.
Solve problems step by step.
""",
            tools={"calculator": calculator},
            memory=memory
        )