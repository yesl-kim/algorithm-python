import sys
import time
from collections import deque

start=time.time()
input_path='/Users/yesl.k/Dev/coding_test/algorithm-python/ignore/섹션 7/17. 피자 배달 거리/in5.txt'
sys.stdin=open(input_path, 'rt')
N,M=map(int, input().split())
board=[[int(x) for x in input().split()] for _ in range(N)]

hs=[]
pz=[]
for i in range(N):
    for j in range(N):
        if board[i][j]==1:
            hs.append((i,j))
        elif board[i][j]==2:
            pz.append((i,j))

# print(hs)
# print(pz)

cb=[0]*M
res=float('inf')
def dfs(L=0,i=0):
    global res
    if L==M:
        dsum=0
        for x1,y1 in hs:
            d=float('inf')
            for i in cb:
                x2,y2=pz[i]
                d=min(d,abs(x1-x2)+abs(y1-y2))
            dsum+=d
        res=min(res,dsum)
    else:
        for j in range(i,len(pz)):
            cb[L]=j
            dfs(L+1,j+1)

dfs()
print(res)
end=time.time()
print(f"{end - start:.5f} sec")