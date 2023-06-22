import sys
import time

start=time.time()
input_path='/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 7/7. 송아지 찾기/in0.txt'
sys.stdin=open(input_path, 'rt')
S,E=map(int, input().split())
res=float('inf')

# 첫 시도
# def dfs(L=S, cnt=0):
#     global res
#     if cnt>res: return
#     if L==E:
#         if res>cnt: res=cnt
#     elif L<E:
#         dfs(L+5,cnt+1)
#         dfs(L+1,cnt+1)
#     else:
#         dfs(L-1,cnt+1)

# def dfs(s=S,cnt=0):
#     global res
#     if cnt>res: return
#     if s==E:
#         if res>cnt: res=cnt
#     elif s<E:
#         if (E-s)/5>1:
#             jump=int((E-s)/5)
#             dfs(s+jump*5,cnt+jump)
#         else:
#             jump=E-s
#             dfs(s+jump, cnt+jump)
#     else:
#         dfs(s-1,cnt+1)

def dfs(s=S,cnt=0):
    global res
    if cnt>res: return
    if s==E:
        if res>cnt: res=cnt
    elif s<E:
        if (E-s)/5>1:
            jump=(E-s)//5
            dfs(s+jump*5,cnt+jump)
            dfs(s+(jump+1)*5, cnt+jump+1)
        else:
            jump=E-s
            dfs(s+jump, cnt+jump)
    else:
        dfs(s-1,cnt+1)
    

dfs()
print(res)
end=time.time()
print(f"{end - start:.5f} sec")