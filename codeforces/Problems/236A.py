#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        s = set(input())
        print('CHAT WITH HER!' if len(s) % 2 == 0 else 'IGNORE HIM!')

