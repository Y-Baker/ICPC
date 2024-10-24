#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        s1, s2 = input().split()
        print(f"{s2[0]+s1[1:]} {s1[0]+s2[1:]}")
