시행착오

```py
x=y=[]
x.append(1)
x # [1]
y # [1]

x=[]
y=[]
x.append(1)
x # [1]
y # []
```

### 정답풀이

#### slice 사용해서 배열 reverse 시키기

```py
a=[1,2,3]
a[::-1]
```

#### 7\*7 격자판에서 5자리수 확인하기

```py
for i in range(3):
    for j in range(7):
        n[j][i:i+5]
```

- slice 사용
- 모든 행,열 요소를 순회할 필요없음
