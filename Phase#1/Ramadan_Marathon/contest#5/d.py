#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        mapp = {}
        for i in arr:
            if i in mapp:
                mapp[i] += 1
            else:
                mapp[i] = 1

        maxx = 0
        for i in mapp:
            curr = max(mapp.get(i + 1, 0), mapp.get(i - 1, 0))
            maxx = max(maxx, curr + mapp[i])

        print(maxx)
