# https://leetcode.com/problems/build-array-from-permutation/

class Solution:
    def buildArray(self, nums):
        return [nums[nums[i]] for i in range(len(nums))]