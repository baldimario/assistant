from lib.Ears import Ears
from lib.Voice import Voice
from lib.Memory import Memory
from lib.Brain import Brain
from lib.Engine import Engine

def main():
    engine = Engine({
        'ears': Ears,
        'voice': Voice,
        'memory': Memory,
        'brain': Brain
    })

    engine.run()
    
if __name__ == '__main__':
    main()