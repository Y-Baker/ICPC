#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        s = input()
        n = len(s)
        l1 = 0
        r2 = n - 1
        r1 = n // 2 - 1
        l2 = r1 + 2

        re = True
        while l1 <= r1:
            if not (s[l1] == s[r1] and s[l2] == s[r2] and s[l1] == s[r2]):
                re = False
                break
            l1 += 1
            r1 -= 1
            l2 += 1
            r2 -= 1
        if re:
            print("Yes")
        else:
            print("No")
