#!/usr/bin/python3
from math import sqrt
from collections import defaultdict

def prime_factors(n):
    factors = defaultdict(int)
    while n % 2 == 0:
        factors[2] += 1
        n //= 2
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            factors[i] += 1
            n //= i
    if n > 2:
        factors[n] += 1

    return factors

def find_b(a, c):
    if c % a != 0:
        return -1  # No such b exists

    a_factors = prime_factors(a)
    c_factors = prime_factors(c)
    
    b_factors = defaultdict(int)
    
    for prime, exp in c_factors.items():
        if prime in a_factors:
            if a_factors[prime] < exp:
                b_factors[prime] = exp
        else:
            b_factors[prime] = exp
    
    b = 1
    for prime, exp in b_factors.items():
        b *= prime ** exp
    
    return b

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        a, c = map(int, input().split())
        # a, c = sorted([a, c])
        b = find_b(a, c)
        print(b)
        

