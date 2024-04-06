#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        re = []
        cnt = 0
        re.append(1)

        for i in range(1, n):
            if arr[i] == 1:
                re.append(1)
                cnt += 1
            else:
                re[cnt] += 1

        print(len(re))
        print(' '.join(map(str, re)))
