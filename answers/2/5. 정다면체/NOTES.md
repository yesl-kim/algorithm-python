## 딕셔너리 자료형

```py
a={1: 'a'}
a[2]='b'

del a[1]

a.keys()
# dict_keys([2])

a.values()
# dict_values(['b'])

a.items()
# dict_items([(2, 'b')])

a.clear()
# {}

a.get(2)
# = a[2]
# 'b'

# default 값 정하기
# key 3에 해당하는 값이 없을 경우 0 반환
# !기본값이 a 에 추가되지는 않음
a.get(3, 0)
# 0

# 해당 key의 존재여부 확인
2 in a
# True
3 in a
# False

```
