#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        s = list(input())
        costs = list(map(int, input().split()))
        cnt = 0
        n = len(s)

        start = 0
        while s[start] == '?':
            start += 1
            if start >= n:
                print(0)
                print(''.join('a' for _ in range(n)))
                break
        else:
            s = [s[start] for _ in range(start)] + s[start:]
            while start < n:
                if s[start] == '?':
                    s[start] = s[start-1]
                start += 1

            for i in range(1, n):
                cnt += abs(costs[ord(s[i-1]) - 97]- costs[ord(s[i]) - 97])
            print(cnt)
            print(''.join(s))
