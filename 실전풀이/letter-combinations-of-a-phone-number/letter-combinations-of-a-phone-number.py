# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return ["".join(x) for x in (product(*[letters[d] for d in digits]))]
