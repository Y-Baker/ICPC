#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        fruits = list(map(int, input().split()))
        heights = list(map(int, input().split()))
        if n == 1 and fruits[0] <= k:
            print(1)
            continue
        if min(fruits) > k:
            print(0)
            continue

        currFruit = fruits[0]
        window = 1
        start = 0
        i = 1
        maxx = 0

        while i < n:
            currFruit += fruits[i]
            if heights[i-1] % heights[i] == 0 and currFruit <= k:
                window += 1
                maxx = max(maxx, window)
            else:
                maxx = max(maxx, window)
                start = i
                window = 1
                currFruit = fruits[i]
            i += 1

        print(maxx)