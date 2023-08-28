# https://leetcode.com/problems/merge-intervals/
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        def _merge(intervals):
            if len(intervals) == 1:
                return intervals
            else:
                prev, cur = intervals.pop(0), intervals[0]

                if prev[1] < cur[0]:
                    return [prev] + _merge(intervals)
                
                cur[0], cur[1] = prev[0], max(prev[1], cur[1])
                return _merge(intervals)

        intervals.sort(key=lambda x:x[0])
        return _merge(intervals)
            
    

s = Solution()
intervals = [[15,18], [1,3],[2,6],[8,10]]
print('=>', s.merge(intervals))