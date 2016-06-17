def reversability(n, max_num):
    temp_num, num_reverse = n, 0

    skip_factor = 0.1
    while temp_num > 0:
        num_reverse = num_reverse * 10 + temp_num % 10
        temp_num //= 10
        skip_factor *= 10

    val = n + num_reverse
    if (val % 10) % 2 == 0: return -1 * skip_factor

    while val > 0:
        if (val % 10) % 2 == 0: return 0
        val //= 10

    return 2 if num_reverse < max_num else 1


if __name__ == '__main__':
    for _ in range(int(input())):
        max_num = int(input())

        count = 0
        num = 11
        while num < max_num:
            factor = reversability(num, max_num)

            if factor > 0:
                count += factor
                num += 2
            elif factor == 0:
                num += 2
            else:
                num += -1 * factor

        print(count)
