#!/usr/bin/python3

if __name__ == '__main__':
    num = str(input())
    times = 0
    while (len(num) > 1):
        times += 1
        new_num = 0
        for digit in num:
            new_num += int(digit)
        num = str(new_num)

    print(times)
