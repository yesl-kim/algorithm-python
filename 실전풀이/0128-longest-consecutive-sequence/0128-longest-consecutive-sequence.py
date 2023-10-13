# https://leetcode.com/problems/longest-consecutive-sequence/
from typing import List

class Solution:
    def length(self, sequence):
        return sequence[1] - sequence[0] + 1
    
    def longestConsecutive(self, nums: List[int]) -> int:
        sequences = {}
        nums = set(nums)
        for x in nums:
            start = sequences.get(x-1, (x, None))[0]
            end = sequences.get(x+1, (None, x))[1]
            sequences[start] = sequences[end] = (start, end)
        
        if not sequences:
            return 0
        return max(map(self.length, sequences.values()))

nums = [0,3,7,2,5,8,4,6,0,1]
s = Solution()
print(s.longestConsecutive(nums))