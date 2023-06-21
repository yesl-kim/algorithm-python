import sys
import time

start=time.time()
input_path='/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 7/4. 동전바꿔주기/in5.txt'
sys.stdin=open(input_path, 'rt')
T=int(input())
k=int(input())
coin=[list(map(int, input().split())) for _ in range(k)]
cnt=0

def dfs(L=0, sum=0):
    global cnt
    if sum>T: return
    if L==k:
        if sum==T:
            cnt+=1
    else:
        for n in range(coin[L][1]+1):
            dfs(L+1, sum+(coin[L][0]*n))

    

dfs()
print(cnt)
end=time.time()
print(f"{end - start:.5f} sec")