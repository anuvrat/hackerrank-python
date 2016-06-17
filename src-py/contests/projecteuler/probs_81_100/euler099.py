from heapq import heappush, heappop

import math

if __name__ == '__main__':
    heap = []
    log_map = {}
    for _ in range(int(input())):
        a, b = map(int, input().split())
        log_val = b * math.log2(a)
        heappush(heap, log_val)
        log_map[log_val] = (a, b)

    val = None
    for _ in range(int(input())):
        val = heappop(heap)

    a, b = log_map[val]
    print(a, b)
