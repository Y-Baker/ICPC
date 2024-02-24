#!/usr/bin/python3

if __name__ == "__main__":
    t = 1
    # t = int(input())

    for _ in range(t):
        num_candy, queries = list(map(int, input().split(' ')))
        candies = list(map(int, input().split(' ')))
        candies.sort(reverse=True)
        for candy in range(1, num_candy):
            candies[candy] += candies[candy - 1]

        for one in range(queries):
            count = 0
            flag = True
            query = int(input())
            if query > candies[-1]:
                print(-1)
                continue
            for idx, candy in enumerate(candies):
                if candy >= query:
                    print(idx + 1)
                    break
