#!/usr/bin/python3

def play_iterative(n, jumbs, swim, grid):
    stack = [(0, swim)]
    end = n + 1

    while stack:
        idx, swim = stack.pop()
        if idx == end:
            return True
        if grid[idx] == 'L':
            flag = True
            for i in range(1, jumbs + 1):
                if i + idx > n + 1:
                    break
                if grid[idx + i] == 'L':
                    flag = False
                    stack.append((idx + i, swim))
            if flag:
                for i in range(jumbs, 0, -1):
                    if i + idx > n + 1:
                        break
                    if grid[idx + i] == 'W':
                        stack.append((idx + i, swim))
                        break
        elif grid[idx] == 'W':
            if swim > 0:
                stack.append((idx + 1, swim - 1))

    return False

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n, jumbs, swim = map(int, input().split())
        grid = 'L' + input().strip() + 'L'
        if play_iterative(n, jumbs, swim, grid):
            print('YES')
        else:
            print('NO')
