#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))

        idx = range(1, n+1)
        mapp = sorted(zip(arr, idx), key=lambda x: x[0])

        l = 0
        r = n - 1
        re = 'IMPOSSIBLE'
        while l < r:
            if mapp[l][0] + mapp[r][0] == k:
                re = str(mapp[l][1]) + ' ' + str(mapp[r][1])
                break
            elif mapp[l][0] + mapp[r][0] > k:
                r -= 1
            else:
                l += 1
        print(re)
