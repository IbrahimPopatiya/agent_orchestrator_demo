# memory.py
import json

class Memory:
    def __init__(self, file="memory.json"):
        self.file = file
        try:
            with open(file, "r") as f:
                self.data = json.load(f)
        except:
            self.data = []

    def add(self, entry):
        self.data.append(entry)
        with open(self.file, "w") as f:
            json.dump(self.data, f, indent=2)

    def get_all(self):
        return self.data