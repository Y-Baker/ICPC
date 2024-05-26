#!/usr/bin/python3

class Solution:
    def arrangeCoins(self, n: int) -> int:

        def can(x):
            need = x * (x+1) / 2
            if n >= need:
                return True
            return False

        l = 0
        r = n
        while l <= r:
            mid = l + (r-l)//2
            if can(mid):
                l = mid + 1
            else:
                r = mid - 1
        if can(mid):
            return mid
        return mid - 1


s = Solution()
print(s.arrangeCoins(5))
print(s.arrangeCoins(8))
print(s.arrangeCoins(1))