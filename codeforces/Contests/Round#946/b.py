#!/usr/bin/python3

def getR(s):
    sett = sorted(set(s))
    mapp = {ele: idx for idx, ele in enumerate(sett)}
    return sett, mapp

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        s = input()
        r, mapp = getR(s)
        size = len(r) - 1
        re = [r[size - mapp[c]] for c in s]
        print(''.join(re))
