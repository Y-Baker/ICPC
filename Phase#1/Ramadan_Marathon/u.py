#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    # O(n) worse case
    for _ in range(t):
        n = int(input())
        x = input()

        re = ''
        i = n - 1
        while i >= 0:
            if i > 1 and x[i] == '0':
                re = chr(int(x[i-2:i]) + 96) + re
                i -= 3
            else:
                re = chr(int(x[i]) + 96) + re
                i -= 1
        print(re)
