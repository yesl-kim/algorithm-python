# 리스트와 내장함수 (1)

import random as r

# 리스트 초기화
a = []
b = list()
c = list(range(1, 10))

# 리스트의 결합? +
a = [1, 2]
b = [3,4]
c = a + b
# print(c)

# 삽입
# append = push (js)
a = [1,2,3]
b = a.append(6)
print(a)
print(b) # 반환값 없음

# insert: 특정 인덱스에 요소 삽입
a=[1]
'''
insert는 꼭 두 개의 인자가 필요
b=a.insert(2) <-- 에러남
'''
c = a.insert(1, 3)
# print(a)
# print(c) # insert 함수 반환값은 없

# sum: 요소의 총합

# max, min: 요소 중 최대, 최솟값
a = list(range(1, 11))

'''
print(max(a))
print(min(a))
print(min(3, 5,2,6, 7,8,9))
print(max(3, 5,2,6, 7,8,9))

# random
r.shuffle(a)
print(a)

# sort
a.sort()
print(a)
a.sort(reverse=True)
print(a)

# clear
a.clear()
print(a)
'''

# 더하기, 곱하기
a=[1,2,3]
b=[4,5,6]
print(a+b)
c=a*2
print(c)
del c[1]
print(c)
del c[3:]
print(c)
c.remove(3)
print(c)
# print(c.index(3)) <-- valueError
print(c.index(1))


