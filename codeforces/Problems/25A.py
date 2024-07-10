#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        even = 0
        odd = 0
        idx1 = 0
        idx2 = 0
        for idx, val in enumerate(arr):
            if val % 2 == 0:
                even += 1
                idx1 = idx
            else:
                odd += 1
                idx2 = idx

        if even == 1:
            print(idx1 + 1)
        else:
            print(idx2 + 1)
