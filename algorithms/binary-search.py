# 참고 https://www.acmicpc.net/blog/view/109

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

