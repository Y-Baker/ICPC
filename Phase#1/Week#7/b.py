#!/usr/bin/python3

from bisect import bisect_left
if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())
        arr1 = sorted(map(int, input().split()))
        arr2 = sorted(map(int, input().split()))

        if n > m:
            n, m = m, n
            arr1, arr2 = arr2, arr1

        minn = float('inf')
        for i in arr1:
            idx = bisect_left(arr2, i)
            if idx < m:
                minn = min(minn, abs(arr2[idx] - i))
            idx -= 1
            if idx >= 0:
                minn = min(minn, abs(arr2[idx] - i))

        print(minn)
