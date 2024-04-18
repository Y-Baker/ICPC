from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def solve(row, col):
            from collections import deque
            dimensions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            q = deque([(row, col)])
            seen = set([(row, col)])
            re = 0

            while q:
                r, c = q.popleft()
                for one in dimensions:
                    new_row = r + one[0]
                    new_col = c + one[1]
                    if new_row not in range(0, len(grid)) or new_col not in range(0, len(grid[0])):
                        re += 1
                        continue
                    if grid[new_row][new_col] == 0:
                        re += 1
                    else:
                        if (new_row, new_col) not in seen:
                            seen.add((new_row, new_col))
                            q.append((new_row, new_col))
            return re

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return solve(row, col)

s = Solution()
print(s.islandPerimeter([[1,1],[1,1]])) # 8