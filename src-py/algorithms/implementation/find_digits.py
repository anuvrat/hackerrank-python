if __name__ == '__main__':
    for _ in range(int(input())):
        num_str = input()
        num = int(num_str)
        count = 0
        for c in num_str:
            if c != '0' and num % int(c) == 0: count += 1

        print(count)