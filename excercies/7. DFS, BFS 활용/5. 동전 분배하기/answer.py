import sys
import time

start=time.time()
input_path='/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 7/5. 동전분배하기/in0.txt'
sys.stdin=open(input_path, 'rt')
N=int(input())
coin=[int(input()) for _ in range(N)]
res=float('inf')

def dfs(L=0, s=[0,0,0]):
    global res
    if L==N:
        a=max(s)-min(s)
        if res>a: 
            res=a
    else:
        for i in range(3):
            if s[i]+coin[L] in s: continue
            s[i]+=coin[L]
            dfs(L+1, s)
            s[i]-=coin[L]

dfs()
print(res)
end=time.time()
print(f"{end - start:.5f} sec")