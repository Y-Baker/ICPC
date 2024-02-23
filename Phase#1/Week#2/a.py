if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        maxx = 0
        size = int(input())
        s = input()

        dist = []
        s1 = set()
        s2 = set()
        for idx in range(len(s)):
            s1.add(s[idx])
            dist.append(len(s1))

        for i in range(size - 1, 0, -1):
            s2.add(s[i])
            maxx = max(maxx, dist[i - 1] + len(s2))
        
        print(maxx)

