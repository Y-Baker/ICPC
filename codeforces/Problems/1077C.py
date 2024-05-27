#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        mapp = {}
        summ = 0
        for i in range(n):
            summ += arr[i]
            if arr[i] not in mapp:
                mapp[arr[i]] = [i + 1]
            else:
                mapp[arr[i]].append(i + 1)

        re = set()
        for idx in range(n):
            remain = summ - 2 * arr[idx]
            if remain in mapp:
                re.update(filter(lambda x: x != idx + 1, mapp[remain]))

        print(len(re))
        print(*re)
