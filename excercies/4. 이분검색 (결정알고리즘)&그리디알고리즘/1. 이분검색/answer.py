'''
1. n 오름차순 정렬
2. 이진탐색으로 m이 n의 몇번째인지 출력
'''

# 0.00511 s

def isLow(n, v): return lambda i: v <= n[i]

def solution(n, m):
    n.sort()
    lo,hi=0,len(n)-1
    check=isLow(n, m)
    while lo+1<hi:
        mid=int((lo+hi)/2)
        if check(mid)==check(lo): lo=mid
        else: hi=mid
    return lo+1 if check(lo) else hi+1


