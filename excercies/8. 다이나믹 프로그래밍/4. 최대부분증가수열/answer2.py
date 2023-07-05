import sys

input_path='/Users/yesl.k/Dev/coding_test/algorithm-python/ignore/섹션 8/4. 최대부분증가수열/in4.txt'
sys.stdin=open(input_path, 'rt')

n=int(input())
ns=[int(x) for x in input().split()]

memo=[0]*n
memo[-1]=1

for i in range(n-2,0,-1):
    res=0
    for j in range(i+1,n):
        if ns[i]<ns[j] and res<memo[j]:
            res=memo[j]
    memo[i]=res+1

print(max(memo))