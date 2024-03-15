#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        sorted_arr = sorted(enumerate(arr), key=lambda x: x[1], reverse=True)
        counter = 0

        for idx, one in enumerate(sorted_arr):
            counter += one[1] * idx + 1

        print(counter)
        re = [one[0] + 1 for one in sorted_arr]
        print(" ".join(map(str, re)))
