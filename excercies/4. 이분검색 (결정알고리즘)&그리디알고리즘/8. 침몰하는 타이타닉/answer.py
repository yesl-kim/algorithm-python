'''
N명의 승객
N개의 몸무게 수열 n

한 구명보트의 
최대 가용 인원: 2
최대 가용 무게: m

(단 각 승객의 몸무게는 m을 넘지 않는다. = 구명보트를 타지 못하는 승객은 없다.)

=> 모든 승객이 탈출하기 위해 필요한 구명보트의 최소 개수
'''

from collections import deque

# 0.00327 sec
def solution(n, m):
    n.sort(reverse=True)
    c=0
    lt=0
    rt=len(n)-1
    while lt<rt:
        if n[lt]+n[rt] <=m:
            lt+=1
            rt-=1
        else:
            lt+=1
        c+=1
    if lt==rt: c+=1
    return c

# 정답 풀이
# 0.00290 sec
def solution2(n, m):
    n.sort()
    n=deque(n)
    c=0
    while n:
        if len(n)==1:
            c+=1
            break
        if n[0]+n[-1]>m:
            n.pop()
            c+=1
        else:
            n.pop()
            n.popleft()
            c+=1
    return c

print(solution([90, 50, 70, 100, 60], 140))