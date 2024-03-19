#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        n, m = list(map(int, input().split()))
        grid = [list(map(int, input().split())) for _ in range(n)]

        def get_diagonal_sum(x, y):
            sum = 0
            for i in range(n):
                for j in range(m):
                    if abs(x - i) == abs(y - j):
                        sum += grid[i][j]
            return sum

        max_sum = 0
        for i in range(n):
            for j in range(m):
                cur_sum = grid[i][j]
                dimensions = [(i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)]
                should_end = [(0, 0), (0, m - 1), (n - 1, 0), (n - 1, m - 1)]
                operations = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

                for (x, y), end in zip(dimensions, should_end):
                    while 0 <= x < n and 0 <= y < m:
                        cur_sum += grid[x][y]
                        x += operations[0][0]
                        y += operations[0][1]
                    operations.pop(0)
                max_sum = max(max_sum, cur_sum)

        print(max_sum)
