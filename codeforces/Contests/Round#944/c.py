#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        a, b, c, d = map(int, input().split())
        flag = [0, 0]
        if a > b:
            a, b = b, a
        if c in range(a, b + 1):
            flag[0] = True
        else:
            flag[0] = False
        if d in range(a, b + 1):
            flag[1] = True
        else:
            flag[1] = False
        if flag[0] == flag[1]:
            print("NO")
        else:
            print("YES")
