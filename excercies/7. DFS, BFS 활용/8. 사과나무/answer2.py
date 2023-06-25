import sys
import time
from collections import deque

start=time.time()
input_path='/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 7/8. 사과나무/in1.txt'
sys.stdin=open(input_path, 'rt')
N=int(input())
g=[[int(x) for x in input().split()] for _ in range(N)]
mid=N//2

apple=deque([])
apple.append((mid, mid))
res,g[mid][mid]=g[mid][mid],None
L=0

# while L<N:
#     x,y=apple.popleft()
#     for i,j in ((x+1,y),(x-1, y),(x, y+1),(x,y-1)):
#         if 0<=i<N and 0<=j<N and g[i][j]!=None:
#             apple.append((i,j))
#             res+=g[i][j]
#             g[i][j]=None
#     L+=1

while True:
    if L==mid:
        break
    for _ in range(len(apple)):
        x,y=apple.popleft()
        for i,j in ((x+1,y),(x-1, y),(x, y+1),(x,y-1)):
            if 0<=i<N and 0<=j<N and g[i][j]!=None:
                apple.append((i,j))
                res+=g[i][j]
                g[i][j]=None
    L+=1
        

print(res)
print(g)
end=time.time()
print(f"{end - start:.5f} sec")
