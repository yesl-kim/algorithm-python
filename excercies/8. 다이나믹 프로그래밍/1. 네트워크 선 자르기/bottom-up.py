import sys

input_path='/Users/yesl.k/Dev/coding_test/algorithm-python/ignore/섹션 8/1, 2. 네트워크 선 자르기/in2.txt'
sys.stdin=open(input_path, 'rt')

N=int(input())

# dy[n]=f(n)
dy=[0]*(N+1)
dy[0]=0
dy[1]=1
dy[2]=2

for i in range(3,N+1):
    dy[i]=dy[i-1]+dy[i-2]
print(dy[N])