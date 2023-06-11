# 최대힙

### TIP: 파이썬 내장 모듈 heapq를 사용하여 최대힙을 구현하는 방법

- 값을 넣고 뺄 때 `-`부호를 붙여 활용할 수 있다.

  ```py
  import heapq

  a=[5, 3, 2, 1, 4, 6, 7]
  h=[]
  for x in a:
    heapq.heappush(h, -x)
  print(h) # [-7, -4, -6, -1, -3, -2, -5]
  while h:
    print(-heapq.heappop(h)) # 7 6 5 4 3 2 1
  ```
