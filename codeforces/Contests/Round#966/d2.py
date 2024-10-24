#!/usr/bin/python3

# from itertools import permutations, combinations
from collections import defaultdict

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        lst = list(map(int,input().split()))
        s = input()
        firstL = 0
        lastR = 0
        for i in range(n) :
            if s[i] == 'L' :
                firstL = i
                break
        for i in range(n-1,-1,-1) :
            if s[i] == 'R' :
                lastR = i
                break
        cnt = 0
        while firstL < lastR :
            for i in range(firstL , lastR +1):
                cnt += lst[i]
            
            Found = False
            for i in range(firstL+1,lastR):
                if s[i] == 'L':
                    firstL = i
                    Found = True
                    break
            if not Found:
                break
            Found = False
            for i in range(lastR-1, firstL, -1):
                if s[i] == 'R':
                    Found = True
                    lastR = i
                    break
            if not Found:
                break

        print(cnt)