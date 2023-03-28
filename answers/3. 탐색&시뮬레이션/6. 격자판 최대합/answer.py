'''
격자판 최대합

n*n 격자판
2차원 배열 m

-> m[행][열]
-> 각 행의 합, 각 열의 합, 두 대각선의 합 중 가장 큰 합 출력
'''

# 0.0302 s

def makeArr(n):
    return [[int(x) for x in input().split()] for _ in range(n)]
                
def solution(n, m):
    hs=[]
    vs=[0]*n
    x=0
    y=0
    for i in range(n):
        # i는 행번호
        h=0
        mi=m[i]
        r=n-i-1
        mr=m[r]
        for j in range(n):
            # j는 열번호
            h+=mi[j]
            vs[j]+=mi[j]
            if i == j:
                x+=mi[j]
            if r == j:
                y+=mr[j]
        else: 
            hs.append(h)
    # print(max(hs+vs+[x, y]))
    return max(hs+vs+[x, y])


# solution(5, [[10, 13, 10, 12, 15], [12, 39, 30, 23, 11], [11, 25, 50, 53, 15], [19, 27, 29, 37, 27], [19, 13, 30, 13, 19]])
    
'''
오름차순 대각선 x
0,0
1,1
2,2
3,3
4,4

내림차순 대각선 y
4,4
3,3
2,2
1,1
0,0
'''