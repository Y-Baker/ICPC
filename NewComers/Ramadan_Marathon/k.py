#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        d1, d2, d3 = map(int, input().split())
        target = [False, False]

        curr = 0
        summ = 0
        while not all(target):
            if curr == 0:
                if d1 < d2:
                    summ += d1
                    curr = 1
                    target[0] = True
                else:
                    summ += d2
                    curr = 2
                    target[1] = True
            elif curr == 1:
                if d3 < d1 + d2:
                    summ += d3
                    curr = 2
                    target[1] = True
                else:
                    summ += d1 + d2
                    curr = 2
                    target[1] = True
            else:
                if d3 < d1 + d2:
                    summ += d3
                    curr = 1
                    target[0] = True
                else:
                    summ += d1 + d2
                    curr = 1
                    target[0] = True
        
        if curr == 1:
            summ += min(d1, d2 + d3)
        else:
            summ += min(d2, d1 + d3)

        print(summ)


