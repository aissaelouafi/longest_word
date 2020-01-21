# tests/test_game.py
import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)
    def test_word_is_valid(self):
        game = Game()
        game.grid = list(['FJULOLWSOAZTOBP'])
        self.assertEqual(game.is_valid('FOOTBALL'), True)

    def test_if_word_empty(self):
        game = Game()
        game.grid = ['']
        self.assertEqual(game.is_valid(''),False)
