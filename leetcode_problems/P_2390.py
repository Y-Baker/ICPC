#!/usr/bin/python3

def calTime(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        res = func(*args, **kwargs)
        print(f"Time taken to execute {func.__name__}: {time.time() - start}")
        return res
    return wrapper


class Solution:
    @calTime
    def removeStars(self, s: str) -> str:
        s = list(s)
        cnt = 0
        i = len(s) - 1
        while i >= 0:
            if s[i] == '*':
                cnt += 1
                s.pop(i)
            else:
                if cnt > 0:
                    s.pop(i)
                    cnt -= 1
            i -= 1

        return ''.join(s)

    @calTime
    def removeStars1(self, s: str) -> str: # Using stack Faster
        stack = []
        for c in s:
            if c == '*':
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)

s = Solution()
print(s.removeStars("leet**cod*e"))
print(s.removeStars1("leet**cod*e"))

print('\n\n')

print(s.removeStars("erase*****"))
print(s.removeStars1("erase*****"))
