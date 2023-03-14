a=1
A = 2
c=5
A1 = 3
_b = 4
print(a, A, A1, _b)
a, b, c=3, 2, 1
print(a, b, c)

# 값 교환
a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)

# 변수 타입
a = 12345
print(type(a))
a=12.123456789123456789
print(type(a))

a='12345'
print(type(a))

# 출력방식
print("number")
a, b, c = 1, 2, 3
# sep를 통해 값 사이 출력을 어떻게 할지 지정할 수 있음
print(a, b, c, sep=", ")
print(a, b, c, sep='\n')
# end를 통해
print(a, end='-')
print(b)

# 변수입력과 연산자
'''
a=input("숫자를 입력하세요")
print(a)
input을 통해 전달받은 값은 문자열 타입
'''
a, b=map(int, input("숫자 입력해라").split(" "))
print(a+b)
# 몫 연산자
print(a//b)
print(a%b)
# 거듭제곱 ex. a의 b제곱
print(a**b)

