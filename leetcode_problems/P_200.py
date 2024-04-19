#!/usr/bin/python3
from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited = set()

        counter = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(row_root, col_root):
            q = deque()
            directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

            q.append((row_root, col_root))
            visited.add((row_root, col_root))

            while len(q) > 0:
                row, col = q.popleft()

                for one in directions:
                    r = row + one[0]
                    c = col + one[1]

                    if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0:
                        continue
                    if grid[r][c] == '1' and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    bfs(row, col)
                    counter += 1
            
        return counter
