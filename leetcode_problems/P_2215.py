#!/usr/bin/python3

from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set()
        for i in set(nums2):
            if i in s1:
                s1.remove(i)
            else:
                s2.add(i)
        return [list(s1), list(s2)]

s = Solution()
print(s.findDifference([1,2,3], [2,4,6]))
print(s.findDifference([1,2,3,3], [1,1,2,2]))
