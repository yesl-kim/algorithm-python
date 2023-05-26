

'''
== 같니?
!= 다르니?
>= 크거나 같다

x=7
if x==7:
    print("lucky")
    # print("ddd") if 문 안의 실행문은 들여쓰기를 맞춰줘야한다.

if 10<=x:
    if x%2 == 1:
        print("10이상의 홀수")

and (= &&)

x=7
if x>0 and x<10:
    print("10보다 작은 자연수")

비교 연산자를 연이어 작성할 수도 있음
if 0<x<10:
    print("10보다 작은 자연수")

if, else (분기)

if, elif, else


'''
x=11
if x%2 == 0:
    print("양수")
else:
    print("음수")

x=85
if x>= 90:
    print("A")
elif x>=80:
    print("B")
elif x>=70:
    print("C")
elif x>=60:
    print("D")
else:
    print("F")
    
