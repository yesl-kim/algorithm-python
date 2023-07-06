import sys

path='/Users/yesl.k/Dev/coding_test/algorithm-python/ignore/섹션 8/7, 8. 알리바바와 40인의 도둑/in5.txt'
sys.stdin=open(path,'rt')
n=int(input())
board=[[int(x) for x in input().split()] for _ in range(n)]
ds=[[0]*n for _ in range(n)]
ds[0][0]=board[0][0]

dx=[-1,0]
dy=[0,-1]

for x in range(n):
    for y in range(n):
        if x==0 and y==0: continue
        min=float('inf')
        for i in range(2):
            xx,yy=x+dx[i],y+dy[i]
            if 0<=xx<n and 0<=yy<n and min>ds[xx][yy]:
                min=ds[xx][yy]
        ds[x][y]=min+board[x][y]

print(ds[n-1][n-1])