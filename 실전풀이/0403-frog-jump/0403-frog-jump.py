# https://leetcode.com/problems/frog-jump/
from typing import List
from bisect import bisect_left

def memoize(fn):
    cache = {}
    def wrapper(*args):
        key = tuple(args)
        if not key in cache:
            cache[key] = fn(*args)
        return cache[key]
    return wrapper


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        @memoize
        def can_jump(pos, step):
            if pos == stones[-1]:
                return True
            
            i = bisect_left(stones, pos)
            if len(stones) <= i or pos != stones[i]:
                return False
            
            return any(can_jump(pos+step, k) for k in range(step-1, step+2) if 0<k)
        
        return can_jump(0, 1)