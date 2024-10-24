#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        x = input()
        curr = 1
        flag = False
        for i in range(len(x)):
            if x[i] == '0':
                if i != 0 and x[i - 1] == '1':
                    curr += 1
                if i + 1 < len(x) and x[i + 1] == '1':
                    curr += 1
                    flag = True
        if flag:
            curr -= 1
        print(curr)


# 11 | 0 | 1 | 0
# 0110 -> 0 | 1 1 | 0