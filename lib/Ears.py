import speech_recognition as sr

class Ears:
    def __init__(self, language='it') -> None:
        self.m_recognizer = sr.Recognizer()
        self.m_microphone = sr.Microphone()
        self.m_language = language

    def listen(self):
        with self.m_microphone as source:
            self.m_recognizer.adjust_for_ambient_noise(source)

            while True:
                audio = self.m_recognizer.listen(source)
                yield self.m_recognizer.recognize_google(audio, language=self.m_language)