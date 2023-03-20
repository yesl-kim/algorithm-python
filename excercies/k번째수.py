def solution(n, s,e,k):
    s,e, k=int(s), int(e), int(k)
    a=sorted(n[s-1:e])
    print(a[k-1])

solution([5, 2, 7, 3, 8, 9], 2, 5, 3)
