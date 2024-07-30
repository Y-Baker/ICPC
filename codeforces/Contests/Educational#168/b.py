#!/usr/bin/python3
 
if __name__ == '__main__':
    t = 1
    t = int(input())
 
    for _ in range(t):
        n = int(input())
        grid = [[] for _ in range(2)]
        for i in range(2):
            grid[i] = list(input().strip())
        can_3 = 0
 
        if set(grid[0]) == {'x'} and set(grid[1]) == {'x'}:
            print(0)
            continue

        prefixWater = [0] * n
        cnt = 0
        for i in range(n):
            if grid[0][i] == '.':
                cnt += 1
            if grid[1][i] == '.':
                cnt += 1
            prefixWater[i] = cnt

        totalWater = cnt
        for i in range(1, n-1):
            if (grid[0][i] == '.' and grid[1][i] == '.'):
                l = prefixWater[i-1]
                r = totalWater - l - 2
                if l > 0 and r > 0:
                    if grid[1][i-1] == 'x' and grid[1][i+1] == 'x':
                        can_3 += 1
                    if grid[0][i-1] == 'x' and grid[0][i+1] == 'x':
                        can_3 += 1
        
        print(can_3)

