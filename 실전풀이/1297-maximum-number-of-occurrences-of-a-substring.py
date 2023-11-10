from collections import defaultdict, Counter

def window(arr, size):
    for i in range(len(arr) - size + 1):
        yield arr[i: i + size]

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        subs_cnt = defaultdict(int)

        for size in range(minSize, maxSize + 1):
            for subs in window(s, size):
                if len(set(subs)) <= maxLetters:
                    subs_cnt[subs] += 1
        
        return max(subs_cnt.values()) if subs_cnt else 0


# s = 'aababcaab'
# maxLetters = 2
# minSize = 3
# maxSize = 4
# print('=>', Solution().maxFreq(s, maxLetters, minSize, maxSize))