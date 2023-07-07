import sys

path='/Users/kim-yeseul/Documents/dev/algorithm/algorithm-python/ignore/exercise/섹션 8/9. 가방문제/in5.txt'
sys.stdin=open(path,'rt')

n,limit=map(int,input().split())
js=[tuple(map(int,input().split())) for _ in range(n)]
js.sort(key=lambda j: (-j[1], j[0]))
res=0

def solution(L=0,remain=limit,sum=0):
    global res
    if L==n:
        res=max(res,sum)
    else:
        m=remain//js[L][0]
        for i in range(m,-1,-1):
            solution(L+1,remain-js[L][0]*i,sum+js[L][1]*i)

solution()
print(res)