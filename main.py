# main.py

from memory import Memory
from research_agent import ResearchAgent
from calculator_agent import CalculatorAgent
from writer_agent import WriterAgent
from orchestrator import Orchestrator

memory = Memory()

research_agent = ResearchAgent(memory)
calculator_agent = CalculatorAgent(memory)
writer_agent = WriterAgent(memory)

agents = {
    "research": research_agent,
    "calculator": calculator_agent,
    "writer": writer_agent
}

orchestrator = Orchestrator(agents)

while True:
    user_input = input(">> ")

    if user_input == "exit":
        break

    response = orchestrator.route(user_input)
    print("\nResponse:", response)