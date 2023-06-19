import sys
import time

start=time.time()
input_path='/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 7/2. 휴가/in4.txt'
sys.stdin=open(input_path, 'rt')
N=int(input())
n=[tuple(map(int,input().split())) for _ in range(N)]
res=0
# print(n)

# def dfs(L=0,p=0):
#     global res
#     if L>N: return
#     if L==N:
#         if res<p: res=p
#     else:
#         dfs(L+1,p)
#         dfs(L+n[L][0], p+n[L][1])

def dfs(L=0,p=0):
    global res
    if L==N:
        if res<p: res=p
    else:
        if L+n[L][0]<=N:
            dfs(L+n[L][0], p+n[L][1])
        dfs(L+1,p)

dfs()
print(res)
end=time.time()
print(f"{end - start:.5f} sec")