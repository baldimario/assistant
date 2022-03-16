from text_to_speech import speak
import playsound
import os
class Voice:
    def __init__(self, language='it') -> None:
        self.m_language = language

    def speak(self, response):
        response = response.replace('\n', '. ')
        speak(response, self.m_language, speak=True)
    
    def play(self, filename):
        soundpath = os.path.join(os.path.dirname(__file__), '..', 'assets', filename)
        playsound.playsound(soundpath, True)