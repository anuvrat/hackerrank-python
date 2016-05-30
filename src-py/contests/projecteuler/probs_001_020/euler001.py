def sum_of_numbers(n):
    return (n * (n + 1)) >> 1


def sum_of_multiples(n):
    multiples_of_3 = n // 3
    multiples_of_5 = n // 5
    multiples_of_15 = n // 15

    return int(sum_of_numbers(multiples_of_3)) * 3 + \
           int(sum_of_numbers(multiples_of_5)) * 5 - \
           int(sum_of_numbers(multiples_of_15)) * 15


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        print(sum_of_multiples(n - 1))