#!/bin/python3


class ZeroOneGame(object):
    def does_first_player_win(self, sequence):
        if len(sequence) <= 2: return False

        self._transform_single_ones(sequence)

        count = 0
        n = len(sequence)
        for idx in range(n):
            if idx == 0:
                if sequence[0] == 0 and sequence[1] == 0: count += 1
            elif idx == n - 1:
                if sequence[n - 1] == 0 and sequence[n - 2] == 0: count += 1
            else:
                if sequence[idx] == 0 and not (sequence[idx - 1] == 1 and sequence[idx + 1] == 1): count += 1

        return True if count % 2 == 1 else False

    def _transform_single_ones(self, s):
        for idx in range(1, len(s) - 1):
            if s[idx] == 1 and s[idx - 1] == 0 and s[idx + 1] == 0:
                s[idx] = 0

if __name__ == '__main__':
    game = ZeroOneGame()

    for _ in range(int(input().strip())):
        n = int(input().strip())
        seq = list(map(int, input().strip().split(' ')))

        print('Alice' if game.does_first_player_win(seq) else 'Bob')
