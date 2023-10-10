# https://leetcode.com/problems/summary-ranges/

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        n = len(nums)-1
        start = 0
        res = []
        summary = lambda e: res.append(str(nums[start]) if start == e else f"{nums[start]}->{nums[e]}")

        for i in range(n):
            if nums[i]+1 != nums[i+1]:
                summary(i)
                start = i+1
        summary(n)
        
        return res

s = Solution()
# nums = [0,1,2,4,5,7]
nums = []
# nums = [-1]
print(s.summaryRanges(nums))