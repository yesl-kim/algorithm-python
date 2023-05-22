'''
곳감 (모래시계)

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

# 0.00294

def makeArr(n):
    return [[int(x) for x in input().split()] for _ in range(n)]

# 곳감 이동시키기                
def move(n, m):
    i,d,x=m
    l=len(n)
    a=[None]*l
    for j in range(l):
        p=(j-x)%l if d==0 else (j+x)%l
        a[p]=n[i-1][j]
    n[i-1]=a
    return n

# 곳감 개수 세기
def count(n): 
    sum=p=0
    m=int(len(n)/2)
    for i in range(len(n)):
        for j in range(p, len(n)-p):
            sum+=n[i][j]
        if i<m: p+=1
        else: p-=1
    return sum
        
    

a=move([[10, 13, 10, 12, 15], [12, 39, 30, 23, 11], [11, 25, 50, 53, 15], [19, 27, 29, 37, 27], [19, 13, 30, 13, 19]], [2,0,3])
a=move(a, [5, 1, 2])
a=move(a, [3, 1, 4])
print(count(a))