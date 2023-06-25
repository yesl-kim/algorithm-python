import sys
import time
from collections import deque

start=time.time()
input_path='/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 7/9. 미로의 최단거리 통로/in2.txt'
sys.stdin=open(input_path, 'rt')
N=7
board=[[int(x) for x in input().split()] for _ in range(N)]
dis=[[0]*N for _ in range(N)]
q=deque([(0,0)])
dx=[-1,1,0,0]
dy=[0,0,-1,1]

while q:
    x,y=q.popleft()
    # if x==6 and y==6:
    #     break
    # x=6, y=6이면 어차피 상,하,좌,우 갈 곳이 없기 때문에 (이미 갔거나 못가거나)
    # 순회가 종료됨
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if 0<=nx<N and 0<=ny<N and board[nx][ny]==0:
            board[nx][ny]=1
            q.append((nx,ny))
            dis[nx][ny]=dis[x][y]+1

if dis[6][6]==0:
    print(-1)
else:
    print(dis[6][6])

end=time.time()
print(f"{end - start:.5f} sec")