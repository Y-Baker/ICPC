from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        from collections import deque
        q = deque([(root, 2)])
        seen = set()
    
        while q:
            node, dp = q.popleft()
            if dp == depth:
                new_l = TreeNode(val, node.left)
                new_r = TreeNode(val, None, node.right)
                node.left = new_l
                node.right = new_r
            elif dp < depth:
                seen.add(node)
                if node.left and node.left not in seen:
                    q.append((node.left, dp+1))
                if node.right and node.right not in seen:
                    q.append((node.right, dp+1))
        return root
            

tree = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, TreeNode(5)))
s = Solution()
s.addOneRow(tree, 1, 3)