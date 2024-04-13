#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        arr_sorted = sorted(arr)
        flag = True

        for idx in range(n):
            if arr[idx] % 2 != arr_sorted[idx] % 2:
                flag = False
                break

        print('YES' if flag else 'NO')

