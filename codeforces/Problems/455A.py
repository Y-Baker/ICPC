#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n = int(input())
        cnt = -1
        def mapp(x):
            global cnt
            cnt += 1
            return (int(x), cnt)
        data = list(map(mapp, input().split()))
        data = sorted(data, key=lambda x: (-x[0], x[1]))
        re = 0
        while data:
            re += data[0][0]
            before = -1
            after = float('inf')
            to_delete = [0, 0, data[0]]
            for i in range(1, len(data)):
                if data[i][1] < data[0][1] and data[i][1] > before:
                    before = data[i][1]
                    to_delete[0] = data[i]
                if data[i][1] > data[0][1] and data[i][1] < after:
                    after = data[i][1]
                    to_delete[1] = data[i]
            for one in to_delete:
                if one != 0:
                    data.remove(one)
            to_delete = [0, 0, 0]

        print(re)

