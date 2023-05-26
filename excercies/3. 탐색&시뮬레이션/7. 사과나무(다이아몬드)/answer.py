'''
사과나무

n*n 격자판
각 격자 안의 자연수를 표현한 2차원 배열 m
다이아몬드 범위 안 자연수의 총합

중간값 x = n/2 + 0.5
중간값과읙 거리를 비교
i의 것보다 작은 j
그 위치의 자연수를 합함
'''

# 0.00294

def makeArr(n):
    return [[int(x) for x in input().split()] for _ in range(n)]
                
def solution(n, m):
    sum=0
    y=0
    x=int(n/2)
    # print(x)
    for i in range(n):
        for j in range(n):
            d=abs(x-j)
            if(d<=y):
                # print("({}, {})".format(str(i), str(j)), end=' ')
                sum+=m[i][j]
        if i<x: y+=1
        else: y-=1
        # print()
    # print('===>', sum)
    return sum




# solution(5, [[10, 13, 10, 12, 15], [12, 39, 30, 23, 11], [11, 25, 50, 53, 15], [19, 27, 29, 37, 27], [19, 13, 30, 13, 19]])