#!/usr/bin/python3

def subsequence(a, b):
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
        j += 1
    return i == len(a)

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())
        a = input()
        b = input()

        ans = 0
        i = 0
        j = 0
        while i < n and j < m:
            if a[i] == b[j]:
                i += 1
                ans += 1
            j += 1

        print(ans)
