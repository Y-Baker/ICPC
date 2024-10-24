#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        grid = []
        for _ in range(5):
            grid.append(list(map(int, input().split())))
        one = None
        for i in range(5):
            for j in range(5):
                if grid[i][j] == 1:
                    one = (i, j)
                    break
            if one:
                break
        print(abs(one[0] - 2) + abs(one[1] - 2))
