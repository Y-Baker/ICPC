#!/usr/bin/python3

from typing import List
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions) - 1
        res = [0 for _ in range(len(spells))]
        for idx, spell in enumerate(spells):
            l = 0
            r = n
            re = n
            while l <= r:
                mid = (l+r) >> 1
                check = potions[mid] * spell
                if check >= success:
                    if mid == 0 or potions[mid - 1] * spell < success:
                        re = n - mid + 1
                        break
                    else:
                        r = mid
                else:
                    l = mid + 1
            if l == n + 1:
                re = 0
            res[idx] = re
        return res

s = Solution()
print(s.successfulPairs([5, 1, 3], [1,2,3,4,5], 7))  # [4, 0, 3]