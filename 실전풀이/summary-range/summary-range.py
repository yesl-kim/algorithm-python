# https://leetcode.com/problems/summary-ranges/

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        n = len(nums)-1
        left = 0
        res = []

        for i in range(n):
            if nums[i]+1 != nums[i+1]:
                res.append(str(nums[i]) if left == i else f"{nums[left]}->{nums[i]}")
                left = i+1

        res.append(str(nums[n]) if left == n else f"{nums[left]}->{nums[n]}")
        
        return res

s = Solution()
# nums = [0,1,2,4,5,7]
nums = []
# nums = [-1]
print(s.summaryRanges(nums))