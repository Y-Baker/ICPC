from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        from collections import deque

        minn = None
        q = deque([(root, '')])
        seen = set()

        while q:
            node, x = q.popleft()
            x = x + chr(node.val + 97)
            seen.add(node)
            if not node.left and not node.right:
                if not minn:
                    minn = x[::-1]
                else:
                    minn = min(minn, x[::-1])
            if node.left and node.left not in seen:
                q.append((node.left, x))
            if node.right and node.right not in seen:
                q.append((node.right, x))

        return minn     

tree = TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(3), TreeNode(4)))
s = Solution()
print(s.smallestFromLeaf(tree))
