#!/bin/python3

hackerrank = list("hackerrank")
hackerrank_length = len(hackerrank)


if __name__ == '__main__':
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()

        input_string = list(s)
        input_string_length = len(input_string)

        input_idx = hackerrank_idx = 0
        successful = False
        while not successful and input_idx < input_string_length and hackerrank_idx < hackerrank_length:
            if input_string[input_idx] == hackerrank[hackerrank_idx]:
                hackerrank_idx += 1
                if hackerrank_idx == hackerrank_length:
                    successful = True

            input_idx += 1

        print("YES" if successful else "NO")
