# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        last = nums[0]
        for num in nums:
            if last != num:
                nums[k] = num
                last = num
                k += 1
        return k