#!/usr/bin/python3

# from itertools import permutations, combinations
from collections import defaultdict

def calcWins(a1, a2, b1, b2):
    rounds = [
        (a1, b1, a2, b2),
        (a1, b2, a2, b1),
        (a2, b1, a1, b2),
        (a2, b2, a1, b1)
    ]
    win_count = 0
    cnt1 = 0
    cnt2 = 0
    
    for (s1, t1, s2, t2) in rounds:
        cnt1 = 0
        cnt2 = 0
    
        if s1 > t1:
            cnt1 += 1
        elif s1 < t1:
            cnt2 += 1

        if s2 > t2:
            cnt1 += 1
        elif s2 < t2:
            cnt2 += 1
        
        if cnt1 > cnt2:
            win_count += 1
    return win_count

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        a1, a2, b1, b2 = map(int, input().split())
        result = calcWins(a1, a2, b1, b2)
        print(result)

