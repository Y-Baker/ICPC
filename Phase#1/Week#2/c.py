#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        pairs = {}
        p1 = {}
        p2 = {}
        count = 0
        for one in range(n):
            pair = input()
            count += p1.get(pair[0], 0) + p2.get(pair[1], 0) - 2 * pairs.get(pair, 0)
            if pair[0] not in p1:
                p1[pair[0]] = 1
            else:
                p1[pair[0]] += 1
            if pair[1] not in p2:
                p2[pair[1]] = 1
            else:
                p2[pair[1]] += 1
            if pair not in pairs:
                pairs[pair] = 1
            else:
                pairs[pair] += 1

        print(count)
