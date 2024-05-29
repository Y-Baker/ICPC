#!/usr/bin/python3

class Solution:
    def numSteps(self, s: str) -> int:
        s = list(s)

        cnt = 0
        while len(s) > 1:
            if s[-1] == '1':
                i = len(s) - 1
                while i >= 0 and s[i] == '1':
                    s[i] = '0'
                    i -= 1
                if i == -1:
                    s.insert(0, '1')
                else:
                    s[i] = '1'
            elif s[-1] == '0':
                s.pop()
            cnt += 1
        return cnt

if __name__ == '__main__':
    s = Solution()
    print(s.numSteps("1101"))
    print(s.numSteps("10"))
