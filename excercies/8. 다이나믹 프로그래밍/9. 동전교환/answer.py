import sys
import time

path='/Users/kim-yeseul/Documents/dev/algorithm/algorithm-python/ignore/exercise/섹션 8/10. 동전교환/in5.txt'
sys.stdin=open(path, 'rt')
start=time.time()

n=int(input())
cs=[int(x) for x in input().split()]
sum=int(input())
dp=[float('inf')]*(sum+1)
dp[0]=0

for c in cs:
    for i in range(c,sum+1):
        dp[i]=min(dp[i],dp[i-c]+1)

print(dp[sum])