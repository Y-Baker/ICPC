#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())
    compare = "codeforces"
    for _ in range(t):
        s = input()

        if len(s) < len(compare):
            print(-1)
        else:
            count = 0
            for i in range(len(s)):
                if s[i] != compare[i]:
                    count += 1

            print(count)
