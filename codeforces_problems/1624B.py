#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        a, b, c = map(int, input().split())

        flag = False
        for i in range(3):
            if i == 0:
                x = 2 * b - c
                if x % a == 0 and x / a > 0:
                    flag = True
                    break
            if i == 1:
                x = (a + c) / 2
                if x % b == 0 and x / b > 0:
                    flag = True
                    break
            if i == 2:
                x = 2 * b - a
                if x % c == 0 and x / c > 0:
                    flag = True
                    break

        print("YES" if flag else "NO")
