if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        size = int(input())
        s = set()
        line = list(map(int, input().split()))
        for i in line:
            s.add(int(i))

        print(len(s) - (size-len(s))%2)
