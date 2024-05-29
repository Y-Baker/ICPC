#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    def fun(x, i):
        re = abs(x - i)
        if re == 0:
            return 0
        return re - 1

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        median = sum(arr) // n

        def cost(x):
            return sum(fun(x, i) for i in arr)

        l = min(arr)
        r = max(arr)

        while l <= r:
            mid = l + (r - l) // 2
            x, y = cost(mid), cost(mid + 1)
            if y > x:
                r = mid - 1
            else:
                l = mid + 1

        print(l, cost(l))
