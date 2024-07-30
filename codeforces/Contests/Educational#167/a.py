#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        x, y = map(int, input().split())
        if y < 0 and y <= -2:
            print("NO")
        else:
            print("YES")
