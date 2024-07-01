#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        s = filter(lambda x : x not in ["a", "o", "y", "e", "u", "i"], input().lower())
        print('.' + '.'.join(s))
        
