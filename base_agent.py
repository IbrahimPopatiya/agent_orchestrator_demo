# base_agent.py
from openai import OpenAI
from dotenv import load_dotenv
import os
from  pathlib import Path


# print("API KEY:",os.getenv("OPENAI_API_KEY"))
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key=os.getenv("OPENAI_API_KEY")
print(api_key)
client = OpenAI(api_key=api_key)

class BaseAgent:
    def __init__(self, name, system_prompt, tools, memory):
        self.name = name
        self.system_prompt = system_prompt
        self.tools = tools
        self.memory = memory

    def run(self, task):
        # If tool exists, use it first
        if self.tools:
            for tool_name, tool_func in self.tools.items():
                try:
                    result = tool_func(task)

                    self.memory.add({
                        "agent": self.name,
                        "task": task,
                        "output": result
                    })

                    return f"[Tool:{tool_name}] {result}"

                except:
                    pass

        # fallback to LLM
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": task}
        ]

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        output = response.choices[0].message.content

        self.memory.add({
            "agent": self.name,
            "task": task,
            "output": output
        })

        return output