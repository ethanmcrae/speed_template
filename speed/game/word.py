from game.actor import Actor
from game.point import Point
from random import randint

class Word(Actor):
    def __init__(self, word):
        super().__init__()
        self._word = word
        self._position = Point(randint(1, 59), 1)
        self._velocity = Point(0, 1)

    def get_word(self):
        return self._word
    
    def get_position(self):
        return self._position

    def get_velocity(self):
        return self._velocity