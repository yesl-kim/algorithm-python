# 반복문
'''
range(a)
- 0부터 a까지의 정수 리스트를 만드는 함수 (a는 포함하지 않음)

range(a, b)
- a 부터 b까지의 정수 리스트를 만드는 함수 (b는 포함하지 않음)

a=range(10)
b=range(1, 10)
for i in a:
    print(i, "in a")
for i in b:
    print(i, "in b")

range(a, b, c)
- a 부터 b까지의 정수 배열을
- c의 규칙으로 만드는 함수

for i in range(10, 0, -2):
    print(i)

# while
i=1
while i<=10:
    print(i)
    i=i+1

# break
i=10
while i>0:
    print(i)
    if i==5:
        break
    i-=1

# continue
for i in range(1, 11):
    if i%2 == 1:
        continue
    print(i)

# for ... else
- for문이 중간에 중단없이 (ex. break) 모두 순회하고 난 다음에
- else문이 실행된다
for i in range(1, 11):
    # if i > 5:
    #if i > 15:
     #   break
    if i%2==0:
        continue
    print(i)
else:
    print('끝!')

'''




