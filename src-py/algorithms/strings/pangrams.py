if __name__ == '__main__':
    occurances = [0] * 26
    for c in input().lower():
        idx = ord(c) - ord('a')
        if 0 <= idx < 26: occurances[idx] += 1

    missing_chars_count = sum(1 for c in occurances if c == 0)
    print("pangram") if missing_chars_count == 0 else print("not pangram")