'''
1. n 오름차순 정렬
2. 이진탐색으로 m이 n의 몇번째인지 출력
'''

def isLow(n,v): return lambda i: v<=n[i]

def solution(n, m):
    n.sort()
    lo,hi=0,len(n)
    check=isLow(n,m)
    while lo+1<hi:
        mid=int((lo+hi)/2)
        if check(lo)==check(mid):
            lo=mid
        else:
            hi=mid
        continue
    # lo+1=hi
    # = lo 다음칸이 바로 hi
    # 답은 lo or hi
    return lo if check(lo) else hi



# print(solution(['level', 'soon', 'gooG', 'moon']))
# solution('0 1 0 0 1 0 1 1 0 0')

