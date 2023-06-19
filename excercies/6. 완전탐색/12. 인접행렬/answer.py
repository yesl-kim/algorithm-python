import sys
import time

path='/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 6/11. 수들의 조합'
num=1

input_path="/Users/kimyeseul/dev/algorithm/algorithm-python/excercies/6. 완전탐색/12. 인접행렬/in.txt"
sys.stdin=open(input_path, 'rt')
N,E=map(int, input().split())

# ====================

# 1. for문
res=[[0]*N for _ in range(N)]
for _ in range(E):
    f,t,v=map(int, input().split())
    res[f-1][t-1]=v

for i in range(N):
    for j in range(N):
        print(res[i][j], end=' ')
    print()


# 2. 재귀
res=[0]*N
def dfs(L=0, i=1):
    global res
    if L==E:
        print(" ".join(str(x) for x in res))
    else:
        f,t,v=map(int, input().split())
        while i<f:
            print(" ".join(str(x) for x in res))
            res=[0]*N
            i+=1
        res[t-1]=v
        dfs(L+1, f)
dfs()
        
# ====================

