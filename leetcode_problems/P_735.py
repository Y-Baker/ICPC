#!/usr/bin/python3

from typing import List

class Solution:
    # def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    #     stack = []

    #     for ele in asteroids:
    #         if len(stack) == 0:
    #             stack.append(ele)
    #         else:
    #             if stack[-1] * ele >= 0:
    #                 stack.append(ele)
    #             else:
    #                 while abs(ele) > abs(stack[-1]):
    #                     stack.pop()
    #                     if len(stack) == 0:
    #                         stack.append(ele)
    #                         break
    #                 if abs(ele) == abs(stack[-1]):
    #                     stack.pop()

    #     return stack

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ele in asteroids:
            if len(stack) == 0:
                stack.append(ele)
            else:
                if stack[-1] * ele >= 0:
                    stack.append(ele)
                elif ele > 0:
                    stack.append(ele)
                else:
                    while stack[-1] > 0 and abs(ele) >= stack[-1]:
                        if len(stack) == 1 or stack[-2] < 0:
                            if stack[-1] != abs(ele):
                                stack.pop()
                                stack.append(ele)
                            else:
                                stack.pop()
                            break
                        if abs(ele) == stack[-1]:
                            stack.pop()
                            break
                        stack.pop()

        return stack

s = Solution()
print(s.asteroidCollision([5, 10, -5])) # [5, 10]
print(s.asteroidCollision([8, -8])) # []
print(s.asteroidCollision([10, 2, -5])) # [10]
print(s.asteroidCollision([-2,1,1,-1])) # [-2, 1]