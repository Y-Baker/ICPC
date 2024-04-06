#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        arr.sort()

        i = 0
        while i < n - 1:
            if arr[i] + 1 < arr[i + 1]:
                break
            i += 1
        if i == n - 1:
            print("YES")
        else:
            print("NO")

