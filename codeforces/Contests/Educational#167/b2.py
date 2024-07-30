#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        a = input()
        b = input()
        p1 = 0
        p2 = 0
        prev = 0
        cnt = len(a)
        while p1 < len(a):
            while p2 < len(b) and a[p1] != b[p2]:
                p2 += 1
            if p2 == len(b):
                p1 += 1
                p2 = prev
            else:
                if prev != p2:
                    cnt += p2 - prev

                prev = p2 + 1
                p1 += 1
                p2 += 1

        cnt += len(b) - prev
        print(cnt)