from collections import deque

def solution(n,m):
    res=''
    for s in m:
        if s in n: res+=s
    return 'YES' if res==n else 'NO'

# => 반례: 필수 과목을 여러번 이수할 경우

def solution2(n,m):
    n=deque(n)
    for x in m:
        if x in n and x!=n.popleft(): return 'NO'
    else:
        if len(n)>0: return 'NO'
    return 'YES'

print(solution2('AFC', 'AFFDCCFF'))
