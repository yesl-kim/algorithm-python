import sys
import time

# 트럭 가용무게 c
# 바둑이의 몸무게 배열 n
path='/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 6/7. 동전교환'
num=5

input_path=path + "/in" + str(num) + ".txt"
sys.stdin=open(input_path, 'rt')
N=int(input())
n=[int(x) for x in input().split()]
n.sort(reverse=True)
total=int(input())
res=float('inf')
# ====================

def dfs(L=0, sum=total):
    global res
    if L>=res or sum<0: return
    if sum==0:
        if res>L: res=L
    else:
        for x in n:
            if sum-x<0: continue
            dfs(L+1, sum-x)
        
    

# ====================

start=time.time()
dfs()

output_path=path +"/out" + str(num) + ".txt"
sys.stdin=open(output_path, 'rt')
expected=int(input())
if not res==expected: 
        print('answer wrong!')
        print('output: ', res)
        print('expected: ', expected)
else:
    end=time.time()
    print('success!')
    print(f"{end - start:.5f} sec")