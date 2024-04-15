#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        n, m, k = map(int, input().split())
        if m <= 1:
            print("NO")
            continue
        most_common = (n / m).__ceil__()
        remain = n - most_common
        # print(_, remain, most_common)
        if remain > k:
            print("YES")
        else:
            print("NO")
