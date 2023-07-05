import sys

input_path='/Users/yesl.k/Dev/coding_test/algorithm-python/ignore/섹션 8/4. 최대부분증가수열/in5.txt'
sys.stdin=open(input_path, 'rt')

n=int(input())
ns=[int(x) for x in input().split()]

memo=[0]*n
memo[-1]=1

def dfs(L=0):
    if memo[L]>0: return memo[L]
    else:
        memo[L]=max(1,memo[L])
        for i in range(L+1,n):
            if ns[L]>=ns[i]: continue
            memo[L]=max(memo[L],dfs(i)+1)
        return memo[L]

for i in range(n-1):
    dfs(i)
print(max(memo))