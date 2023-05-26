# ㅏㄹ람ㅁㄷㅏ다하ㅎㅏ함ㅁㅅㅜ수
# = 익명함수 = 함수표현식
# lt's like arrow function

def plus_one(x):
    return x+1

print(plus_one(2))

plus_two = lambda x: x+2

print(plus_two(1))

# 함수의 인자로 사용될 때 유용
a=[1,2,3]
print(list(map(lambda x:x*x, a)))
