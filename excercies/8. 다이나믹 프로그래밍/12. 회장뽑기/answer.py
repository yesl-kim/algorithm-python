import sys

path='/Users/kim-yeseul/Documents/dev/algorithm/algorithm-python/ignore/exercise/섹션 8/13. 회장뽑기/in5.txt'
sys.stdin=open(path,'rt')

n=int(input())
dp=[[float('inf')]*n for _ in range(n)]
while True:
    i,j=map(int,input().split())
    if i==-1 and j==-1: break
    dp[i-1][j-1]=1
    dp[j-1][i-1]=1
for i in range(n):
    dp[i][i]=0

score=float('inf')
dis=[0]*n
for k in range(n):
    for i in range(n):
        s=0
        for j in range(n):
            if i==j: continue
            dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j])
            s=max(s,dp[i][j])
        score=min(score,s)
        dis[i]=s

res=[i+1 for i in range(n) if dis[i]==score]
print(score, len(res))
for x in res:
    print(x,end=' ')