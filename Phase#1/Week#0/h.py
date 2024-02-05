if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        size = int(input())
        line = list(map(int, input().split()))
        eated = list(map(lambda x: x-min(line), line))
        print(sum(eated))
