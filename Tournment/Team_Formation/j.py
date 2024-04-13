#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        for idx in range(n - 1):
            if arr[idx] & 1:
                try:
                    value = min(filter(lambda x: x % 2 != 0, arr[idx:]))
                except ValueError:
                    continue
                v_idx = arr[idx:].index(value) + idx
                arr[v_idx] = arr[idx]
                arr[idx] = value

            else:
                try:
                    value = min(filter(lambda x: x % 2 == 0, arr[idx:]))
                except ValueError:
                    continue
                v_idx = arr[idx:].index(value) + idx
                arr[v_idx] = arr[idx]
                arr[idx] = value

        print('YES' if arr == sorted(arr) else 'NO')
