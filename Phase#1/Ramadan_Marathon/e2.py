#!/usr/bin/python3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())
        grid = [list(map(int, input().split())) for _ in range(n)]

        # Initialize diagonal sums lists
        diag1 = [0] * (n + m - 1)
        diag2 = [0] * (n + m - 1)

        # Calculate diagonal sums
        for i in range(n):
            for j in range(m):
                diag1[i + j] += grid[i][j]
                diag2[i - j + m - 1] += grid[i][j]

        # Find maximum sum among diagonals
        max_sum = max(max(diag1), max(diag2))
        print(max_sum)
