import sys
import time

path='/Users/kim-yeseul/Documents/dev/algorithm/algorithm-python/ignore/exercise/섹션 8/9. 가방문제/in5.txt'
sys.stdin=open(path,'rt')

start=time.time()
n,limit=map(int,input().split())
dy=[0]*(limit+1)

for _ in range(n):
    w,v=map(int,input().split())
    for i in range(w,limit+1):
        dy[i]=max(dy[i],dy[i-w]+v)

print(dy[limit])
end=time.time()
print(f"{end - start:.5f} sec")
