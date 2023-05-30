# 참고 https://www.acmicpc.net/blog/view/109

def isLow(n,v): return lambda i: v<=n[i]

def binarySearch2(n, m):
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


# 참고 | 인프런 "파이썬 알고리즘 문제풀이 입문 강의"
def binarySearch(n, m):
    lt,rt=0,len(n)-1
    while lt<=rt:
        mid=(lt+rt)//2
        if n[mid]==m: return mid+1
        elif m<n[mid]: rt=mid-1
        else: lt=mid+1

a=[23, 87, 65, 12, 57, 32, 99, 81]
a.sort()
print(binarySearch(a, 32))