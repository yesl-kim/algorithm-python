import sys
import time

start=time.time()
input_path='/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 7/9. 미로의 최단거리 통로/in1.txt'
sys.stdin=open(input_path, 'rt')
N=7
g=[[int(x) for x in input().split()] for _ in range(N)]
res=float('inf')
d=[1,-1]

def bfs(x=0,y=0,cnt=0):
    global res
    if cnt>res: return
    if x==6 and y==6:
        if res>cnt:
            res=cnt
    else:
        g[x][y]=1
        for i in d:
            if 0<=x+i <N and g[x+i][y]==0:bfs(x+i,y,cnt+1)
            if 0<=y+i<N and g[x][y+i]==0:bfs(x,y+i,cnt+1)
        g[x][y]=0

    
            
bfs()
if res==float('inf'): print(-1)
else: print(res)
end=time.time()
print(f"{end - start:.5f} sec")