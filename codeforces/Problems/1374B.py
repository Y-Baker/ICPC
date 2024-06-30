#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        if n == 1:
            print(0)
            continue
        cnt = 0
        flag = 0
        while n > 1:
            if n % 6 == 0:
                flag = 0
                n //= 6
            else:
                if flag > 3:
                    print(-1)
                    break
                n *= 2
                flag += 1
            cnt += 1
        if flag <= 3:
            print(cnt)

