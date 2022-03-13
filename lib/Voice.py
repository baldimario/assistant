from text_to_speech import speak

class Voice:
    def __init__(self, language='it') -> None:
        self.m_language = language

    def speak(self, response):
        speak(response, self.m_language, speak=True)