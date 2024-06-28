#!/usr/bin/python3

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def genTree(nums):
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


if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        subsets = genTree(arr)
        cashe = {}
        ans = 0
        for subset in subsets:
            if not subset:
                continue
            curr = subset[0]
            for num in subset[1:]:
                one = min(curr, num)
                two = max(curr, num)
                if (one, two) in cashe:
                    curr = cashe[(one, two)]
                    continue

                curr = one | two
                cashe[(one, two)] = curr

            ans += curr
        print(ans)
