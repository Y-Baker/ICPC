#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        arr.sort()
        maxx = arr.pop()
        summ = sum(arr)
        if maxx == 0:
            re = 0
        elif maxx > summ:
            re = maxx - summ
        else:
            re = 1
        print(re)
