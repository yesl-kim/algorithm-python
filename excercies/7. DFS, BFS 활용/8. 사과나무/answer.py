import sys
import time

start=time.time()
input_path='/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 7/8. 사과나무/in5.txt'
sys.stdin=open(input_path, 'rt')
N=int(input())
g=[[int(x) for x in input().split()] for _ in range(N)]
mid=len(g)//2
res=0

def dfs(L=0,p=0):
    global res
    if L==N:
        print(res)
    else:
        for x in g[L][mid-p:mid+p+1]:
            res+=x
        if L<mid:
            dfs(L+1, p+1)
        else:
            dfs(L+1, p-1)
            
dfs()
end=time.time()
print(f"{end - start:.5f} sec")