#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        while True:
            try:
                (x1, y1) = map(int, input().split())
                break
            except ValueError:
                continue

        (x2, y2) = map(int, input().split())
        (x3, y3) = map(int, input().split())

        cnt = 0
        if x1 == x2 == x3 or y1 == y2 == y3:
            if x3 in range(min(x1, x2) + 1, max(x1, x2)) or y3 in range(min(y1, y2) + 1, max(y1, y2)):
                cnt += 2
        cnt += abs(x1 - x2) + abs(y1 - y2)

        print(cnt)
