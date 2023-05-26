'''
카드역배치

1~20까지 오름차순으로 적힌 20장의 카드
주어진 구간의 카드를 역순으로 재배치

reverse(a, b, n)
숫자 배열 n
구간 a, b (1 <= a <= b <= 20)
n[a:b+1]까지의 구간을 역순으로 재배치
'''

def solution(a, b, n):
    a=a-1
    b=b-1
    m=n[:]
    for i in range(b-a+1):
        m[a+i]=n[b-i]
    return m


# print(solution('0 0 0 0 0 0 1 0 0 1 0 0 0 1 0 0 0 1 1 1'))
# solution('0 1 0 0 1 0 1 1 0 0')
