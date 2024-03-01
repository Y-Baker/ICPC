#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        n, q = list(map(int, input().split()))

        arr = list(map(int, input().split()))
        for _ in range(q):
            l, r, k = list(map(int, input().split()))
            s = sum(arr[:l - 1]) + sum(arr[r:]) + k * (r - l + 1)
            if s % 2 == 1:
                print("YES")
            else:
                print("NO")
