#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        arr.sort()
        a = arr[:n:2]
        b = arr[1:n:2]

        # check if a is distinct
        if len(set(a)) != len(a) or len(set(b)) != len(b):
            print("NO")
            continue
        else:
            print("YES")
            print(len(a))
            print(*a)
            print(len(b))
            print(*b[::-1])
