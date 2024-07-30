#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        movie1 = 0
        movie2 = 0
        pluss = 0
        minuss = 0

        for i in range(n):
            if a[i] == b[i]:
                if a[i] == 1:
                    pluss += 1
                elif a[i] == -1:
                    minuss += 1
                continue

            if a[i] == 1 and b[i] < 1:
                movie1 += 1
            elif a[i] == 0 and b[i] < 0:
                continue
            elif b[i] == 1 and a[i] < 1:
                movie2 += 1
            elif b[i] == 0 and a[i] < 0:
                continue

        while pluss > 0:
            if movie1 < movie2:
                movie1 += 1
            else:
                movie2 += 1
            pluss -= 1
        while minuss > 0:
            if movie1 < movie2:
                movie2 -= 1
            else:
                movie1 -= 1
            minuss -= 1

        print(min(movie1, movie2))


