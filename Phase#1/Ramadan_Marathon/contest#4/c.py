#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())
    is_cube = lambda x: round(x ** (1/3)) ** 3 == x
    for _ in range(t):
        n = int(input())
        re = False
        i = 1
        while i ** 3 < n:
            x = n - i ** 3
            if is_cube(x):
                re = True
                break
            i += 1

        print("YES" if re else "NO")
