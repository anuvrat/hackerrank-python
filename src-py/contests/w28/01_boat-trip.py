
if __name__ == "__main__":
    n, c, m = map(int, input().strip().split(' '))
    p = list(map(int, input().strip().split(' ')))

    print("No" if any(_ > c * m for _ in p) else "Yes")
