#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n, t = map(int, input().split())
        arr = list(map(int, input().split()))
        prefix = [0] * (n+1)
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + arr[i-1]
        summ = prefix[n]
        def can(x):
            for i in range(n-x+1):
                if prefix[i+x] - prefix[i] <= t:
                    return True
            return False

        l = 0
        r = n
        ans = 0
        while l <= r:
            m = l + (r-l)//2
            if can(m):
                ans = max(ans, m)
                l = m + 1
            else:
                r = m - 1
        print(ans)

