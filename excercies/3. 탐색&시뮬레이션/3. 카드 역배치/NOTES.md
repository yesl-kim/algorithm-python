## 얕은 복사와 깊은 복사

- 파이썬에서는 list, set, dict 타입은 mutable한 타입
- 자바스크립트의 참조형 타입과 같은 원리이다

### 앝은 복사: 슬라이싱

```py
a=[1,2,3]
b=a[:]
```

- list의 슬라이싱은 새로운 list를 반환한다

### 얕은 복사: copy 모듈

```py
import copy
a=[1,2,3]
b=copy.copy(a)
```

### 깊은 복사: copy 모듈

```py
import copy
a=[[1,2], [3,4]]
b=copy.deepcopy(a)
a[1].append(5)
a # [[1,2], [3,4,5]]
b # [[1,2], [3,4]]
```
