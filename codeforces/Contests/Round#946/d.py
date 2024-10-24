#!/usr/bin/python3

def checkCloser(x1, y1, targetX, targetY, c):
    if x1 < targetX and c == 'E':
        return True
    if x1 > targetX and c == 'W':
        return True
    if y1 < targetY and c == 'N':
        return True
    if y1 > targetY and c == 'S':
        return True
    return False

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        s = input()
        op = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}

        def Findmax():
            sett = set()
            maxX, maxY = 0, 0
            for c in s:
                sett.add(c)
                x, y = op[c]
                maxX += x
                maxY += y
            if len(sett) == 1 and n & 1:
                return None
            return maxX, maxY

        if not Findmax():
            print("NO")
            continue
        x, y = Findmax()
        if x & 1 or y & 1:
            print("NO")
            continue
        targetX, targetY = x // 2, y // 2
        re = ''
        flag = False

        x1, y1 = 0, 0
        used = [False] * n
        if targetX == 0 and targetY == 0:
            flags = [False, False, False, False]
            idxs = [-1, -1, -1, -1]
            for idx, c in enumerate(s):
                if c == 'N':
                    flags[0] = True
                    idxs[0] = idx
                if c == 'S':
                    flags[1] = True
                    idxs[1] = idx
                if c == 'E':
                    flags[2] = True
                    idxs[2] = idx
                if c == 'W':
                    flags[3] = True
                    idxs[3] = idx
                if flags[0] and flags[1] and flags[2] and flags[3]:
                    break
            if flags[0] and flags[1]:
                idx1 = min(idxs[0], idxs[1])
                idx2 = max(idxs[0], idxs[1])
                re = 'R' * idx1 + 'H' + 'R' * (idx2 - idx1 - 1) + 'H' + 'R' * (n - idx2 - 1)
                if n == 2:
                    print("NO")
                else:
                    print(re)
                continue
            elif flags[2] and flags[3]:
                idx1 = min(idxs[2], idxs[3])
                idx2 = max(idxs[2], idxs[3])
                re = 'R' * idx1 + 'H' + 'R' * (idx2 - idx1 - 1) + 'H' + 'R' * (n - idx2 - 1)
                if n == 2:
                    print("NO")
                else:
                    print(re)
                continue
            else:
                print("NO")
                continue

        for idx, c in enumerate(s):
            if flag:
                re += 'R' * (n - idx)
                break
            if checkCloser(x1, y1, targetX, targetY, c):
                re += 'H'
                x1 += op[c][0]
                y1 += op[c][1]
            else:
                re += 'R'
            if x1 == targetX and y1 == targetY:
                flag = True
        if len(set(re)) == 1:
            print("NO")
        else:
            print(re)
