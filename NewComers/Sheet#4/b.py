#!/usr/bin/python3

if __name__ == '__main__':
    # t = 1
    t = int(input())

    for _ in range(t):
        s = input()
        freq = [0 for i in range(3)]

        for c in s:
            freq[ord(c) - ord('A')] += 1

        if freq[1] == freq[0] + freq[2]:
            print("YES")
        else:
            print("NO")
