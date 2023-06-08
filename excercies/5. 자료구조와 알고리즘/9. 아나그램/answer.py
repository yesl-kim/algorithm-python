# 0.00336 sec
def solution(n,m):
    temp={}
    for x in n:
        if x in temp:
            temp[x]+=1
        else:
            temp[x]=1
    for x in m:
        if x in temp:
            temp[x]-=1
        else: return 'NO'
    if any(x!=0 for x in temp.values()): return 'NO'
    else: return 'YES'

# print(solution('AbaAeCe', 'baeeACA'))