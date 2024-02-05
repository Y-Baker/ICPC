#!/usr/bin/python3

if __name__ == '__main__':
    operations_nums, total = map(int, input().split())
    operations = [input() for _ in range(operations_nums)]
    failer = 0
    for operation in operations:
        sign, num = operation.split()
        num = int(num)
        if sign == '+':
                total += num
        else:
            if total >= num:
                    total -= num
            else:
                failer += 1

print(total, failer)
