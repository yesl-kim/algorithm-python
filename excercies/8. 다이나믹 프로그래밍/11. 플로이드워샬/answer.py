import sys

path='/Users/kim-yeseul/Documents/dev/algorithm/algorithm-python/ignore/exercise/섹션 8/12. 플로이드 워샬 알고리즘/in4.txt'
sys.stdin=open(path,'rt')

n,m=map(int,input().split())
dp=[[float('inf')]*n for _ in range(n)]

# 초기화
for i in range(n):
    dp[i][i]=0
for _ in range(m):
    i,j,d=map(int,input().split())
    dp[i-1][j-1]=d

# 최소비용 계산
for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j])

# 출력
for line in dp:
    for d in line:
        if d==float('inf'):
            print('M', end=' ')
        else:
            print(d, end=' ')
    print()