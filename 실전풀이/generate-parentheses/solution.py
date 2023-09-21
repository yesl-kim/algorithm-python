# https://leetcode.com/problems/generate-parentheses/

from typing import List
from functools import reduce

class Solution:
    def isValid(self, s: str) -> bool:
        opens=[]

        for x in s:
            if x == '(':
                opens.append(x)
            else:
                if not opens:
                    return False
                opens.pop()

        return len(opens) == 0

    def generateParenthesis(self, n: int) -> List[str]:
        pairs = ('((', '()', '))', ')(')
        def generate(n):
            if n == 1:
                return pairs
            return (p1 + p2 for p1 in pairs for p2 in generate(n-1))

        return [parenthesis for parenthesis in generate(n) if self.isValid(parenthesis)]

s = Solution()
print(s.generateParenthesis(3))