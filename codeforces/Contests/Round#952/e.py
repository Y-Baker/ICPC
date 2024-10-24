#!/usr/bin/env python3

def count_placements(x, y, z, k):
    max_placements = 0
    for a in range(1, x + 1):
        for b in range(1, y + 1):
            if k % (a * b):
                continue
            c = k // (a * b)
            ans = (x - a + 1) * (y - b + 1) * (z - c + 1)
            max_placements = max(max_placements, ans)
    return max_placements


t = int(input())
results = []
for _ in range(t):
    x, y, z, k = map(int, input().split())
    print(count_placements(x, y, z, k))
