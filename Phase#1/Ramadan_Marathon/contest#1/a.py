#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    SHOULD_BE = "YES"
    for _ in range(t):
        s = input().upper()

        if s == SHOULD_BE:
            print("YES")
        else:
            print("NO")
