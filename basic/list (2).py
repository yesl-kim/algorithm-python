# 리스트와 내장함수 (2)

# slice는 원본배열을 건드리지 않고 slice된 요소를 반환 
a=[10, 20, 30, 12, 31, 55]
b=a[:3]
c=a[1:4]
#print(a)
#print(b)
#print(c)

# pop은 원본배열에서 요소를 제거하여 제거된 요소를 반환 
c = a.pop()

# list length과 순회
for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    print(x, end=' ')
print()

# list 순회: 튜플
for x in enumerate(a):
    print('x[', x[0], '] = ', x[1], sep='')

for i, v in enumerate(a):
    print('x[', i, '] = ', v, sep='')

# all, any
if all(x>=10 for x in a):
    print('yes')
else:
    print('no')

if any(50<x for x in a):
    print('yes')
else:
    print('no')


# ===
# 투플
a =(1, 2, 3, 4, 5)
print(a)
print(a[0])
# a[0] = 7 <-- error! 튜플은 값을 변경할 수 없다
