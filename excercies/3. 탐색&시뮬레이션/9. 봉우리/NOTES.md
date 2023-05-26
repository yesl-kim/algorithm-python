### all 함수

2차원 배열에서 현재 위치 요소의 값과 상하좌우의 값을 비교하는 코드

- 내가 작성한 코드

```py
x=n[i][j]
if n[i-1][j] < x and n[i+1][j] < x and n[i][j-1] < x and n[i][j+1] < x:
```

- 답안

```py
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
```
