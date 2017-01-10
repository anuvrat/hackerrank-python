
if __name__ == '__main__':
    for _ in range(int(input().strip())):
        x = int(input().strip())

        count = 0
        val = 1
        while x:
            if not (x & 1): count += val

            x >>= 1
            val *= 2

        print(count)