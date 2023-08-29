# https://leetcode.com/problems/generate-parentheses/

from typing import List

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


    # def generateParenthesis(self, n: int) -> List[str]:
    #     parentheses = ['(', ')']
    #     res = []

    #     def generate(L = 0, s = ''):
    #         if L == n*2:
    #             if self.isValid(s):
    #                 res.append(s)
    #         else:
    #             for i in range(2):
    #                 generate(L+1, s+parentheses[i])

    #     generate()
    #     return res

    # res 제거, 반환값 활용
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(L = 0, s = ''):
            if L == n*2:
                return [s] if self.isValid(s) else []
            else:
                return generate(L+1, s+'(') + generate(L+1, s+')')

        return generate()
    