# closest dessert cost

> DFS

## 오답노트

### 전역변수 참조 문제

> 첫 코드

```py
class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        res=float('inf') # <-- res 변수 선언
        def dfs(L,sum):
            global res # <-- res 변수 접근
            #...
            # res=x <-- * 할당시 참조 에러 발생! *
        return res
```

- 최종 답이 될 res 변수를 함수 내에서 초기화, 내부 dfs 함수 내에서 참조하기 위해 global 키워드를 사용했다.
- 상위 함수는 클래스로 선언되었기 때문에 res는 전역변수가 아니다 -> 내부함수에서 참조 에러 발생

> 수정된 코드

```py
res=float('inf') # <-- 전역변수로 지정
class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        def dfs(L,sum):
            global res # <-- 전역변수 참조. 서로 다른 케이스끼리 영향을 주게 되어 오답
            #...
        return res
```

- res 변수를 전역변수로 선언하고 내부함수에서 전역변수를 참조했다.
- 하지만 그럴 경우 다른 케이스끼리도 영향을 주게 되어 오답이 발생했다.
  - ex. 1번 문제의 답이 2번 문제 답에 영향을 주게 됨

> 최종 수정 코드

```py
class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        global res # <-- 전역변수 선언
        res=float('inf') # <-- 초기화
        def dfs(L,sum):
            global res # <-- 전역변수 참조
            #...
        return res
```

- res는 전역변수이되, class 내에서 res를 초기화시켜주었다.
