#!/usr/bin/python3


# If the price of the orange was increased by x%. How many oranges can be bought for the amount that used to buy y oranges?
# so if x = 25 and y = 10 then the answer is 8

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        y, x = list(map(int, input().split()))

        y *= 100
        x += 100
        print(y // x)
