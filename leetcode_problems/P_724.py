#!/usr/bin/python3

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # 1 8 11 17 22 28
        # perfix sum
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        for i in range(len(nums)):
            left = 0 if i == 0 else nums[i-1]
            right = nums[-1] - nums[i]
            if left == right:
                return i
        return -1
