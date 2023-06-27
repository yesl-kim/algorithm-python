import sys
import time
from collections import deque

startt=time.time()
input_path='/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 7/15. 토마토/in4.txt'
sys.stdin=open(input_path, 'rt')
M,N=map(int,input().split())
day=0
n=0 # 안 익은 토마토 개수
box=[]
q=deque()
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 토마토가 담긴 상자 초기화
# 안 익은 토마토 개수 카운팅
for _ in range(N):
    line=[]
    for t in input().split():
        t=int(t)
        line.append(t)
        if t==0: 
            n+=1
    box.append(line)

# day 계산
if n==0: print(day)
else:
    while n:
        ch=[[0]*M for _ in range(N)]
        day+=1
        for x in range(N):
            for y in range(M):
                if box[x][y]==1:
                    for i in range(4):
                        nx,ny=x+dx[i],y+dy[i]
                        if 0<=nx<N and 0<=ny<M and box[nx][ny]==0 and ch[nx][ny]==0:
                            n-=1
                            ch[nx][ny]=1
                            q.append((nx,ny))
        if n>0 and len(q)>0:
            print(-1)
            break
        while q:
            x,y=q.popleft()
            box[x][y]=1
    else:
        print(day)
                    
                



end=time.time()
print(f"{end - startt:.5f} sec")


# [
#     [1, -1, 1, -1, 1, -1, 1, 1, 0, 0], 
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0], 
#     [1, 1, 1, 1, 1, 1, 1, -1, 0, -1], 
#     [1, 1, 1, 1, -1, 1, 1, -1, 0, 0], 
#     [1, 1, 1, 1, 1, -1, 1, 1, 0, 0], 
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0], 
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0], 
#     [1, 1, -1, 1, 1, 1, 1, 1, -1, 0], 
#     [-1, 1, 1, 1, -1, 1, 1, 1, 0, 0], 
#     [0, 0, -1, 1, 1, 1, 1, 1, 0, 0]
#     ]

# [
#     [1, -1, 1, -1, 1, -1, 1, 1, 0, 0], 
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0], 
#     [1, 1, 1, 1, 1, 1, 1, -1, 0, -1], 
#     [1, 1, 1, 1, -1, 1, 1, -1, 0, 0], 
#     [1, 1, 1, 1, 1, -1, 1, 1, 0, 0], 
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0], 
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0], 
#     [1, 1, -1, 1, 1, 1, 1, 1, -1, 0], 
#     [-1, 1, 1, 1, -1, 1, 1, 1, 0, 0], 
#     [0, 0, -1, 1, 1, 1, 1, 1, 0, 0]
# ]