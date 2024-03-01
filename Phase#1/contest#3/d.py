#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        n, m = list(map(int, input().split()))
        s = []
        count = {}
        for _ in range(n):
            s.append(input())

        for i in range(m):
            for p1 in range(n):
                for p2 in range(p1 + 1, n):
                    if i == 0:
                        count[(p1, p2)] = abs(ord(s[p1][i]) - ord(s[p2][i]))
                    else:
                        count[(p1, p2)] += abs(ord(s[p1][i]) - ord(s[p2][i]))

        print(min(count.values()))
