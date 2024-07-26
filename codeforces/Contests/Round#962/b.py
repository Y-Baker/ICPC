#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        grid = [[] for _ in range(n)]
        for i in range(n):
            grid[i] = list(input())

        def printgrade(grade, n):
            for i in range(n):
                print(''.join(grade[i]))

        if k == 1:
            printgrade(grid, n)
            continue
        new_n = n // k
        new_grid = [[0] * new_n for _ in range(new_n)]
        for i in range(0, n, k):
            for j in range(0, n, k):
                new_grid[i // k][j // k] = grid[i][j]
        printgrade(new_grid, new_n)