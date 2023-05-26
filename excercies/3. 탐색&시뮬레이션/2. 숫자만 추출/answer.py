'''
숫자만 추출

1. 문자열 중 숫자만 추출하여 순서대로 자연수 생성
2. 자연수와 그 수의 약수 개수 반환
'''

def solution(n):
    a= [s for s in n if s.isdigit()]
    a=int("".join(a))
    count=0
    for x in range(1, a+1):
        if a%x == 0:
            count+=1
    return '{}\n{}'.format(a, count)
# print(solution('0 0 0 0 0 0 1 0 0 1 0 0 0 1 0 0 0 1 1 1'))
# solution('0 1 0 0 1 0 1 1 0 0')
# print(solution('g0en2Ts8eSoft'))

