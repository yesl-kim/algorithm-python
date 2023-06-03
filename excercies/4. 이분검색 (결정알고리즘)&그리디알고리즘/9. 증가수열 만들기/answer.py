from collections import deque

def solution(n):
    n=deque(n)
    end=0
    temp=[]
    res=''
    while n:
        if end<n[0]:
            temp.append((n[0], 'L', n.popleft))
        if len(n)>1 and end<n[-1]:
            temp.append((n[-1], 'R', n.pop))
        if not temp: break
        temp.sort()
        end=temp[0][0]
        res+=temp[0][1]
        temp[0][2]()
        temp=[]
    # else:
    #     if end<n[0]:
    #         res+='L'
    return (len(res), res)
