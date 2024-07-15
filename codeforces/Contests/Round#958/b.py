#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(input())
        l = [arr[0]]
        for ele in arr[1:]:
            if ele == '0' and l[-1] == '0':
                continue
            l.append(ele)
        print('YES' if l.count('1') > l.count('0') else 'NO')


