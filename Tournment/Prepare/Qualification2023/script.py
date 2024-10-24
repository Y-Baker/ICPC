#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        for i in range(1, 1000):
            if sum(map(int, str(i))) == 16:
                print(i)

