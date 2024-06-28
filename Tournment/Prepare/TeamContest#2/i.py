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
        start = 0
        if '(' not in x:
            print(0)
            continue
        while x[start] != '(':
            start += 1

        root = TreeNode(int(x[:start]))
        current = root
        curr = ''
        for idx, c in enumerate(x[start:]):
            if c == '(':
                continue
            if c == ')':
                current = current.parent
                continue
            curr += c
            if x[idx + start + 1] not in ['(', ')']:
                continue
            num = int(curr)
            curr = ''
            node = TreeNode(num)
            node.parent = current
            current.childs.append(node)
            current = node
            res[num] = node.parent.val
        print(*res[1:])
