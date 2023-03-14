# 문자열과 내장함수
msg = 'It is Time'
# upper, lower
temp = msg.upper()

# find: 첫 요소의 인덱스 반환
print(temp.find('T')) # 1

# count: 해당 요소의 개수 반환
print(temp.count('T')) # 2

# len: 길이반환
print(len(msg))
'''
for i in range(len(msg)):
    print(msg[i])
'''

# slice: a부터 b까지의 문자열 반환 (b 인덱스의 문자열은 미포함)
print(msg[3:5])

# 예제
for x in msg:
    #if x.isupper():
    if x.islower():
        print(x, end=' ')
print()

# isalpha: 공백제외, 알파벳인지 여부
a='123 adf ㅊㅇㄴ'
for x in a:
    if x.isalpha:
        print(x, end='')
print()

# ord: 문자열의 아즈키넘버를 반환
temp='AF'
for x in temp:
    print(ord(x))

#chr: 아즈키넘버를 문자열로 반환
num = 66
print(chr(num))
