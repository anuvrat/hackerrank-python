import unittest
from contests.w31.zeroonegame import ZeroOneGame


class TestBeautifulWord(unittest.TestCase):
    def test1(self):
        sequence = [1, 0, 0, 1]
        self.assertFalse(ZeroOneGame().does_first_player_win(sequence))

    def test2(self):
        sequence = [1, 0, 1, 0, 1]
        self.assertTrue(ZeroOneGame().does_first_player_win(sequence))

    def test3(self):
        sequence = [0, 0, 0, 0, 0, 0]
        self.assertFalse(ZeroOneGame().does_first_player_win(sequence))

    def test4(self):
        sequence = [0, 0]
        self.assertFalse(ZeroOneGame().does_first_player_win(sequence))

    def test5(self):
        sequence = [0]
        self.assertFalse(ZeroOneGame().does_first_player_win(sequence))

    def test6(self):
        sequence = [0, 0, 1, 0]
        self.assertFalse(ZeroOneGame().does_first_player_win(sequence))

    def test7(self):
        sequence = [0, 0, 1, 0, 0]
        self.assertTrue(ZeroOneGame().does_first_player_win(sequence))

    def test8(self):
        sequence = [0, 1, 0]
        self.assertTrue(ZeroOneGame().does_first_player_win(sequence))

    def test9(self):
        sequence = [1, 0, 1]
        self.assertFalse(ZeroOneGame().does_first_player_win(sequence))

    def test10(self):
        sequence = [1, 0, 0]
        self.assertFalse(ZeroOneGame().does_first_player_win(sequence))

    def test11(self):
        sequence = [0, 1, 1]
        self.assertFalse(ZeroOneGame().does_first_player_win(sequence))
