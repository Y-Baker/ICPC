#!/usr/bin/python3
from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxx = 0
        maxx = max(maxx, gain[0])
        for i in range(1, len(gain)):
            gain[i] += gain[i-1]
            maxx = max(maxx, gain[i])
        return maxx
