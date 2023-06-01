'''

c마리의 말을 N개의 마구간에 배치했을 때
가장 가까운 두 말의 거리가 최대가 되는 값

n은 N개의 마구간 좌표 배열
모두 일직선상에 존재함

=> 0.01919 sec
'''

# 거리 d
# n은 정렬된 배열이라 가정
# 최소한 거리 d만큼 말을 놓았을 때
# 놓을 수 있는 말의 수
def count(n, d):
    c=1
    p=n[0]
    for x in n:
        if d<=x-p:
            c+=1
            p=x
    return c

# 말의 거리와 놓을 수 있는 말의 수는 반비례
# 최대 길이를 구하기 위해 lt 이동
def solution(n, c):
    lt=1
    rt=max(n)-min(n)
    while lt<=rt:
        mid=(lt+rt)//2
        if c<=count(n, mid):
            res=mid
            lt=mid+1
        else:
            rt=mid-1
    return res
