
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        b, w = map(int, input().strip().split(' '))
        x, y, z = map(int, input().strip().split(' '))

        print(b * min(x, y + z) + w * min(y, x + z))
