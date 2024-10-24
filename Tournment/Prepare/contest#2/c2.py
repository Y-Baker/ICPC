#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n = int(input())
        listt = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]
        sorted_mapp = sorted(listt, key=lambda x: (x[0] / (x[1] + x[0]), -(x[0] + x[1])), reverse=True)
        print(*[x[2] for x in sorted_mapp])
