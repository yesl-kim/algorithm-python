'''
일렬로 상자가 쌓여있을 때
각 열의 쌓여진 상자 개수 배열 n
상자 이동 회수 m

0.00286 sec
'''

def solution(n, m):
    l=len(n)-1
    for _ in range(m):
        n.sort()
        n[0]+=1
        n[l]-=1
    n.sort()
    return n[l]-n[0]


print(solution([69, 42, 68, 76, 40, 87, 14, 65, 76, 81], 50))