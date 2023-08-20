# https://leetcode.com/problems/merge-intervals/
from functools import reduce

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        def _merge(acc, cur):
            prev = acc[-1]
            if prev[1] < cur[0]:
                acc.append(cur)
            else:
                prev[1] = max(prev[1],cur[1])
            return acc

        return reduce(_merge, intervals[1:], [intervals[0]])