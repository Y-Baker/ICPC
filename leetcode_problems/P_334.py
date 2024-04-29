#!/usr/bin/python3

from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        first = second = float('inf')
        for ele in nums:
            if ele < first:
                first = ele
            elif ele < second:
                second = ele
            else:
                return True
        return False

s = Solution()
print(s.increasingTriplet([1,2,3,4,5])) # True
print(s.increasingTriplet([5,4,3,2,1])) # False
print(s.increasingTriplet([2,1,5,0,4,6])) # True
print(s.increasingTriplet([0,4,2,1,0,-1,-3])) # False