#!/usr/bin/python3
from math import ceil, log

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        def solve():
            n = int(input())
            arr = list(map(int, input().split()))
            cnt = 0

            def check(arr):
                for i in range(n - 1):
                    if arr[i] >= arr[i + 1]:
                        return False
                return True

            def fn(a, b):
                if a == b:
                    return 1, a // 2
                x = ceil(log(a/b, 2))
                return x, a // (2 ** x)

            while not check(arr):
                for i in range(n - 1):
                    if arr[i] >= arr[i + 1]:
                        if arr[i + 1] == 0:
                            print(-1)
                            return
                        x, arr[i] = fn(arr[i], arr[i+1])
                        cnt += x

            print(cnt)


        solve()
