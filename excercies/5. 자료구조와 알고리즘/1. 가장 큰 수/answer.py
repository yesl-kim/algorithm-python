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
        temp=n[i:m+1]
        large=max(temp)
        res.append(large)
        i+=temp.index(large)+1
        m+=1
    return res
    # return "".join([str(x) for x in res])

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