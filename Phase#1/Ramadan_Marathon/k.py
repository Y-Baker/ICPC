#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        if n & 1: # odd
            print("Mike")
        else:
            minn = arr[0]
            turn = 0
            for i in range(1, n):
                if arr[i] < minn:
                    turn = i
                    minn = arr[i]

            if turn & 1:
                print("Mike")
            else:
                print("Joe")
