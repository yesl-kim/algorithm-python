# https://leetcode.com/problems/summary-ranges/
# 재귀?

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        _range = lambda s, e: [str(nums[s]) if s == e else f"{nums[s]}->{nums[e]}"]
        def summary(s, e):
            if e == len(nums):
                return _range(s, e-1)
            
            if nums[e]-nums[s] == e-s:
                return summary(s, e+1)

            return _range(s, e-1) + summary(e, e+1)
        
        if not nums:
            return nums
        return summary(0, 1)
    

s = Solution()
nums = [0,1,2,4,5,7]
print(s.summaryRanges(nums))