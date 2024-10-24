#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        cnt = 0
        for one in arr:
            if one >= arr[k-1] and one > 0:
                cnt += 1
        print(cnt)
