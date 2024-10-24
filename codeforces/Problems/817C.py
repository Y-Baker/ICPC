#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    def fn(x):
        n = x * 10
        cnt = 0
        while x > 0:
            cnt += x % 10
            x = x // 10
        return n - cnt

    for _ in range(t):
        n, s = map(int, input().split())

        l = s // 10
        r = n // 10

# 1 2 3 4 5 6
        ans = n + 1
        while l <= r:
            mid = l + (r - l) // 2
            curr = fn(mid)
            if curr < s:
                l = mid + 1
            else:
                ans = mid * 10
                r = mid - 1

        print(n - ans + 1)
