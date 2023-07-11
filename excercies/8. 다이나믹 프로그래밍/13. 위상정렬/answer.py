import sys
from collections import deque

path='/Users/kim-yeseul/Documents/dev/algorithm/algorithm-python/ignore/exercise/섹션 8/14. 위상정렬/in1.txt'
sys.stdin=open(path,'rt')

n,m=map(int,input().split())
dg=[0]*(n+1)
board=[[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x,y=map(int,input().split())
    board[x][y]=1
    dg[y]+=1

q=deque()
res=[]
while len(res)<n:
    for i in range(1,n+1):
        if i in res: continue
        if dg[i]==0:
            q.append(i)
        while q:
            x=q.popleft()
            res.append(x)
            for to,v in enumerate(board[x]):
                if v==1:
                    dg[to]-=1


print(res)