'''
봉우리

n*n 격자판
회전 명령 정보에 따라 값을 이동시킴
회전 명령 정보 = <행> <방향정보, 0:왼쪽, 1:오른쪽> <회전수>
ex. 2 0 3 -> 2행을 왼쪽으로 3만큼

회전 후 모래시계 모영의 영역에 있는 감의 개수

n
n 줄에 걸쳐 각 줄에 n개의 자연수
회전명령 개수 m
m 줄에 걸쳐 회전명령정보

2차원 배열의 격자판 n
회전명령정보 배열 [i, d, x]
'''

# 0.00426s

def makeArr(n):
    b=[[0]*(n+2)]
    for _ in range(n):
        a=[int(x) for x in input().split()]
        a.insert(0, 0)
        a.append(0)
        b.append(a)
    b.append([0]*(n+2))
    return b

def solution(n):
    c=0
    l=len(n)
    for i in range(1, l-1):
        for j in range(1, l-1):
            x=n[i][j]
            if n[i-1][j] < x and n[i+1][j] < x and n[i][j-1] < x and n[i][j+1] < x: c+=1
    return c
        
    
# a=move([[10, 13, 10, 12, 15], [12, 39, 30, 23, 11], [11, 25, 50, 53, 15], [19, 27, 29, 37, 27], [19, 13, 30, 13, 19]], [2,0,3])
# a=move(a, [5, 1, 2])
# a=move(a, [3, 1, 4])
# print(count(a))
# print(solution([[0, 0, 0, 0, 0, 0], [0, 5, 3, 7, 2, 3, 0], [0, 3, 7, 1, 6, 1, 0], [0, 7, 2, 5, 3, 4, 0], [0, 4, 3, 6, 4, 1, 0], [0, 8, 7, 3, 5, 2, 0], [0, 0, 0, 0, 0, 0]]))