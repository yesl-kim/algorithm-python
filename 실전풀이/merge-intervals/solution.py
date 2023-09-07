# https://leetcode.com/problems/merge-intervals/
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        def _merge(intervals):
            if len(intervals) <= 1:
                return intervals
            
            next, cur = intervals.pop(), intervals[-1] # 여기가 문제
            if cur[1] < next[0]:
                return _merge(intervals) + [next]
            
            cur[0], cur[1] = min(cur[0], next[0]), next[1]
            return _merge(intervals)

        intervals.sort(key=lambda x:x[1])
        return _merge(intervals)
            
    

s = Solution()
intervals = []
# intervals = [[15,18], [1,3],[2,6],[8,10]]
print('=>', s.merge(intervals))