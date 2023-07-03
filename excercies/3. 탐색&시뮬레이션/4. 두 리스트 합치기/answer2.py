def solution(a,b):
    p1=p2=0
    res=[]
    while p1<=len(a) and p2<=len(b):
        if a[p1]<b[p2]:
            res.append(a[p1])
            p1+=1
        else:
            res.append(b[p2])
            p2+=1
    if p1<len(a):
        res+=a[p1:-1]
    if p2<len(b):
        res+=b[p2:-1]
    return ' '.join([str(x) for x in res])