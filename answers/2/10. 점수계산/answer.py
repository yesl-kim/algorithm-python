'''
ox 문제의 점수계산

채점 문자열 n

맞으면 1, 틀리면 0
연속 정답인경우 가산점
가산점까지 합한 총 점수 출력
'''

def solution(n):
    score=0
    sum=0
    c=0
    n=list(map(int, n.split()))
    for x in n:
        if x==1:
            c+=1
            sum+=x*c
            # print('맞앗다', c, sum)
        else:
            score+=sum
            c=0
            sum=0
            # print('틀렸다', score)
    else:
        score+=sum
    return str(score)

# print(solution('0 0 0 0 0 0 1 0 0 1 0 0 0 1 0 0 0 1 1 1'))
# solution('0 1 0 0 1 0 1 1 0 0')

