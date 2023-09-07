# https://leetcode.com/problems/plus-one/
from typing import List

# 1. 커플링 제거
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        digits[0] += 1

        for i, v in enumerate(digits):
            if v > 9:
                digits[i] = v % 10
                digits[i+1] += 1
            else:
                break
        
        digits.reverse()
        return digits

# 2. reverse를 두 번 하는 것 피하기
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1

        for i, v in enumerate(reversed(digits)):
            idx = -1-i
            if v > 9:
                digits[idx] = v % 10
                digits[idx - 1] += 1
            else:
                break
        
        return digits
    

digits=[1,9,4,9,9]
s = Solution()
print(s.plusOne(digits))