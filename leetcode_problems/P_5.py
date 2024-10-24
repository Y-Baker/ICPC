#!/usr/bin/python3

class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxx = 0
        re = ''
        def check(idx, flag):
            sub = ''
            if flag:
                if (idx == 0 or idx == len(s) - 1):
                    return s[idx]
                l = idx - 1
                r = idx + 1
                sub = s[idx]
            else:
                if idx == len(s) - 1:
                    return ''
                l = idx
                r = idx + 1

            while s[l] == s[r]:
                sub = s[l] + sub + s[l]
                l -= 1
                r += 1
                if r > len(s) - 1 or l < 0:
                    break
    
            return sub

        for c in range(len(s)):
            curr = check(c, flag=True)
            # print(s[c], curr)
            if maxx < len(curr):
                maxx = len(curr)
                re = curr
            curr = check(c, flag=False)
            # print(s[c], curr)
            if maxx < len(curr):
                maxx = len(curr)
                re = curr
        return re

s = Solution()
print(s.longestPalindrome("babad")) # bab
print(s.longestPalindrome("cbbd")) # bb
print(s.longestPalindrome("a")) # a
print(s.longestPalindrome("bb")) 