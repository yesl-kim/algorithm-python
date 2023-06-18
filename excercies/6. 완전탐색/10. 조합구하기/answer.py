import sys
import time

# 트럭 가용무게 c
# 바둑이의 몸무게 배열 n
path='/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 6/10. 조합 구하기'
num=4

input_path=path + "/in" + str(num) + ".txt"
sys.stdin=open(input_path, 'rt')
N,m=map(int, input().split())
# N,m=4,2
# ====================

c=0
n=list(range(1, N+1))
res=[0]*m
def dfs(L=0, i=0):
    global c
    if L==m:
        print(" ".join(str(x) for x in res))
        c+=1
    else:
        for j in range(i,N):
            res[L]=n[j]
            dfs(L+1, j+1)      
        
# ====================

dfs()
print(c)
