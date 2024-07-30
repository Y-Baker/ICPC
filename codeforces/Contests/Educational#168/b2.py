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
 
        def Opesite(row):
            if row == 0:
                return 1
            return 0
 
        for i in range(1, n-1):
            for row in range(2):
                if grid[row][i] == 'x':
                    continue
                if grid[Opesite(row)][i] == 'x':
                    continue
                if grid[row][i + 1] == 'x' or grid[row][i - 1] == 'x':
                    continue
                if grid[Opesite(row)][i + 1] == 'x' and grid[Opesite(row)][i - 1] == 'x':
                    can_3 += 1
 
        print(can_3)