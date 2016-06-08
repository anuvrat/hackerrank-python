def bin(s):
    return str(s) if s <= 1 else bin(s >> 1) + str(s & 1)


def padded_bin(s, d):
    bin_s = bin(s)
    return bin_s if len(bin_s) == d else '0' * (d - len(bin_s)) + bin_s


def flip_bits(s):
    return ''.join(str(abs(1 - int(c))) for c in s)


if __name__ == '__main__':
    for _ in range(int(input())):
        print(int(flip_bits(padded_bin(int(input()), 32)), 2))