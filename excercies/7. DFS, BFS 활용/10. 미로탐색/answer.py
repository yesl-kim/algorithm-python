import sys
import time

start=time.time()
input_path='/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 7/10. 미로탐색/in5.txt'
sys.stdin=open(input_path, 'rt')
N=7
g=[[int(x) for x in input().split()] for _ in range(N)]
res=float('inf')
d=[1,-1]
cnt=0

def bfs(x=0,y=0):
    global cnt
    if x==6 and y==6:
        cnt+=1
    else:
        g[x][y]=1
        for i in d:
            if 0<=x+i <N and g[x+i][y]==0:bfs(x+i,y)
            if 0<=y+i<N and g[x][y+i]==0:bfs(x,y+i)
        g[x][y]=0

    
            
bfs()
print(cnt)
end=time.time()
print(f"{end - start:.5f} sec")