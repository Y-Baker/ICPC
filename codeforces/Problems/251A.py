#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

        
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))

        def can(x):
            
        l = 0
        r = n
        ans = 0
        while l <= r:
            mid = l + (r - l) // 2
            if can(mid):
                ans = max(ans, mid)
                l = mid + 1
            else:
                r = mid - 1

        print(ans)

# 4 -> 1 10 20 - 1 10 30 - 1 20 30 - 10 20 30
# 5 -> 1 10 20 - 1 10 30 - 1 10 50 - 1 20 