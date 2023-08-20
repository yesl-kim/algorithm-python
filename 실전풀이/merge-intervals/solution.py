# https://leetcode.com/problems/merge-intervals/
from functools import reduce

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        
        def _merge(acc, i = 1):
            if i == len(intervals):
                return acc

            prev = acc[-1]
            cur = intervals[i]
            if prev[1] < cur[0]:
                acc.append(cur)
            else:
                prev[1] = max(prev[1], cur[1])
            return _merge(acc, i+1)
            
            
        return _merge([intervals[0]])