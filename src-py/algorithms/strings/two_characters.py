

def get_distribution(s):
    distribution = [0] * 26

    for c in s:
        distribution[ord(c) - ord('a')] += 1

    return distribution


def check_string(s, a, b):
    last_char = '0'
    for i in range(1, len(s)):
        if s[i] == a or s[i] == b:
            if s[i] == last_char: return False
            last_char = s[i]

    return True


if __name__ == '__main__':
    s_len = int(input().strip())
    s = input().strip()

    distribution = get_distribution(s)

    max_len = 0
    for i in range(26):
        if distribution[i] == 0: continue

        for j in range(i + 1, 26):
            val = distribution[i] + distribution[j]
            if val < max_len: continue

            diff = distribution[i] - distribution[j]
            if diff < 0: diff *= -1

            if distribution[j] == 0 or diff > 1: continue

            if check_string(s, chr(i + ord('a')), chr(j + ord('a'))): max_len = val

    print(max_len)
