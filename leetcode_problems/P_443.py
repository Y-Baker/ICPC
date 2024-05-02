#!/usr/bin/python3

from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 1
        ptr = 1
        cnt = 0
        start = chars[0]
        while ptr < len(chars):
            if chars[ptr] == start:
                cnt += 1
            else:
                if cnt > 0:
                    toAdd = list(str(cnt + 1))
                    for c in toAdd:
                        chars[write] = c
                        write += 1
                    cnt = 0
                start = chars[ptr]
                chars[write] = start
                write += 1
            ptr += 1
        if cnt > 0:
            toAdd = list(str(cnt + 1))
            for c in toAdd:
                chars[write] = c
                write += 1
        chars[:] = chars[:write]

s = Solution()
chars = ["a","a","a","b","b","a","a"]
s.compress(chars)
print(chars) # ["a","2","b","2","c","3"]
s.compress(["a"]) # ["a"]
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
s.compress(chars)
print(chars) # ["a","b","1","2"]