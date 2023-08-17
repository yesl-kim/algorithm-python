# https://leetcode.com/problems/intersection-of-two-arrays-ii/

from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        occasions = defaultdict(int)
        for n in nums1:
            occasions[n]+=1
        
        res = []
        for n in nums2:
            if 0 < occasions[n]:
                res.append(n)
                occasions[n]-=1
        
        return res