#!/bin/python3


def find_shortest_path():
    states = [(0, 0, 0)]

    grid = [[]] * n
    for i in range(n):
        grid[i] = [max_moves] * n

    while states:
        curr_state = states.pop(0)
        if curr_state[0] < 0 or curr_state[1] < 0 or curr_state[0] >= n or curr_state[1] >= n or curr_state[2] >= max_moves:
            continue

        if curr_state[2] >= grid[curr_state[0]][curr_state[1]]:
            continue

        if curr_state[0] == n - 1 and curr_state[1] == n - 1:
            return curr_state[2]

        grid[curr_state[0]][curr_state[1]] = curr_state[2]

        states.extend([
            (curr_state[0] + a + 1, curr_state[1] + b + 1, curr_state[2] + 1),
            (curr_state[0] + a + 1, curr_state[1] - b - 1, curr_state[2] + 1),
            (curr_state[0] - a - 1, curr_state[1] + b + 1, curr_state[2] + 1),
            (curr_state[0] - a - 1, curr_state[1] - b - 1, curr_state[2] + 1),
            (curr_state[0] + b + 1, curr_state[1] + a + 1, curr_state[2] + 1),
            (curr_state[0] + b + 1, curr_state[1] - a - 1, curr_state[2] + 1),
            (curr_state[0] - b - 1, curr_state[1] + a + 1, curr_state[2] + 1),
            (curr_state[0] - b - 1, curr_state[1] - a - 1, curr_state[2] + 1)
        ])


if __name__ == '__main__':
    n = int(input().strip())
    max_moves = n * n + 1
    # your code goes here

    moves = [[]] * (n - 1)
    for i in range(n - 1):
        moves[i] = [-1] * (n - 1)

    for a in range(n - 1):
        for b in range(a, n - 1):
            move_length = find_shortest_path()
            moves[a][b] = moves[b][a] = move_length if move_length else -1

    for i in range(n - 1):
        print(" ".join(map(str, moves[i])))

