import sys
import time

startt=time.time()
input_path='/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 7/11. 등산경로/in5.txt'
sys.stdin=open(input_path, 'rt')
N=int(input())
board=[[int(x) for x in input().split()] for _ in range(N)]
cnt=0

# 출발지점
start=(0,0)
end=(0,0)
for x in range(N):
    for y in range(N):
        now=board[x][y]
        if board[start[0]][start[1]]>board[x][y]:
            start=(x,y)
        elif board[end[0]][end[1]]<board[x][y]:
            end=(x,y)


# 경로탐색
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(x,y):
    global cnt
    if x==end[0] and y==end[1]:
        cnt+=1
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<N and board[x][y]<board[nx][ny]:
            dfs(nx,ny)
dfs(start[0], start[1])

# 정답출력
print(cnt)
end=time.time()
print(f"{end - startt:.5f} sec")