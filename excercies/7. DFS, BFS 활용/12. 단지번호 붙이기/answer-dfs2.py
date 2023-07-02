import sys
import time

start=time.time()
input_path='/Users/yesl.k/Dev/coding_test/algorithm-python/ignore/섹션 7/12. 단지번호붙이기/in5.txt'
sys.stdin=open(input_path, 'rt')

N=int(input())
board=[[int(x) for x in input()] for _ in range(N)]
res=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    global cnt
    board[x][y]=0
    for i in range(4):
        xx,yy=x+dx[i],y+dy[i]
        if 0<=xx<N and 0<=yy<N and board[xx][yy]==1:
            cnt+=1
            dfs(xx,yy)

for i in range(N):
    for j in range(N):
        if board[i][j]==1:
            cnt=1   
            dfs(i,j)
            res.append(cnt)

print(len(res))
res.sort()
for x in res:
    print(x)


end=time.time()
print(f"{end - start:.5f} sec")