#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n = int(input())
        grid = []
        ans = [-1 for i in range(n)]
        maxx = -1
        values = set()
        for i in range(n):
            row = list(map(int, input().split()))
            grid.append(row)
            values.update(row)
            maxx = max(maxx, max(row))
            sett = set()
            for ele in row:
                if ele in sett:
                    ans[i] = ele
                    break
                else:
                    sett.add(ele)

        idx = ans.index(-1)
        ans[idx] = maxx
        idx = ans.index(-1)
        ans[idx] = maxx + 1

        print(*ans)
