#!/usr/bin/python3

from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        def can(x):
            l = 0
            r = len(nums) - 1
            idx = -1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] < x:
                    idx = mid
                    l = mid + 1
                else:
                    r = mid - 1
            ans = len(nums) - idx - 1
            if ans == x:
                return 0
            elif ans > x:
                return 1
            return -1

        l = 1
        r = len(nums)
        ans = -1

        while l <= r:
            mid = l + (r - l) // 2
            re = can(mid)
            if re == 0:
                return mid
            elif re == 1:
                l = mid + 1
            else:
                r = mid -1
        return ans
