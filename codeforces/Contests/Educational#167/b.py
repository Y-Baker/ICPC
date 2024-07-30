#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        a = input()
        b = input()

        def isSubsequence(root, s, i, j):
            if j == 0:
                return True
            if i == 0:
                return False

            if s[j-1] == root[i-1]:
                return isSubsequence(root, s, i-1, j-1)

            return isSubsequence(root, s, i-1, j)

        def getLargest(a, b):
            maxx = 0
            for i in range(len(b)):
                for j in range(i, len(b)):
                    ss = b[i:j+1]
                    if a == ss or isSubsequence(a, ss, len(a), len(ss)):
                        if len(ss) > maxx:
                            maxx = len(ss)
                    else:
                        break
                    
            if maxx == 0:
                print(len(a) + len(b))
            else:
                print(len(a) + len(b) - maxx)

        getLargest(a, b)
