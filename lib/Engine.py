class Engine:
    def __init__(self, dependencies) -> None:
        self.m_dependencies = dependencies
        self.m_ears = self.m_dependencies('ears')()
        self.m_voice = self.m_dependencies('voice')()
        self.m_brain = self.m_dependencies('brain')()
        self.m_memory = self.m_dependencies('memory')()            
        self.m_memory.set('ciao', 'ciao a te')
        self.m_memory.set('accendi la luce', 'ok, accendo la luce')
        self.m_memory.set('spegni la luce', 'ok, spengo la luce')
        self.m_memory.set('fantastico', 'grazie')

    def run(self):
        for phrase in self.m_ears.listen():
            sentence = self.brain.think(phrase)
            self.m_voice.speak(sentence)
