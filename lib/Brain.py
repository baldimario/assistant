import fasttext
import fasttext.util
import numpy as np
import subprocess
class Brain:
    def __init__(self, memory, language='it') -> None:
        self.m_language = language
        self.m_memory = memory
        self.m_memory.load()
        fasttext.util.download_model(self.m_language, if_exists='ignore') 
        self.m_ft = fasttext.load_model('cc.it.300.bin')
        self.m_hooks = self.m_memory.get_hooks()
        self.m_hooks_vec = [self.sentence2vec(hook) for hook in self.m_hooks if hook is not '_']
        print('ready')

    def sentence2vec(self, sentence):
        words = [self.m_ft[word] for word in sentence.split(' ') if word in self.m_ft.words]
        if len(words) > 1:
            return np.mean(words, axis=0)
        else:
            return words[0]

    def recall(self, phrase_vec):
        distances = [np.linalg.norm(phrase_vec - hook_vec) for hook_vec in self.m_hooks_vec]
        min_idx = np.argmin(distances)
        if(distances[min_idx] > 0.5):
            return None
        else:
            return self.m_hooks[min_idx]

    def think(self, phrase):
        phrase_vec = self.sentence2vec(phrase)
        response_hook = self.recall(phrase_vec)
        if response_hook in self.m_hooks:
            response_cmd = self.m_memory.get(response_hook)
        else:
            response_cmd = self.m_memory.get('_')
        output = subprocess.check_output(['sh', '-c', response_cmd]).decode('utf-8')
        return output
