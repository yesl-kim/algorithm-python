# 인접행렬

### 시행착오

**2차원 리스트 초기화**

```py
N=6
# trial
graph=[[0]*N]*N

# solution
graph=[[0]*N for _ in range(N)]
```

- 첫 시도한대로 하면, 각 행의 리스트는 모두 같은 리스트를 가리키게 된다. (결국 같은 값)
- 때문에 한 행의 요소를 수정하면, 나머지 모든 행의 동일한 위치의 요소가 수정된다.

  ```py
  graph[0][1]=7
  print(graph)

  '''
  [
    [0, 7, 0, 0, 0, 0],
    [0, 7, 0, 0, 0, 0],
    [0, 7, 0, 0, 0, 0],
    [0, 7, 0, 0, 0, 0],
    [0, 7, 0, 0, 0, 0],
    [0, 7, 0, 0, 0, 0]
  ]
  '''
  ```
