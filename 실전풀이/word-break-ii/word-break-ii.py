# https://leetcode.com/problems/word-break-ii/
from typing import List
from functools import reduce

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def find(s, sentence = ''):
            if not s:
                return [sentence.strip()]

            return reduce(lambda sentences, word: sentences + find(s[len(word):], sentence + ' ' + word), 
                          (word for word in wordDict if s.startswith(word)), [])

        return find(s)
    
solution = Solution()

s='catsanddog'
wordDict = ["cat","cats","and","sand","dog"]
print(solution.wordBreak(s, wordDict))