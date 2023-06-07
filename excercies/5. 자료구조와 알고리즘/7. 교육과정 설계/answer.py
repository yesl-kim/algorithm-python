from collections import deque

def solution(n,m):
    res=''
    for s in m:
        if s in n: res+=s
    return 'YES' if res==n else 'NO'

print(solution('CBA', 'CTSBDEA'))
