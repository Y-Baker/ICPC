#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        summ = sum(arr)
        l = 0
        r = summ
        re = False
        while l <= r:
            mid = l + (r-l)//2
            if mid * mid == summ:
                re = True
                break
            elif mid * mid < summ:
                l = mid + 1
            else:
                r = mid - 1

        if re:
            print("YES")
        else:
            print("NO")

