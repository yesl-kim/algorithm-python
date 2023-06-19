import sys
import time

# 트럭 가용무게 c
# 바둑이의 몸무게 배열 n
path='/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 6/11. 수들의 조합'
num=5

input_path=path + "/in" + str(num) + ".txt"
sys.stdin=open(input_path, 'rt')
N,k=map(int, input().split())
n=list(map(int, input().split()))
m=int(input())
# N,k,m=5,3,6
# n=[2,4,5,8,12]
# ====================

c=0
res=[0]*k
def dfs(L=0, i=0):
    global c
    if L==k:
        s=sum(res)
        if s%m==0:c+=1
    else:
        for j in range(i, N):
            res[L]=n[j]
            dfs(L+1, j+1)
        
# ====================

dfs()
print(c)
