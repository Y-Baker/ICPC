#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        count = 0
        mapp = {}
        for i in arr:
            if i % 3 == 0:
                count += 1
            elif i % 3 == 1:
                mapp[1] = mapp.get(1, 0) + 1
            elif i % 3 == 2:
                mapp[2] = mapp.get(2, 0) + 1

        while mapp[1] > 0 and mapp[2] > 0:
            count += 1
            mapp[1] -= 1
            mapp[2] -= 1

        while mapp[1] >= 3:
            count += 1
            mapp[1] -= 3

        while mapp[2] >= 3:
            count += 1
            mapp[2] -= 3

        print(count)
