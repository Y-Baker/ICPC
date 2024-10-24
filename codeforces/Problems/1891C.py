#!/usr/bin/python3

from math import ceil
if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        cnt = 0
        power = 0
        for i in range(n):
            if i == n - 1:
                if power >= arr[i] and arr[i] > 1:
                    power = 0
                    cnt += 1
                else:
                    need = ceil((power + arr[i]) / 2) + 1
                    cnt += need - 1
            else:
                if power >= arr[i] and arr[i] > 1:
                    power = 0
                    cnt += 1
                else:
                    power += arr[i]
                    cnt += arr[i]
        print(cnt)
