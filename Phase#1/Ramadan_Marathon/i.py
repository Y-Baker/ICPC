#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())
    directions = [(0, 1), (1, 0), (1, 1)]
    for _ in range(t):
        grid = [[*input()] for _ in range(4)]

        for r in range(4):
            for c in range(4):
                cnt = 0
                cnt2 = 0
                for d in directions:
                    n_r = r + d[0]
                    n_c = c + d[1]
                    if 0 <= n_r < 4 and 0 <= n_c < 4:
                        if grid[r][c] == grid[n_r][n_c]:
                            cnt += 1
                        else:
                            cnt2 += 1
                if cnt >= 2 or cnt2 == 3:
                    print('YES')
                    exit()
        print('NO')
