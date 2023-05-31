'''
K개의 랜선의 길이가 담긴 k,
K개의 랜선으로
n개의 랜선을 만들 수 있는 랜선 최대 길이
'''

# 

def __check(k, n): return lambda v: n <= sum([x//v for x in k])
    

def solution(k, n):
    lo,hi=0,max(k)
    check=__check(k, n)
    while lo<=hi:
        mid=(lo+hi)//2
        if check(mid): 
            res=mid
            # 정답은 될 수 있으나
            # n개의 랜선을 얻을 수 있는
            # 랜선 최대길이를 찾기 위해
            # 더 긴 길이도 확인한다.
            lo=mid+1
        else:
            hi=mid-1
    return max(res)
            


