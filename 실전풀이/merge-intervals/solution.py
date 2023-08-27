# https://leetcode.com/problems/merge-intervals/
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        def _merge(prev, it):
            try:
                cur = next(it)
                if prev[1] < cur[0]:
                    return [prev] + _merge(cur, it)
                
                prev[1] = max(prev[1], cur[1])
                return _merge(prev, it)
            except:
                return [prev]

        intervals.sort(key=lambda x:x[0])
        intervals = iter(intervals)
        return _merge(next(intervals), intervals)
            
    

s = Solution()
intervals = [[15,18], [1,3],[2,6],[8,10]]
print('=>', s.merge(intervals))