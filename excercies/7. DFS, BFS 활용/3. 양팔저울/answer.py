import sys
import time

start=time.time()
input_path='/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 7/3. 양팔저울/in5.txt'
sys.stdin=open(input_path, 'rt')
N=int(input())
n=[int(x) for x in input().split()]
ch=[0]*(sum(n)+1)
ch[0]=1
# print(n)

# L=추의 무게
def dfs(L=0, sum=0):
    if L==N:
        if sum>0:
            ch[sum]=1
    else:
        dfs(L+1,sum)
        dfs(L+1,sum+n[L])
        dfs(L+1,sum-n[L])

dfs()
print(len([x for x in ch if x==0]))
end=time.time()
print(f"{end - start:.5f} sec")