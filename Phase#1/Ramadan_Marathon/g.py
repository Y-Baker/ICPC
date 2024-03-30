#!/usr/bin/python3

def solve(n, k, a):
    freq_l = {}
    freq_r = {}
    l, r = [], []
    l_idx = 0
    r_idx = 2 * n - 1

    while l_idx < n:
        if a[l_idx] not in freq_l:
            freq_l[a[l_idx]] = 0
        freq_l[a[l_idx]] += 1
        if freq_l.get(a[l_idx], 0) == 2:
            l.append(a[l_idx])
            l.append(a[l_idx])

        if a[r_idx] not in freq_r:
            freq_r[a[r_idx]] = 0
        freq_r[a[r_idx]] += 1
        if freq_r.get(a[r_idx], 0) == 2:
            r.append(a[r_idx])
            r.append(a[r_idx])

        l_idx += 1
        r_idx -= 1

    for i in range(n):
        if freq_l.get(a[i], 0) == 1:
            l.append(a[i])
            r.append(a[i])

    return l[:2*k], r[:2*k]


if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))

        l, r = solve(n, k, a)

        print(' '.join(map(str, l)))
        print(' '.join(map(str, r)))

