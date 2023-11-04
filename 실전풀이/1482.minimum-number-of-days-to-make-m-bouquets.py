from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def check(x):
            bouquets = 0
            flowers = 0
            for day in bloomDay:
                if day <= x:
                    flowers += 1
                else:
                    bouquets += (flowers // k)
                    flowers = 0
            
            bouquets += (flowers // k)
            return bouquets >= m

            
        # 0 < x <= max(bloomDay)
        lo, hi = 1, max(bloomDay)
        res = None
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return res if res else -1
    

# m = 3
m = 1
k = 1
# k = 2
# bloomDay = [1, 10, 3, 10, 2]
bloomDay = [1000000000,1000000000]
print('=>', Solution().minDays(bloomDay, m, k))