#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        cnt = 0
        maxx = arr[0]
        summ = arr[0]
        for i in range(1, n):
            if summ - maxx == maxx:
                cnt += 1
            maxx = max(maxx, arr[i])
            summ += arr[i]
        if summ - maxx == maxx:
            cnt += 1
        print(cnt)

