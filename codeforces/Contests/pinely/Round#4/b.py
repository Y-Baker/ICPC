#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        re = [0] * n
        vaild = True
        re[0] = arr[0]
        for i in range(1, n-1):
            re[i] = arr[i - 1] | arr[i]
            if re[i - 1] & re[i] != arr[i - 1]:
                vaild = False
                break
        re[-1] = arr[-1]
        if re[-2] & re[-1] != arr[-1]:
            vaild = False
        
        print(*re if vaild else [-1])

