#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        x, y = map(int, input().split())
        res = [[0, ''] for _ in range(4)]
        flags = [False, False, False, False]
        stars = [(3, 3), (3, 10), (10, 3), (10, 10)]
        points = [[x, y], [x, y], [x, y], [x, y]]
        blocks = [(6, 6), (6, 7), (7, 6), (7, 7), (9, 2), (9, 3), (10, 2), (9, 10), (9, 11), (10, 11)]

        def go(point, star, i):
            if point[0] == star[0] and point[1] == star[1]:
                flags[i] = True
                return
            if point[0] < star[0] and (point[0] + 1, point[1]) not in blocks:
                point[0] += 1
                res[i][1] += 'D'
            elif point[0] > star[0] and (point[0] - 1, point[1]) not in blocks:
                point[0] -= 1
                res[i][1] += 'U'
            elif point[1] < star[1] and (point[0], point[1] + 1) not in blocks:
                point[1] += 1
                res[i][1] += 'R'
            elif point[1] > star[1] and (point[0], point[1] - 1) not in blocks:
                point[1] -= 1
                res[i][1] += 'L'

            
            res[i][0] += 1

        while flags[0] == False and flags[1] == False and flags[2] == False and flags[3] == False:
        # while not all(flags):
            for i in range(4):
                go(points[i], stars[i], i)

        idx = flags.index(True)
        print(len(res[idx][1]))
        print(res[idx][1])

