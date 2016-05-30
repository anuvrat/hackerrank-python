def sum_even_number_fibonacci_series(n):
    if n < 8: return 2
    if n < 34: return 10
    if n < 144: return 44

    a, b, current_sum = 34, 144, 44
    while n > b: a, b, current_sum = b, 4 * b + a, current_sum + b

    return current_sum


if __name__ == '__main__':
    for _ in range(int(input())):
        print(sum_even_number_fibonacci_series(int(input())))
