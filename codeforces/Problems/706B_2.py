#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        q = int(input())

        a.sort()

        for _ in range(q):
            x = int(input())
            ans = 0
            l = 0
            r = n - 1

# 1 4 6 9 12 15

            while l <= r:
                m = (l + r) // 2
                if a[m] <= x:
                    ans = m + 1
                    l = m + 1
                else:
                    r = m - 1
            print(ans)
