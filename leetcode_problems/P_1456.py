#!/usr/bin/python3

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        l = 0
        r = k - 1
        cnt = 0

        for i in range(k): # O(K)
            if s[i] in vowels:
                cnt += 1

        maxx = cnt
        n = len(s)
        while r < n - 1:
            if s[l] in vowels:
                cnt -= 1
            l += 1
            r += 1
            if s[r] in vowels:
                cnt += 1
            maxx = max(maxx, cnt)
        return maxx

s = Solution()
print(s.maxVowels("abciiidef", 3))
