#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        s = input()
        flag = [False, False]
        l = 0
        r = len(s) - 1
        count = 0

        while l < r:
            if flag == [True, True]:
                for i in range(l, r + 1):
                    if s[i] == '0':
                        count += 1
                break
            else:
                if s[l] == '1':
                    flag[0] = True
                if s[r] == '1':
                    flag[1] = True
            if not flag[0]:
                l += 1
            if not flag[1]:
                r -= 1     
        print(count)
