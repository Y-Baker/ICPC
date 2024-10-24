#!/usr/bin/python3

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def gonext(idx):
            return (idx + 1) % len(gas)

        def check(start):
            cnt = gas[start]
            idx = gonext(start)
            cnt2 = 0
            while cnt2 < len(gas):
                cnt -= cost[idx - 1]
                if cnt < 0:
                    return False
                cnt += gas[idx]
                cnt2 += 1
                idx = gonext(idx)
            return True

        for i in range(len(gas)):
            if check(i):
                return i
        return -1


s = Solution()
print(s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])) # 3
print(s.canCompleteCircuit([2,3,4], [3,4,3])) # -1
print(s.canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1])) # 4
