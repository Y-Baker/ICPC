#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n = int(input())
        count = 0
        arr = list(map(int, input().split(" ")))

        map = {}
        for i in arr:
            if i not in map:
                map[i] = 0
            map[i] += 1

        for elm in arr:
            flag = False
            for i in range(32):
                temp = 1 << i
                to_find = temp - elm
                if to_find in map:
                    if map.get(to_find, 0) > 1 or (map.get(to_find, 0) == 1 and to_find != elm):
                        flag = True
                        break
            if not flag:
                count += 1

        print(count)
