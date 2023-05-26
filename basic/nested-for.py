# 중첩 반복문

# 구구단
for i in range(10):
    for j in range(1, 5):
        if i == 0:
            print(j, '단', sep='', end='          ')
        else:
            print(j, 'x', i, '=', j*i, end='   ')
    print()
        

# 별찍기
'''
for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end= ' ')
    print()
'''

# OR
'''
for i in range(5):
    for j in range(i+1):
        print('*', end=' ')
    print()
'''

'''
for i in range(5, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()
'''

# OR
'''
for i in range(5):
    for j in range(5-i):
        print("*", end=' ')
    print()
'''
