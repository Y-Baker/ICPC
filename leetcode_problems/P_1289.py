#!/usr/bin/python3

from typing import List
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cashe = {}

        def helper(row, col):
            if row == n - 1:
                return 0
            if (row, col) in cashe:
                return cashe[(row, col)]

            row += 1
            minn = 100000
            for i in range(n):
                if i != col:
                    val = grid[row][i] + helper(row, i)
                    cashe[(row, i)] = val
                    minn = min(minn, val)
            return minn

        re = 100000
        for start in range(n):
            re = min(re, grid[0][start] + helper(0, start))

        return re

sol = Solution()
print(sol.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])) # 13
print(sol.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]])) # 13