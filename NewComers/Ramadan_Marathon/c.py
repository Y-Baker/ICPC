#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        n, k = list(map(int, input().split()))
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a.sort()
        b.sort(reverse=True)
        i = 0
        j = 0
        while(k > 0 and i < n and j < n):
            if a[i] < b[j]:
                a[i] = b[j]
                i += 1
                j += 1
                k -= 1
            else:
                break
        print(sum(a))
