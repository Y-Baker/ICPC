#!/usr/bin/python3

from math import ceil
if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        n, m = input().split()
        # required is ceil(n × m)
        required = ceil(int(n) * float(m))

        arr = list(map(int, input().split()))
        for exam in arr:
            if exam >= 50:
                required -= 1
        if required <= 0:
            print("YES")
        else:
            print("NO")
