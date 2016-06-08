if __name__ == '__main__':
    input()

    result = 0
    for n in map(int, input().split()):
        result ^= n

    print(result)