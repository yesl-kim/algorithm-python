import sys

input_path='/Users/yesl.k/Dev/coding_test/algorithm-python/ignore/섹션 8/1, 2. 네트워크 선 자르기/in5.txt'
sys.stdin=open(input_path, 'rt')

N=int(input())
# N=7

# dy[n]=f(n)
dy=[0]*(N+1)
dy[0]=0
dy[1]=1
dy[2]=2


def dfs(L):
    if dy[L]!=0: 
        return dy[L]
    if L==0: 
        return 0
    else:
        dy[L]=dfs(L-1)+dfs(L-2)
        return dy[L]

print(dfs(N))