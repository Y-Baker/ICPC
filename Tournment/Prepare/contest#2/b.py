#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())
    arr = [3, 1, 4, 1, 5, 9]
    chars = 'ABCDEFG'
    prefix = {}
    curr = 0
    for i in range(len(arr)):
        prefix[chars[i]] = curr
        curr += arr[i]
    prefix['G'] = curr

    for _ in range(t):
        x, y = input().split()
        print(abs(prefix[x] - prefix[y]))
