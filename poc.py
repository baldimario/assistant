import speech_recognition as sr
from text_to_speech import speak
import fasttext
import fasttext.util
import numpy as np

short_language = 'it'
language = 'it-IT'

fasttext.util.download_model(short_language, if_exists='ignore') 
ft = fasttext.load_model('cc.it.300.bin')

#for index, name in enumerate(sr.Microphone.list_microphone_names()):
#    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

recognizer = sr.Recognizer()
microphone = sr.Microphone()


commands = [
    ['Accendi la luce', 'Ok, accendo la luce'],
    ['Spegni la luce', 'Ok, spengo la luce'],
    ['Fantastico', 'Grazie']
]

command_sentences = []
for command in commands:
    words = [ft[word] for word in command[0].split(' ') if word in ft.words]
    sentence = np.mean(words, axis=0)
    command_sentences.append(sentence)

print('Listening...')
while True:
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        command = recognizer.recognize_google(audio, language=language)
        print(command)
        words = [ft[word] for word in command.split(' ') if word in ft.words]
        sentence = np.mean(words, axis=0)
        
        distances = [np.linalg.norm(sentence - command_sentence) for command_sentence in command_sentences]
        min_idx = np.argmin(distances)
        if(distances[min_idx] > 0.5):
            command_internal = 'Non ho capito'
            response = 'Non ho capito'
        else:
            command_internal = commands[min_idx][0]
            response = commands[min_idx][1]

        if len(words) > 0:
            print(sentence, command_internal, response)
            speak(response, short_language, speak=True)