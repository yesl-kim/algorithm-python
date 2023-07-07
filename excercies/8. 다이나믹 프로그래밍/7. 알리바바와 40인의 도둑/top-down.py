import sys

path='/Users/kim-yeseul/Documents/dev/algorithm/algorithm-python/ignore/exercise/섹션 8/7, 8. 알리바바와 40인의 도둑/in5.txt'
sys.stdin=open(path,'rt')
n=int(input())
board=[[int(x) for x in input().split()] for _ in range(n)]
ds=[[0]*n for _ in range(n)]
ds[0][0]=board[0][0]

def dfs(x,y):
    if 0<=x and 0<=y:
        if 0<ds[x][y]:
            return ds[x][y]
        else:
            ds[x][y]=min(dfs(x-1,y),dfs(x,y-1))+board[x][y]
            return ds[x][y]
    else:
        return float('inf')

# 정답풀이
def dfs2(x,y):
    if 0<ds[x][y]:
        return ds[x][y]
    else:
        if x==0:
            ds[x][y]=dfs(x,y-1)+board[x][y]
        elif y==0:
            ds[x][y]=dfs(x-1,y)+board[x][y]
        else:
            ds[x][y]=min(dfs(x-1,y),dfs(x,y-1))+board[x][y]
        return ds[x][y]

print(dfs2(n-1,n-1))
