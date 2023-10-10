# https://leetcode.com/problems/array-partition
from typing import List
from functools import reduce


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(map(min, zip(nums[::2], nums[1::2])))