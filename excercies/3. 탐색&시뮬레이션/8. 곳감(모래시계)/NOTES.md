**삼항 연산자**

> <참일 때의 값> if <조건문> else <거짓일 때의 값>

d == 0, 왼쪽으로
d == 1, 오른쪽으로
x만큼 이동

```py
p=(j-x)%l if d==0 else (j+x)%l
```

### 회전

**왼쪽으로 k칸 이동**

```py
for _ in range(k):
  a[h-1].append(a[h-1].pop(0))
```

- pop(<index>): <index> 위치의 요소를 배열에서 제거하고 반환
- <index>가 주어지지 않을경우 가장 마지막 요소를 끄집어 낸 후 반환
- pop한 요소의 자리는 뒤의 요소가 알아서 자리를 채움 (이동)

**오른쪽으로 k칸 이동**

```py
for _ in range(k):
  a[h-1].insert(0, a[h-1].pop())
```

- insert(<index>, <value>): <index> 위치에 <value>를 집어넣음
