#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n, s = map(int, input().split())
        arr = list(map(int, input().split()))

        def can(x):
            arr2 = [0] * n
            for i in range(n):
                arr2[i] = arr[i] + (i + 1) * x
            arr2.sort()

            cnt = sum(arr2[:x])
            if cnt <= s:
                return (True, cnt)
            else:
                return (False, -1)

        l = 0
        r = n
        ans = (-1, -1)
        while l <= r:
            m = l + (r - l) // 2
            re = can(m)
            if re[0]:
                ans = (m, re[1])
                l = m + 1
            else:
                r = m - 1
        print(*ans)
