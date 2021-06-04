from game.actor import Actor

class Welovejosh(Actor):
    def __init__(self):
        super().__init__()
        self._words = []

    def get_words(self):
        
        return self._words

    def remove_word(self, word):
        self._words.remove(word)

    def add_word(self, word):
        self._words.append(word)
