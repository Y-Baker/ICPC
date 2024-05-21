#!/usr/bin/python3

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        class TreeNode:
            def __init__(self, val):
                self.val = val
                self.left = None
                self.right = None

        def genTree():
            root = TreeNode([])
            q = [root]
            for idx, i in enumerate(nums):
                q2 = []
                while q:
                    node = q.pop()
                    x = node.val.copy()
                    node.left = TreeNode(x.copy())
                    x.append(i)
                    node.right = TreeNode(x.copy())
                    q2.extend([node.left, node.right])
                if idx == len(nums) - 1:
                    return [node.val for node in q2]
                q = q2
            return root
        print(genTree())


s = Solution()
s.subsets([1, 2, 3])
