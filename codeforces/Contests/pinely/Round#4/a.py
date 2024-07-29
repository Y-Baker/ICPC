#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(max(a[::2]))        

