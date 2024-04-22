#!/usr/bin/python3

"""Run Time Error"""

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        def solve():
            s = list(input())
            costs = list(map(int, input().split()))
            n = len(s)

            def get_char(lower, upper=None):
                if not upper:
                    for i in range(26):
                        if costs[i] == lower:
                            return chr(i+97)
                else:
                    for i in range(26):
                        if costs[i] <= upper and costs[i] >= lower:
                            return chr(i+97)

            def get_cost(s):
                cnt = 0
                for i in range(1, n):
                    cnt += abs(costs[ord(s[i-1]) - 97]- costs[ord(s[i]) - 97])
                print(cnt)
                print(''.join(s))

            start = 0
            while s[start] == '?':
                start += 1
                if start >= n:
                    print(0)
                    print(''.join('a' for _ in range(n)))
                    break
            else:
                x = get_char(costs[ord(s[start]) - 97])
                s = [x for _ in range(start)] + s[start:]
                l = start
                while l < n:
                    while s[l+1] != '?':
                        l += 1
                        if l+1 >= n:
                            get_cost(s)
                            return

                    r = l+1
                    while s[r] == '?':
                        r += 1
                        if r >= n:
                            x = get_char(costs[ord(s[l]) - 97])
                            for i in range(l+1, n):
                                s[i] = x
                            # s = s[:l+1] + [get_char(costs[s[l]]) for _ in range(r-l-1)]
                            get_cost(s)
                            return
                    x = get_char(costs[ord(s[l]) - 97], costs[ord(s[r]) - 97])
                    for i in range(l+1, r):
                        s[i] = x
                    l = r
        solve()
