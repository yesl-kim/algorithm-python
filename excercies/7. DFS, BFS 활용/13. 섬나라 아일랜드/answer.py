import sys
import time
from collections import deque

startt=time.time()
input_path='/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 7/13. 섬나라 아일랜드/in5.txt'
sys.stdin=open(input_path, 'rt')
N=int(input())
island=[[int(x) for x in input().split()] for _ in range(N)]
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]
cnt=0
res=[]
q=deque()

for z in range(N):
    for j in range(N):
        if island[z][j]==1:
            # cnt=0
            cnt+=1
            island[z][j]=0
            q.append((z,j))

            while q:
                # cnt+=1
                x,y=q.popleft()
                for i in range(8):
                    nx,ny=x+dx[i],y+dy[i]
                    if 0<=nx<N and 0<=ny<N and island[nx][ny]==1:
                        island[nx][ny]=0
                        q.append((nx,ny))
            # res.append(cnt)

print(cnt)
end=time.time()
print(f"{end - startt:.5f} sec")