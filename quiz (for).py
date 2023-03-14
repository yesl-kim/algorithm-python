# 반복문을 통한 문제풀이
# 1부터 N까지 홀수출력

# 함수선언 키워드: def
def odd(n):
    for i in range(1, n+1):
        if i%2 == 1:
            print(i)
q1 = int(input('1. 1부터 n까지의 홀수 출력: '))
odd(q1)


# 1부터 N까지의 합 구하기
def sum(n):
    a = 0
    for i in range(1, n+1):
        a += i
    return a
q2 = int(input('2. 1부터 N까지의 합 구하기: '))
print(sum(q2))


# N의 약수 출력
def getDivisor(n):
    a = []
    for i in range(1, n+1):
        if n % i == 0:
            a.append(i)
    return a
q3 = int(input('3. N의 약수 출력: '))
print(getDivisor(q3))
            
