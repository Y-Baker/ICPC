#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        product = 1
        min_val = min(arr)
        flag = True
        for i in range(n):
            if arr[i] == min_val and flag:
                product *= arr[i] + 1
                flag = False
            else:
                product *= arr[i]

        print(product)