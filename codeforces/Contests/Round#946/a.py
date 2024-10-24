#!/usr/bin/python3
import math
if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        x, y = map(int, input().split())
        can_x = 0
        can_y = 0
        cnt = 0
        need = math.ceil(y / 2)
        

        while need > 0:
            need -= 1
            cnt += 1
            can_y += 2
            can_x += 7

        can_y -= y
        if can_y > 0:
            can_x += 4 * can_y
            can_y = 0

        if can_x >= x or x == 0:
            print(cnt)
        else:
            print(cnt + math.ceil((x - can_x) / 15))

