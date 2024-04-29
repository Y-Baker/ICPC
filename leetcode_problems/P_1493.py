#!/usr/bin/python3

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        def trywindow(start):
            re = 0
            flag = True
            j = start
            while (j < n and (nums[j] != 0 or flag)):
                if nums[j] == 0:
                    flag = False
                else:
                    re += 1
                j += 1
            if start == 0 and flag:
                re -= 1
            return re


        maxx = 0
        for i in range(n):
            if nums[i] == 1 and (i == 0 or nums[i - 1] == 0):
                maxx = max(maxx, trywindow(i))

        return maxx

