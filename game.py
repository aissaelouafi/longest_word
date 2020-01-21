from random import choice
import string
import requests


class Game:
    def __init__(self):
        self.grid = []
        for _ in range(0, 9):
            self.grid.append(choice(string.ascii_uppercase))
    def is_valid(self, word):

            r = requests.get(f'https://wagon-dictionary.herokuapp.com/{word}')
            valid_word_from_dict = r.json()

            if word is '' or not valid_word_from_dict['found']:
                return False
            return set(list(self.grid[0])) >= set(list(word))
