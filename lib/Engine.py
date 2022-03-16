class Engine:
    def __init__(self, dependencies) -> None:
        self.m_dependencies = dependencies
        self.m_ears = self.m_dependencies['ears']()
        self.m_voice = self.m_dependencies['voice']()
        self.m_memory = self.m_dependencies['memory']()         
        self.m_brain = self.m_dependencies['brain'](self.m_memory)   

    def run(self):
        state = False
        for phrase in self.m_ears.listen():
            words = phrase.split(' ')
            if words[0] == 'assistente':
                self.m_voice.play('beep.mp3')
                words = words[1:]
                state = True
            
            print(f'[{1 if state else 0}]> {" ".join(words)}')

            if state == True and len(words) > 0:
                phrase = ' '.join(words)
                sentence = self.m_brain.think(phrase)
                print(f'- {sentence}')
                self.m_voice.speak(sentence)
                state = False
