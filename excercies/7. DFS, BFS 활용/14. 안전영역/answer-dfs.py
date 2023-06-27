import sys
import time

startt=time.time()
input_path='/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 7/14. 안전영역/in5.txt'
sys.stdin=open(input_path, 'rt')
sys.setrecursionlimit(10**6)
N=int(input())
board=[[int(x) for x in input().split()] for _ in range(N)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
res=0

def dfs(x,y):
    global rain
    ch[x][y]=1
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<N and 0<=ny<N and rain<board[nx][ny] and ch[nx][ny]==0:
            dfs(nx,ny)

    
# 강수량 범위
MIN=float('inf')
MAX=float('-inf')
for i in range(N):
    for j in range(N):
        n=board[i][j]
        if n<MIN: MIN=n
        if n>MAX: MAX=n

for rain in range(MIN-1,MAX):
    cnt=0
    ch=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if rain<board[i][j] and ch[i][j]==0:    
                cnt+=1
                dfs(i,j)
    if cnt==0: break
    if res<cnt: res=cnt
    
print(res)
end=time.time()
print(f"{end - startt:.5f} sec")