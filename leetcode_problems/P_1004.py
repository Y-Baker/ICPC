#!/usr/bin/python3

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        def tryWindow(start, k):
            cnt = 0
            curr = start
            while curr < len(nums):
                if nums[curr] == 0:
                    if k <= 0:
                        break
                    k -= 1
                curr += 1                    
                cnt += 1
            start -= 1
            if k > 0:
                while (start >= 0 and k > 0 and nums[start] == 0):
                    cnt += 1
                    k -= 1
                    start -= 1
            return cnt

        maxx = -1
        for idx in range(len(nums)):
            if nums[idx] == 1 and (idx == 0 or nums[idx - 1] == 0):
                maxx = max(maxx, tryWindow(idx, k))

        if maxx == -1:
            return min(k, len(nums))
        return maxx


s = Solution()
print(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)) # 6
print(s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)) # 10

