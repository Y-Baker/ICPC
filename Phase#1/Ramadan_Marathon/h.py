#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n = int(input())
        re = []

        while n > 0:
            if n % 7 == 0:
                re.extend([7] * (n // 7))
                break
            re.append(4)
            if n - 4 < 0:
                re = -1
                break
            n -= 4

        if re == -1:
            print(-1)
        else:
            re.sort()
            print(''.join(map(str, re)))
