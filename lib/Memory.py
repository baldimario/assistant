import os
import json
class Memory:
    def __init__(self) -> None:
        self.m_data = {}
        self.m_memoriespath = os.path.join(os.path.dirname(__file__), '..', 'data', 'memory.json')
    
    def save(self):
        with open(self.m_memoriespath) as f:
            f.write(self.m_data)

    def load(self):
        with open(self.m_memoriespath) as f:
            self.m_data = json.loads(f.read())

    def get_hooks(self):
        return list(self.m_data.keys())

    def get(self, key):
        return self.m_data[key]
    
    def set(self, key, value):
        self.m_data[key] = value