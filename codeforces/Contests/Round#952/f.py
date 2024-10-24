#!/usr/bin/python3

from math import ceil
if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        h, n = map(int, input().split())
        damage = list(map(int, input().split()))
        cooldown = list(map(int, input().split()))

        def can(x):
            curr = h
            for i in range(n):
                rounds = ceil(x/cooldown[i])
                curr -= rounds * damage[i]
                if curr <= 0:
                    return True
            return False

        l = 0
        r = 10000000000000000010
        minn = 10000000000000000010
        while l <= r:
            mid = (l + r) // 2
            if can(mid):
                r = mid - 1
                minn = min(minn, mid)
            else:
                l = mid + 1
        print(minn)
