if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        new_height = 2 ** ((n + 1)//2 + 1) - 1
        print(new_height - 1 if n % 2 == 1 else new_height)