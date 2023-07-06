import sys
import time

path='/Users/yesl.k/Dev/coding_test/algorithm-python/ignore/섹션 8/6. 가장 높은 탑 쌓기(LIS 응용)/in4.txt'
sys.stdin=open(path, 'rt')
start=time.time()

n=int(input())
bs=[tuple(map(int, input().split())) for _ in range(n)] # (넓이, 높이, 무게)
bs.sort(key=lambda x: x[0], reverse=True)
memo=[0]*n
memo[0]=res=bs[0][1]

for i in range(1,n):
    mm=0
    for j in range(i-1,-1,-1):
        if bs[i][2]<bs[j][2] and mm<memo[j]:
            mm=memo[j]
    memo[i]=mm+bs[i][1]
    if res<memo[i]:
        res=memo[i]

print(res)
# print(memo)
end=time.time()
print(f"{end - start:.5f} sec")