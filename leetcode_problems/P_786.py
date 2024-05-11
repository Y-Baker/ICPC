#!/usr/bin/python3

from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        l = 0
        r = len(arr) - 1
        k -= 1
        while k:
            if arr[l+1] / arr[len(arr) - 1] < arr[0] / arr[r - 1]:
                l += 1
                r = len(arr) - 1
            else:
                l = 0
                r -= 1
            k -= 1
        return [arr[l], arr[r]]

    def _kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        ans = []
        for i in range(len(arr) - 1):
            for j in range(i+1, len(arr)):
                ans.append((arr[i], arr[j]))
        ans.sort(key=lambda x : x[0] / x[1])
        return ans

    # def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
    #     ans = []
    #     for i in range(len(arr) - 1):
    #         for j in range(i+1, len(arr)):
    #             ans.append((arr[i], arr[j]))
    #     ans.sort(key=lambda x : x[0] / x[1])
    #     return ans[k-1]

s = Solution()
print(s.kthSmallestPrimeFraction([1, 2, 3, 5], 3)) # [2, 5]
print(s.kthSmallestPrimeFraction([1, 7], 1)) # [1, 7]
print(s._kthSmallestPrimeFraction([1, 13, 17, 59], 6)) # [13, 17]
print(s.kthSmallestPrimeFraction([1,13,17,59], 6)) # [13, 17]