#!/bin/python3

vowels = "aeiouy"
consonants = "bcdfghjklmnpqrstvwyxz"


class BeautifulWord(object):
    def is_beautiful(self, word):
        last_char = word[0]

        for idx in range(1, len(word)):
            char = word[idx]

            if char == last_char or (char in vowels and last_char in vowels): return False

            last_char = char

        return True


if __name__ == '__main__':
    w = input().strip()

    print('Yes' if BeautifulWord().is_beautiful(w) else 'No')
