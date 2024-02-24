#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n, k = list(map(int, input().split(" ")))
        arr = list(map(int, input().split(" ")))

        arr.sort()
        count = 0
        for i in arr:
            if i <= arr[k - 1]:
                count += 1
        if k == 0 and arr[0] == 1:
            print(-1)
        elif k == 0 and arr[0] != 1:
            print(arr[k] - 1)
        elif k == count:
            print(arr[k - 1])
        else:
            print(-1)
