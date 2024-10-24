#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    t = int(input())

    for _ in range(t):
        str_n = input()
        n = int(str_n)
        sum_first = sum(map(int, str_n[:3]))
        sum_last = sum(map(int, str_n[3:]))
        if sum_first == sum_last == 16:
            print("YES")
            continue
        if sum_first != 16:
            print("NO")
            continue
        last_three = n % 1000
        start = 200 * (last_three // 200)
        end = start + 200
        # start = 200
        # end = 
        print(start, end, sep='------>')
        valid = False
        while start < end:
            if sum(map(int, str(start))) == 16:
                print(start)
                valid = True
                break
            start += 1
        print("YES" if valid else "NO")
