#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        m, n = list(map(int, input().split()))
        if n == m:
            print(0)
        elif n % m != 0:
            print(-1)
        else:
            x = n // m
            counter = 0
            while x > 1:
                if x % 2 == 0:
                    x //= 2
                    counter += 1
                elif x % 3 == 0:
                    x //= 3
                    counter += 1
                else:
                    break
            if x == 1:
                print(counter)
            else:
                print(-1)
