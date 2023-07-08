import sys

path='/Users/kim-yeseul/Documents/dev/algorithm/algorithm-python/ignore/exercise/섹션 8/11. 최대점수 구하기(냅색알고리즘)/in5.txt'
sys.stdin=open(path,'rt')

n,m=map(int,input().split())
dp=[0]*(m+1)

for _ in range(n):
    s,t=map(int,input().split())
    for i in range(m,t-1,-1):
        dp[i]=max(dp[i],dp[i-t]+s)

print(dp[m])
