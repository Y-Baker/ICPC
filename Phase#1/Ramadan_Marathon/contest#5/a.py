#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n = int(input())
        re = ("Mahmoud", "Bashar")
        if n % 2 == 0:
            flag = 0
        else:
            flag = 1

        print(re[flag])

