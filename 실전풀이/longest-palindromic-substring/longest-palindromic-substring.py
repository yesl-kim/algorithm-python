# https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s

        res = ''
        for i in range(n):
            for size in range(2):
                left, right = i, i + size
                while 0 <= left and right < n and s[left] == s[right]:
                    substring = s[left: right + 1]
                    if len(res) < len(substring):
                        res = substring
                    left -= 1
                    right += 1

        return res