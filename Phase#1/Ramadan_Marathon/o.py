#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        a.sort()
        days = 0
        i = 0
        while i < n:
            should_solve = days + 1
            if a[i] >= should_solve:
                i += 1
                days += 1
            else:
                i += 1
        print(days)
