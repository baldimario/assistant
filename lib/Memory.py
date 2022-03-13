class Memory:
    def __init__(self) -> None:
        self.m_data = {}
    
    def save(self):
        with open('memories.json') as f:
            f.write(self.m_data)

    def load(self):
        with open('memories.json') as f:
            self.m_data = f.read()

    def get(self, key):
        return self.m_data[key]
    
    def set(self, key, value):
        self.m_data[key] = value