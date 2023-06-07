# 응급실

TODO

## TIP

### enumarate: iterable에서 요소와 인덱스를 함께 얻고 싶을 때

> for index, value in enumerate(<iterable>)

- iterable 객체를 순회하며 요소의 index도 필요한 경우 사용할 수 있다.
- enumerate는 순회가능한 객체를 받아 각 요소의 인덱스와 값을 튜플 형태의 요소로 하는 iterator 객체를 반환해주는 함수이다
- 순회하면서 직접 index 값을 계산해줘도 되지만 (아래코드처럼) 이럴 경우 순회가 끝나도 i 변수가 네임스페이스에 남아있기 때문에 이상적이지 않다
  ```py
  i=0
  for x in [1,2,3]:
    print(i, x)
    i+=1
  ```
- 또 다른 방법으로 순회할 목록의 길이만큼 range를 만든 뒤, index값으로 요소 값에 접근하는 방식~~은 파이썬답지 않다~~
  ```py
  a=[1,2,3]
  for i in range(len(a)):
    print(i, a[i])
  ```

### any

> any(<iterable>)

- 인자로 받은 이터러블한 객체의 요소 중에 하나라도 True인 게 있으면 `True`, 아니면 `False` 반환

```py
any([True, False, False]) # True
any([False, False, False]) # False

temp=[1,3,6,2]
any(cur<num for num in temp) # True

# 예제 문제
a=[(0, 60), (1, 60), (2, 90), (3, 60), (4, 60), (5, 60)]
x=a.pop()
any(y[1]>x[1] for y in a) # True
```

### all

> all(<iterable>)

```py
all([True, False, True]) # False
all([True, True, True]) # True
```

- 인자로 받은 이터러블한 객체의 요소가 모두 True이면 `True`, 아니면 `False` 반환
