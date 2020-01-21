from random import choice
import string
class Game:
    def __init__(self):
        self.grid = []
        for _ in range(0, 9):
            self.grid.append(choice(string.ascii_uppercase))
    def is_valid(self, word):
            if word is '':
                return False
            return set(list(self.grid[0])) >= set(list(word))
