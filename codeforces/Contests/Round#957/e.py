#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())
    for _ in range(t):
        n = int(input())
        n_str = str(n)
        digits = len(n_str)
        res = []

        def tryy(x, a):
            if a == x:
                s = 0
            else:
                division = x // digits
                remain = x % digits
                s = n_str * (a - division)
                s = s[:len(s) - remain]
                if len(s) > 10:
                    return 2
                if s == '':
                    s = 0
                else:
                    s = int(s)
            if n * a - x == s:
                return 0
            elif n * a - x > s:
                return 1
            else:
                return 2

        for a in range(1, 10001):
            l = 1
            r = min(10000,a*n)
            while l <= r:
                mid = l + (r - l) // 2
                ret = tryy(mid, a)
                if ret == 0:
                    if a != mid:
                        res.append([a, mid])
                    break
                elif ret == 1:
                    r = mid - 1
                elif ret == 2:
                    l = mid + 1
                else:
                    break

        print(len(res))
        for x in res:
            print(x[0], x[1])


