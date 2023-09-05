# https://leetcode.com/problems/excel-sheet-column-number/

numerical = lambda word: ord(word) - 64

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        decimals = 26
        for i, word in enumerate(list(reversed(columnTitle))):
            res += (decimals**i) * numerical(word)

        return res