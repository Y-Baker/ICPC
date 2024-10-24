#!/usr/bin/python3

from collections import defaultdict
if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        mapp = defaultdict(int)

        def all_factors(n):
            factors = set()
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    if i == n // i:
                        mapp[i] += 1
                    else:
                        mapp[i] += 1
                        mapp[n // i] += 1

        for i in arr:
            all_factors(i)
        # print(mapp)
        mapp = sorted(mapp.items(), key=lambda x: x[0], reverse=True)
        # print(mapp)
        needed = n - k
        for k, v in mapp:
            if v >= needed:
                print(k)
                break
