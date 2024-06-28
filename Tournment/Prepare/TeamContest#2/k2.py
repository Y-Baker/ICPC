#!/usr/bin/python3

def subsets(nums):
    res = []
    backtrack(res, [], nums, 0)
    return res

def backtrack(res, temp, nums, start):
    res.append(temp[:]) 
    for i in range(start, len(nums)):
        temp.append(nums[i])
        backtrack(res, temp, nums, i + 1)
        temp.pop()


if __name__ == '__main__':
    t = 1
    # t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        subsets = subsets(arr)
        cashe = {}
        ans = 0
        for subset in subsets:
            if not subset:
                continue
            curr = subset[0]
            for num in subset[1:]:
                one = min(curr, num)
                two = max(curr, num)
                if (one, two) in cashe:
                    curr = cashe[(one, two)]
                    continue

                curr = one | two
                cashe[(one, two)] = curr

            ans += curr
        print(ans)
