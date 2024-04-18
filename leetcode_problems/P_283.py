class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = 1
        while p1 < len(nums):
            if p2 < p1:
                p2 = p1 + 1
            while p2 < len(nums) and nums[p2] == 0:
                p2 += 1
            if nums[p1] == 0 and p2 < len(nums) and nums[p2] != 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1


s = Solution()
arr = [4,2,4,0,0,3,0,5,1,0]
s.moveZeroes(arr)
print(arr)