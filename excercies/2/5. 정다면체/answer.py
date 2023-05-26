'''
정 n면체, 정 m면체의 주사위
나올수 있는 눈의 합 중 가장 확률이 높은 숫자
여러개일 경우 오름차순

1. 모든 눈의 합 계산 -> {숫자: 횟수}
2. 가장 높은 횟수 조회 -> b=max(list(a.values))
3. b와 횟수가 같은 숫자를 찾아서 리턴
'''
def solution(n, m):
    a={}
    for i in range(1, n+1):
        for j in range(1, m+1):
            sum=i+j
            a[sum]=a.get(sum, 0)+1
    b=max(list(a.values()))
    s=[]
    for x, y in list(a.items()):
        if y==b:
            s.append(str(x))
    return " ".join(s)

# solution(4, 6)
