import sys
from collections import deque

input_path='/Users/yesl.k/Dev/coding_test/algorithm-python/ignore/섹션 7/12. 단지번호붙이기/in4.txt'
sys.stdin=open(input_path, 'rt')
N=int(input())
board=[[int(x) for x in input()] for _ in range(N)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
res=[]

q=deque()
for i in range(N):
    for j in range(N):
      if board[i][j]==1:
        q.append((i,j))
        board[i][j]=0
        cnt=1
        while q:
           x,y=q.popleft()
           for z in range(4):
              xx,yy=x+dx[z],y+dy[z]
              if 0<=xx<N and 0<=yy<N and board[xx][yy]==1:
                q.append((xx,yy))
                board[xx][yy]=0
                cnt+=1
        res.append(cnt)
  
print(len(res))
res.sort()
for r in res:
  print(r)