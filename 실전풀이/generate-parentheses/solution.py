# https://leetcode.com/problems/generate-parentheses/

from typing import List
from itertools import product

# 오답: n=4, "(())(())" 누락
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return ['']
        return set(sum((['()'+p, '('+p+')', p+'()'] for p in self.generateParenthesis(n-1)), start=[]))
    

class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(o, c):
            if not o and not c:
                yield ''
            
            if 0 < o:
                yield from ('('+p for p in generate(o-1, c))
            if o < c and 0 < c:
                yield from (')'+p for p in generate(o, c-1))
        return list(generate(n, n))

        
s = Solution()
print(s.generateParenthesis(3))