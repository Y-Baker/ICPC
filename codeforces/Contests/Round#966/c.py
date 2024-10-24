#!/usr/bin/python3

# from itertools import permutations, combinations
from collections import defaultdict

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        mapp = defaultdict(list)
        for i in range(n):
            mapp[arr[i]].append(i)
        q = int(input())
        while q:
            valid = True
            q -= 1
            x = input()
            if len(x) != n:
                print("NO")
                continue
            freq = defaultdict(int)
            for i in range(n):
                freq[x[i]] += 1
            for i in range(n):
                if len(mapp[arr[i]]) != freq[x[i]]:
                    valid = False
                    break
                else:
                    compare = x[i]
                    for j in mapp[arr[i]]:
                        if x[j] != compare:
                            valid = False
                            break
            print("YES" if valid else "NO")
