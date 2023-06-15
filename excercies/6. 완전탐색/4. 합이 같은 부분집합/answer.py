import sys

def solution(n):
    total=sum(n)
    def dfs(i=0, sum=0):
        if i==len(n):
            if sum==total-sum:
                print('YES')
                sys.exit(0)
        else: 
            dfs(i+1, sum+n[i])
            dfs(i+1,sum)
    dfs()
    # 종료되지 않고 dfs함수가 마치면 
    # 'YES'인 경우가 없는 것이므로 NO를 출력
    print('NO')


solution([1,3,5,6])