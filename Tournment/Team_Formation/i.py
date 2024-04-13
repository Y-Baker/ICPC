#!/usr/bin/python3

# 1 -> -1
# 2 -> 2
# 3 -> 3
# 4 -> 4
# 5 -> 5
# 6-> 5 1
# 7 -> 4 2 1
# 8 -> 5 3
# 9 -> 5 4
# 10 -> 4 6
# 11 -> 5 6
# 12 -> 4 6 2
# 13 -> 5 6 2
# 14 -> 5 6 3
# 15 -> 5 6 4
# 16 -> 5 6 5
# 17 -> 5 6 5 1
# 18 -> 5 4 6 3
# 19 -> 5 6 5 3
# 20 -> 5 6 5 4
# 21 -> 5 6 4 6
# 22 -> 5 6 5 6

if __name__ == '__main__':
    # t = 1
    t = int(input())
    ans = [0, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4]

    for _ in range(t):
        n = int(input())
        re = 0
        if n == 1:
            print(-1)
        elif n < 22:
            print(ans[n])
        elif n > 11:
            remain = n % 11
            devide = n // 11
            re += devide * 2
            
            if remain == 7:  # 29 -> 5 6 5 4 5 3 Not 5 6 5 6 4 2 1
                re += 2
            else:
                re += ans[remain]

            print(re)
