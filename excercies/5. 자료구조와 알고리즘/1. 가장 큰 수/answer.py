# n: number[]
# m: number

# 0.00340 sec
def solution(n, m):
    res=[]
    i=0
    # 뒤에 몇자리수가 와야하는지
    # 총 만들어야 하는 자릿수 - 1
    # x=len(n)-m-1
    # range(i, len(n)-x)
    while(m<len(n)):
        large=0
        for j in range(i, m+1):
            if large<n[j]:
                large=n[j]
                i=j+1
        res.append(large)
        m+=1
    return "".join([str(x) for x in res])

def solution2(n, m):
    res=[]
    for x in n:
        while res and m>0:
            if res[-1]<x:
                res.pop()
                m-=1
            else: break
        res.append(x)
    if m>0: res=res[:-m]
    return res

a=[int(x) for x in list('9977252641')]
print(solution(a, 5))
print(solution2(a, 5))