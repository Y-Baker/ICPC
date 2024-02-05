#!/usr/bin/python3

if __name__ == '__main__':
    n, p, q = map(int, input().split())
    word = input()
    
    for i in range(n // p + 1):
        for j in range(n // q + 1):
            if i * p + j * q == n:
                print(i + j)
                for k in range(i):
                    print(word[k * p:k * p + p])
                for k in range(i, i + j):
                    print(word[k * q:k * q + q])
                exit()
