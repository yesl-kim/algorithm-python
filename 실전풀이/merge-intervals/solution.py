# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        
        res = [intervals[0]]
        for cur in intervals[1:]:
            prev = res[-1]
            if prev[1] < cur[0]:
                res.append(cur)
            else:
                prev[1] = max(prev[1],cur[1])
        
        return res