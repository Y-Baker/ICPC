#!/usr/bin/python3

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        freq = {'odd': 0, 'even': 0}
        for i in range(n):
            if arr[i] % 2 == 0:
                freq['even'] += 1
            else:
                freq['odd'] += 1

        arr.sort()
        remaing = abs(freq['odd'] - freq['even'])

        if remaing <= 1:
            print(0)
        else:
            if freq['odd'] > freq['even']:
                arr = list(filter(lambda x: x % 2 == 1, arr))
                print(sum(arr[:remaing - 1]))
            else:
                arr = list(filter(lambda x: x % 2 == 0, arr))
                print(sum(arr[:remaing - 1]))
