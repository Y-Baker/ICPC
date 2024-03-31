#!/usr/bin/python3
class CirleList:
    def __init__(self, l):
        self.l = l
        self.curr = 0
        self.size = len(l)

    def next(self):
        self.curr = (self.curr + 1) % self.size
        return self.l[self.curr]

    def prev(self):
        self.curr = (self.curr - 1) % self.size
        return self.l[self.curr]

    def get(self):
        return self.l[self.curr]

def solve():
    n = int(input())

    if n & 1 == 0:
        print("NO")
        return

    l = [1]
    r = []

    for i in range(4, 2 * n + 1, 4):
        l.append(i)
        if i + 1 <= 2 * n:
            l.append(i + 1)

    for i in range(2, 2 * n + 1, 4):
        r.append(i)
        if i + 1 <= 2 * n:
            r.append(i + 1)

    print("YES")
    print(" ".join(map(str, l+r)))

        
    
if __name__ == '__main__':
    solve()

