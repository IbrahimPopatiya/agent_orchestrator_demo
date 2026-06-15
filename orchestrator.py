# orchestrator.py

class Orchestrator:
    def __init__(self, agents):
        self.agents = agents

    def route(self, task):
        task_lower = task.lower()

        if "calculate" in task_lower or any(char.isdigit() for char in task):
            return self.agents["calculator"].run(task)

        elif "search" in task_lower or "find" in task_lower:
            return self.agents["research"].run(task)

        else:
            return self.agents["writer"].run(task)