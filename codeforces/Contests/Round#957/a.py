#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        a, b, c = map(int, input().split())
        # get max of a * b * c and we have 5 ones to add
        arr = sorted([a, b, c])
        cnt = 5

        
        while cnt > 0:
            arr[0] += 1
            cnt -= 1
            arr.sort()

        print(arr[0] * arr[1] * arr[2])