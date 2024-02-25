#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        n, k = list(map(int, input().split(" ")))
        arr = list(map(int, input().split(" ")))

        arr.sort()

        if len(arr) == 1:
            print(0)
            continue

        longest = 0
        l = 0
        r = 1

        while (r < len(arr)):
            if arr[r] - arr[r - 1] <= k:
                r += 1
            else:
                longest = max(longest, r - l)
                l = r
                r = l + 1

        longest = max(longest, r - l)
        print(n - longest)
