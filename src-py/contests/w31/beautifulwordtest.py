import unittest
from contests.w31.beautifulword import BeautifulWord


class TestBeautifulWord(unittest.TestCase):
    def test_1(self):
        w = 'abacaba'
        self.assertTrue(BeautifulWord().is_beautiful(w))

    def test_2(self):
        w = 'badd'
        self.assertFalse(BeautifulWord().is_beautiful(w))
