#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        s = list(input().strip())
        for i in range(0, n, 2):
            if i == 0:
                s[i] = '('
            else:
                if s[i-1] == '(':
                    s[i] = ')'
                else:
                    s[i] = '('
        cnt = 0

        stack = []
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) > 0:
                    x = stack.pop()
                    cnt += i - x
        print(cnt)
