# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        for i, v in enumerate(digits):
            if v == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break
        else:
            digits.append(1)

        digits.reverse()
        return digits