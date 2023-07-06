import sys

input_path='/Users/yesl.k/Dev/coding_test/algorithm-python/ignore/섹션 8/5. 최대 선 연결하기/in5.txt'
sys.stdin=open(input_path, 'rt')
n=int(input())
arr=[int(x) for x in input().split()]
memo=[0]*n
memo[0]=1
for i in range(1,n):
    m=0
    for j in range(i-1,-1,-1):
        if arr[j]<arr[i] and m<memo[j]:
            m=memo[j]
    memo[i]=m+1

print(max(memo))