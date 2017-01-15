
if __name__ == '__main__':
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))

    sum_a, sum_b = 0, 0

    for idx in range(3):
        if a[idx] > b[idx]: sum_a += 1
        elif a[idx] < b[idx]: sum_b += 1

    print(sum_a, sum_b)
