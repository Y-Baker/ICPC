#!/usr/bin/python3

# from itertools import permutations, combinations
from collections import defaultdict

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n = input()
        arr = list(map(int, input().split()))
        minn = arr[0]
        maxx = arr[0]
        valid = True
        for i in range(1, len(arr)):
            if arr[i] < minn:
                if minn - arr[i] > 1:
                    valid = False
                    break
                minn = arr[i]
            elif arr[i] > maxx:
                if arr[i] - maxx > 1:
                    valid = False
                    break
                maxx = arr[i]
        print("YES" if valid else "NO")
