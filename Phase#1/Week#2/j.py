#!/usr/bin/python3
import re
if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        enpassword = input()
        patern = '.' * 10
        arr = re.findall(patern, enpassword)
        structure = []
        re = ''
        for _ in range(10):
            structure.append(input())

        for elm in arr:
            for idx, one in enumerate(structure):
                if one == elm:
                    re = re + str(idx)
                    break           

        print(re)
