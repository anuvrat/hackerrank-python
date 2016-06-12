if __name__ == "__main__":
    n = int(input()) - 1
    arr = list(map(int, input().split()))

    e = arr[n]
    i = n - 1
    while i >= 0:
        if arr[i] > e:
            arr[i + 1] = arr[i]

            print(' '.join(map(str, arr)))

            if i == 0:
                arr[i] = e
                print(' '.join(map(str, arr)))
        else:
            arr[i + 1] = e
            print(' '.join(map(str, arr)))
            break

        i -= 1
