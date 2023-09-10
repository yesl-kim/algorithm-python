# https://leetcode.com/problems/climbing-stairs
import time

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
    
    def recursiveClimbStairs(self, n: int) -> int:
        def climb(stair=0):
            if stair > n:
                return 0
            if stair == n:
                return 1
            
            return climb(stair+1) + climb(stair+2)
        
        return climb()


s = Solution()
n = 38

for fn in (s.climbStairs, s.recursiveClimbStairs):
    start = time.time()
    ans = fn(n)
    end = time.time()
    print(f"ans: {ans} ({end - start:.5f} sec)")

# DP (0.00001 sec)
# recursive (16.67712 sec)