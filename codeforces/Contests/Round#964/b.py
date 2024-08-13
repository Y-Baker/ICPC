#!/usr/bin/python3

# from itertools import permutations, combinations
from collections import defaultdict

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        a1, a2, b1, b2 = map(int, input().split())

        roundA = 0
        roundB = 0
        totalA = 0
        totalB = 0

        if a1 > b1:
            roundA += 1
            if a2 > b2:
                roundA += 1
            elif a2 < b2:
                roundB += 1
        elif a1 < b1:
            roundB += 1
            if a2 > b2:
                roundA += 1
            elif a2 < b2:
                roundB += 1
        if roundA > roundB:
            totalA += 1
        roundA = 0
        roundB = 0

        if a1 > b2:
            roundA += 1
            if a2 > b1:
                roundA += 1
            elif a2 < b1:
                roundB += 1
        elif a1 < b2:
            roundB += 1
            if a2 > b1:
                roundA += 1
            elif a2 < b1:
                roundB += 1
        if roundA > roundB:
            totalA += 1
        roundA = 0
        roundB = 0

        if a2 > b1:
            roundA += 1
            if a1 > b2:
                roundA += 1
            elif a1 < b2:
                roundB += 1
        elif a2 < b1:
            roundB += 1
            if a1 > b2:
                roundA += 1
            elif a1 < b2:
                roundB += 1
        if roundA > roundB:
            totalA += 1
        roundA = 0
        roundB = 0

        if a2 > b2:
            roundA += 1
            if a1 > b1:
                roundA += 1
            elif a1 < b1:
                roundB += 1
        elif a2 < b2:
            roundB += 1
            if a1 > b1:
                roundA += 1
            elif a1 < b1:
                roundB += 1
        if roundA > roundB:
            totalA += 1
        roundA = 0
        roundB = 0

        print(totalA)
        
