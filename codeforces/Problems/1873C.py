#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    def getop(i, j):
        if i < 5 and j < 5:
            return (-1, -1)
        elif i < 5 and j >= 5:
            return (-1, 1)
        elif i >= 5 and j < 5:
            return (1, -1)
        else:
            return (1, 1)

    for _ in range(t):
        grid = []
        for i in range(10):
            grid.append(list(input()))

        cnt = 0
        for i in range(10):
            for j in range(10):
                if grid[i][j] == 'X':
                    op = getop(i, j)
                    ii = i
                    jj = j
                    while ii >= 0 and ii < 10 and jj >= 0 and jj < 10:
                        cnt += 1
                        ii += op[0]
                        jj += op[1]
        print(cnt)
