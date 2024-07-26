#!/usr/bin/python3

from collections import defaultdict
if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n, q = map(int, input().split())
        one = input()
        two = input()
        mapp = defaultdict(list)

        for i in range(n):
            mapp[two[i]].append(i)

        def binarysearch(arr, lowerRange, upperRange):
            l = 0
            r = len(arr) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] < lowerRange:
                    l = mid + 1
                elif arr[mid] > upperRange:
                    r = mid - 1
                else:
                    return mid
            return -1

        for i in range(q):
            i, j = map(int, input().split())
            i -= 1
            j -= 1
            cnt = 0

            # deep copy
            maptmp = defaultdict(list)
            for k in mapp:
                maptmp[k] = mapp[k].copy()

            for k in range(i, j+1):
                if maptmp[one[k]]:
                    idx = binarysearch(maptmp[one[k]], i, j)
                    if idx == -1:
                        cnt += 1
                    else:
                        maptmp[one[k]].pop(idx)
                else:
                    cnt += 1
            print(cnt)