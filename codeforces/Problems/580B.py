#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n, d = map(int, input().split())
        data = []
        for _ in range(n):
            m, s = map(int, input().split())
            data.append((m, s))
        data.sort()
        for i in range(1, n):
            data[i] = (data[i][0], data[i][1] + data[i - 1][1])
        # print(data)
        maxx = -1
        for i in range(n):
            l = i
            r = n
            while l < r:
                mid = (l + r) // 2
                if data[mid][0] - data[i][0] >= d:
                    r = mid
                else:
                    l = mid + 1
            if i == 0:
                maxx = max(maxx, data[l - 1][1])
            else:
                maxx = max(maxx, data[l - 1][1] - data[i - 1][1])

        print(maxx)
