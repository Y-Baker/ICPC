#!/usr/bin/python3

from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = [0 for i in range(1001)]
        sett = set()
        for ele in arr:
            freq[ele] += 1
            sett.add(ele)

        s = set()
        for ele in sett:
            if freq[ele] in s:
                return False
            s.add(freq[ele])
        return True

s = Solution()
print(s.uniqueOccurrences([1,2,2,1,1,3]))
print(s.uniqueOccurrences([1,2]))
print(s.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
