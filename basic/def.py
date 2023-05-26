# ㅎㅏ함ㅁㅅㅜ수 ㅁㅁㅁㅁㅏㄴ만ㄷㅡㄹ들ㄱㅣ기

'''
def add(a, b):
    return a + b

print(add(1, 3))

# 함수 호출 전에 정의를 먼저 해줘야함

def add(a, b):
    c=a+b
    d=a-b
    return c, d

print(add(3,2))
# 함수는 여러개의 값을 리턴할 수도 있다 => 이럴 경우 투플 형태로 반환
'''

def isPrime(x):
    for i in range(2, x):
        if x%i == 0:
            return False
    return True


# filter
a = [25, 13, 7, 9, 19]
print(list(filter(isPrime,a)))
print('tuple', tuple(filter(isPrime,a)))

# list comprehension - filtering
print([num for num in a if isPrime(num)])
print(tuple(num for num in a if isPrime(num)))
