#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())
    gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
    for _ in range(t):
        
        n = int(input())

