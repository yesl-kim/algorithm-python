import sys
import time
from collections import deque

start=time.time()
input_path='/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 7/7. 송아지 찾기/in5.txt'
sys.stdin=open(input_path, 'rt')
S,E=map(int, input().split())

MAX=10000
jump=[0]*(MAX*2)
ch=[0]*(MAX*2)
ch[S]=1

d=deque([])
d.append(S)

# ======
while d:
    now=d.popleft()
    if now==E:
        break
    for next in (now+5, now+1, now-1):
        if 0<next<=MAX and ch[next]==0:
            d.append(next)
            jump[next]=jump[now]+1
            ch[next]=1
        
# ======

print(jump[E])
end=time.time()
print(f"{end - start:.5f} sec")