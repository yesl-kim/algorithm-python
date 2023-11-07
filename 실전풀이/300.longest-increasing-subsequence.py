from collections import defaultdict

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = list(range(len(nums)))
        
        for i in range(len(nums)):
            max_len = 0
            for j in range(i):
                if nums[i] > nums[j] and dp[j] > max_len:
                    max_len = dp[j]
            dp[i] = max_len + 1
                
        return max(dp)