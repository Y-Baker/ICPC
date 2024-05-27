 #!/usr/bin/python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        arr = [3, 5]
        curr = 7
        for i in range(n - 2):
            arr.append(curr)
            curr += 2

        print(*arr)
