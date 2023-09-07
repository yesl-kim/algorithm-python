# https://leetcode.com/problems/maximum-subarray/

from itertools import accumulate

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
        
        sums=list(accumulate(nums))
        min=0
        res=max(nums)
        for x in sums:
            if x < min:
                min = x
            else:
                res=max(res, x, x-min)
        return res