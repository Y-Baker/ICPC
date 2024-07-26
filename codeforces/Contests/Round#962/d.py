#!/usr/bin/python3

def count_triplets(n, x):
    count = 0
    for a in range(1, x + 1):
        for b in range(1, x - a + 1):
            if a * b > n:
                break
            max_c = max((n - a * b) // (a + b), 0)
            max_c = min(max_c, x - a - b)
            if max_c == 0:
                continue
            count += max(max_c, 0) 
    return count

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n, x = map(int, input().split())
        print(count_triplets(n, x))
