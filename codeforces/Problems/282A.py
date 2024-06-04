#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())
    x = 0
    for _ in range(t):
        s = input()
        if s == 'X++' or s == '++X':
            x += 1
        else:
            x -= 1
    print(x)

