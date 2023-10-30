# https://leetcode.com/problems/kth-largest-element-in-an-array/

from heapq import heapify, heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest = nums[:k]
        heapify(largest)
        
        for n in nums[k:]:
            heappush(largest, n)
            heappop(largest)
        
        return largest[0]