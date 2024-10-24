#!/usr/bin/python3

from collections import defaultdict

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))
        m = int(input())
        arr3 = list(map(int, input().split()))
        freq = defaultdict(int)
        for one in arr3:
            freq[one] += 1
        still = set()
        flag = True
        for i in range(n):
            if arr1[i] != arr2[i]:
                if arr2[i] in freq and freq[arr2[i]] > 0:
                    freq[arr2[i]] -= 1
                else:
                    flag = False
                    break
        if flag:
            print("YES")
        else:
            print("NO")

