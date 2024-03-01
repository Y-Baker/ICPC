#!/usr/bin/python3

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    mapp = {}
    for _ in range(n):
        level, yen = list(map(int, input().split()))
        if level not in mapp:
            mapp[level] = yen
        else:
            mapp[level] += yen
    
    sorted_mapp = sorted(mapp.items(), key=lambda x: x[0])


    for level, yen in sorted_mapp:
        if k >= level:
            k += yen
        else:
            break

    print(k)


