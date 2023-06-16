import sys
import time

# 트럭 가용무게 c
# 바둑이의 몸무게 배열 n
path='/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 6/5. 바둑이 승차'
num=5

input_path=path + "/in" + str(num) + ".txt"
sys.stdin=open(input_path, 'rt')
c,N=map(int, input().split())
n=[int(input()) for _ in range(N)]
total=sum(n)
result=0

# ====================

def dfs(i=0, sum=0, tsum=0):
    global result
    global total
    if sum+total-tsum<result: return
    if c<sum: return
    if i==N:
        if result<sum: result=sum
    else:
        dfs(i+1, sum, tsum+n[i])
        dfs(i+1, sum+n[i], tsum+n[i])

# ====================

start=time.time()
dfs()

output_path=path +"/out" + str(num) + ".txt"
sys.stdin=open(output_path, 'rt')
expected=int(input())
if not result==expected: 
        print('answer wrong!')
        print('output: ', result)
        print('expected: ', expected)
else:
    end=time.time()
    print('success!')
    print(f"{end - start:.5f} sec")
