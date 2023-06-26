import sys
import time

startt=time.time()
input_path='/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 7/12. 단지번호붙이기/in1.txt'
sys.stdin=open(input_path, 'rt')
N=int(input())
board=[[int(x) for x in input()] for _ in range(N)]
res=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    global cnt
    cnt+=1
    board[x][y]=0
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<N and 0<=ny<N and board[nx][ny]==1:
            dfs(nx,ny)

for i in range(N):
    for j in range(N):
        if board[i][j]==1:
            cnt=0
            dfs(i,j)
            res.append(cnt)
print(len(res))
res.sort()
for x in res:
    print(x)

end=time.time()
print(f"{end - startt:.5f} sec")