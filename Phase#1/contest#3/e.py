#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        even = arr[0] % 2
        odd = arr[1] % 2
        flag = True

        for idx, i in enumerate(arr):
            if idx % 2 == 0:
                if i % 2 != even:
                    flag = False
                    break
            if idx % 2 != 0:
                if i % 2 != odd:
                    flag = False
                    break
        if flag:
            print('YES')
        else:
            print('NO')

