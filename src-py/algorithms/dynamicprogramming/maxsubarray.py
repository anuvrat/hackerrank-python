def find_max_sums(arr):
    max_till_here, max_contiguous, max_non_contiguous = 0, 0, 0

    all_negative = True
    for n in arr:
        max_non_contiguous += max(n, 0)

        max_till_here = max(max_till_here + n, 0)
        max_contiguous = max(max_till_here, max_contiguous)

        if n > 0: all_negative = False

    return (max(arr), max(arr)) if all_negative else (max_contiguous, max_non_contiguous)


if __name__ == '__main__':
    for _ in range(int(input())):
        input()
        arr = list(map(int, input().split()))
        a, b = find_max_sums(arr)

        print(a, b)