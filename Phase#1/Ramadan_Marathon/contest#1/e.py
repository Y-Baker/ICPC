#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        freq = [0 for _ in range(100)]

        for i in range(n):
            freq[arr[i] - 1] += 1

        print(max(freq))
