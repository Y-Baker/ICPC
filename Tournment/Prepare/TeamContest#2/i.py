#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())
    class TreeNode():
        def __init__(self, val):
            self.val = val
            self.childs = []
            self.parent = None

    for _ in range(t):
        n = int(input())
        res = [0] * (n + 1)
        x = input()
        if x == '':
            print(*res)
            continue
        root = TreeNode(int(x[0]))
        for c in x[1:]:
            if c == '(':
                continue
            if c == ')':
                root = root.parent
                continue
            node = TreeNode(int(c))
            node.parent = root
            root.childs.append(node)
            root = node
            res[int(c)] = node.parent.val
        print(*res[1:])
