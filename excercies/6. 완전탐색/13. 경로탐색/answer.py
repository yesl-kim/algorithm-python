import sys
import time

# 트럭 가용무게 c
# 바둑이의 몸무게 배열 n
path='/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 6/15. 경로탐색'
num=1

input_path=path + "/in" + str(num) + ".txt"
sys.stdin=open(input_path, 'rt')
N,E=map(int, input().split())
# ====================

g=[[0]*(N+1) for _ in range(N+1)]
for _ in range(E):
    f,t=map(int,input().split())
    g[f][t]=1

c=0
def dfs(L=1, res=[1]):
   global c
   if L==N:
       print(" ".join(str(x) for x in res))
       c+=1
   for i,v in enumerate(g[L]):
       if v==0 or i in res: continue
       res.append(i)
       dfs(i, res)
       res.pop() # 원복 필수

# ====================

dfs()
print(c)
