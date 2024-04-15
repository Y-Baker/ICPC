#!/usr/bin/python3

def solve(n):
    re = 0
    flag = 0
    if n == 0:
        return 0
    while (n > 0):
        if n % 10 == 1:
            flag += 1
        re += 1
        n = n // 10
    if re & 1 == 0:
        flag += 1
    res = (re / 2).__ceil__()
    if flag == 1:
        res -= 1
    return res

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n = int(input())
        print(solve(n))
