# https://leetcode.com/problems/merge-intervals/
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        def _merge(acc, it):
            try:
                prev = acc[-1]
                cur = next(it)
                if cur[0] <= prev[1]:
                    prev[1] = max(prev[1], cur[1])
                    return _merge(acc, it)
                
                return _merge(acc + [cur], it)
            except:
                return acc

        intervals = iter(intervals)
        return _merge([next(intervals)], intervals)