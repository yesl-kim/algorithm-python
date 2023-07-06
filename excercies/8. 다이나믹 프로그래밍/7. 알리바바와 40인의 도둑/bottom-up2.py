import sys

path='/Users/yesl.k/Dev/coding_test/algorithm-python/ignore/섹션 8/7, 8. 알리바바와 40인의 도둑/in5.txt'
sys.stdin=open(path,'rt')
n=int(input())
board=[[int(x) for x in input().split()] for _ in range(n)]
ds=[[0]*n for _ in range(n)]
ds[0][0]=board[0][0]

for i in range(1,n):
    ds[0][i]=ds[0][i-1]+board[0][i]
    ds[i][0]=ds[i-1][0]+board[i][0]

for x in range(1,n):
    for y in range(1,n):
        ds[x][y]=min(ds[x][y-1],ds[x-1][y])+board[x][y]

print(ds[n-1][n-1])