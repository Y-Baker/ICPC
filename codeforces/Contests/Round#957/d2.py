#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n, jumbs, swim = map(int, input().split())
        grid = 'L' + input().strip() + 'L'
        start = 0
        end = n + 1
        answerd = [False]

        def play(idx, swim):
            if idx == end:
                answerd[0] = True
                return
            if grid[idx] == 'L':
                flag = True
                for i in range(1, jumbs + 1):
                    if i + idx > n + 1:
                        break
                    if grid[idx + i] == 'L':
                        flag = False
                        play(idx + i, swim)
                if flag:
                    for i in range(jumbs, 0, -1):
                        if i + idx > n + 1:
                            break
                        if grid[idx + i] == 'W':
                            play(idx + i, swim)
                            return
                    answerd[0] ^= False
            elif grid[idx] == 'W':
                if swim > 0:
                    play(idx + 1, swim - 1)
                else:
                    answerd[0] ^= False

        play(start, swim)
        print('YES' if answerd[0] else 'NO')
