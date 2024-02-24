#!/usr/bin/python3

def less_cost(groups, sentense):
    cost = 0
    for one in sentense:
        cost += groups[one]
    return cost

if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n_words, n_groups, n_sentence = list(map(int, input().split(" ")))
        words = input().split(" ")
        costs = list(map(int, input().split(" ")))
        groups = {words[i]: costs[i] for i in range(n_words)}
        for _ in range(n_groups):
            group = list(map(int, input().split(" ")))
            minn = float("inf")
            for i in range(1, len(group)):
                minn = min(minn, costs[group[i] - 1])
            for i in range(1, len(group)):
                groups[words[group[i] - 1]] = minn
        sentence = input().split(" ")
        print(less_cost(groups, sentence))
