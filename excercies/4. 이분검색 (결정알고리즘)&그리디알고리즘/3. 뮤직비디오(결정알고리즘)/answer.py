'''
N곡의 노래 길이가 담긴 배열 n
N개의 노래를 m개의 DVD에 나눠서 녹화
DVD의 최소 크기 v

=> 0.00273 sec
'''

# m 크기의 DVD에 노래 n을 녹화할 때 필요한 DVD의 개수
def count(n, v):
    # DVD는 1부터 시작한다.
    c=1
    sum=0
    for x in n:
        sum+=x
        if v<sum:
            c+=1
            # v(DVD 용량)은 어떤 노래의 크기보다 크다는 것을 가정한다.
            sum=x
    return c

def solution(n, m):
    lt=0
    rt=sum(n)
    maxx=max(n)
    while lt<=rt:
        mid=(lt+rt)//2
        if maxx<=mid and count(n, mid)<=m:
            res=mid
            rt=mid-1
        else:
            lt=mid+1
    return res

print(solution(list(range(1,10)),9))
# print(count(list(range(1,10)), 24))