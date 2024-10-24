#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    def compare(curr, new):
        if curr[0] / (curr[1] + curr[0]) == new[0] / (new[1] + new[0]):
            return True
        return False

    for _ in range(t):
        n = int(input())
        listt = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]
        sorted_mapp = sorted(listt, key=lambda x: x[0] / (x[1] + x[0]), reverse=True)
        # ties broken in ascending order of their assigned numbers
        res = []
        curr = [sorted_mapp[0]]
        for i in range(1, n):
            if compare(curr[0], sorted_mapp[i]):
                curr.append(sorted_mapp[i])
            else:
                res.append(curr)
                curr = [sorted_mapp[i]]
        res.append(curr)
        for i in res:
            i.sort(key=lambda x: x[0] + x[1])

        for i in res:
            for j in i:
                print(j[2], end=' ')
