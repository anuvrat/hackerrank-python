def is_funny_string(s):
    r = s[::-1]

    is_funny = True
    for i in range(1, (len(s) + 1) // 2):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(r[i]) - ord(r[i-1])):
            is_funny = False
            break

    return is_funny


if __name__ == '__main__':
    for _ in range(int(input())):
        print("Funny" if is_funny_string(input()) else "Not Funny")