from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 5 4 2 3 -> 24 30 60 40
        # 5 20 40 120
        # 120 24 6 3

        n = len(nums)
        perfix = [0 for _ in range(n)]
        suffix = [1 for _ in range(n)]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(n):
            suffix[i] *= nums[i]
            if i == 0:
                perfix[i] = nums[i]
            else:
                perfix[i] = perfix[i - 1] * nums[i]

        nums[0] = suffix[1]
        for i in range(1, n - 1):
            nums[i] = suffix[i + 1] * perfix[i - 1]
        nums[n - 1] = perfix[-2]

        return nums
