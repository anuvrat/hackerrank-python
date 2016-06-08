def binary_search(arr, n, start_idx, end_idx):
    if start_idx == end_idx: return start_idx if arr[start_idx] == n else -1

    mid_idx = (start_idx + end_idx) // 2
    mid_val = arr[mid_idx]

    if mid_val == n: return mid_idx
    elif mid_val > n: return binary_search(arr, n, start_idx, mid_idx)
    else: return binary_search(arr, n, mid_idx, end_idx)

if __name__ == '__main__':
    v, n = int(input()), int(input())
    arr = list(map(int, input().split()))
    print(binary_search(arr, v, 0, n))