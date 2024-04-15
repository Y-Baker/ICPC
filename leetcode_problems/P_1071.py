class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def solve(s, t):
            tt = t
            while len(t) > 0:
                x = ''.join(s.split(t))
                x2 = ''.join(tt.split(t))

                if x == '' and x2 == '':
                    return t
                t = t[:-1]
            return t
        return (solve(str1, str2) if len(str1) > len(str2) else solve(str2, str1))
