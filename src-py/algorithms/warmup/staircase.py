if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        blanks = ' ' * (n - i - 2)
        symbols = '#' * (i + 1)
        print(blanks, symbols) if i < n - 1 else print(symbols)