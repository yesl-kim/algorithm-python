import sys
import time

start=time.time()
input_path='/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 7/1. 최대점수 구하기/in5.txt'
sys.stdin=open(input_path, 'rt')
N,M=map(int, input().split())
n=[tuple(map(int,input().split())) for _ in range(N)]
n.sort(key=lambda x: (x[0],-x[1]), reverse=True)
res=0
# print(n)

def dfs(L=0,s=0,t=M):
    global res
    remain=sum([x[0] for x in n[L:-1]])
    if s+remain<res: return
    if L==N or t==0:
        if res<s: res=s
    else:
        dfs(L+1,s,t)
        need=n[L][1]
        if not t-need<0: dfs(L+1, s+n[L][0],t-need)

dfs()
print(res)
end=time.time()
print(f"{end - start:.5f} sec")