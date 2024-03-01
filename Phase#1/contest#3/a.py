#!/usr/bin/python3

import math

def is_square(i: int) -> bool:
    return i == math.isqrt(i) ** 2

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if is_square(arr[i] * arr[j]):
                count += 1

    print(count)
