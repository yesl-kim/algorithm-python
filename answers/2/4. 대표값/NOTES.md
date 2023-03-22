## 평균값 구하기

1. sum 함수

```py
n=[2,3,4]
sum(n)/len(n)
```

2. statistics 모듈 사용

```py
n=[2,3,4]
statistics.mean(n)
```

## 올림, 내림, 반올림

- math를 import 하여 사용

### 내림

- trunc vs floor
  ```py
  math.trunc(-3.14)   #결과는 -3
  math.floor(-3.14)   #결과는 -4
  ```
- trunc는 0을 향해 내림, floor는 그냥 내림

### 반올림: round()

- 반올림할 자리의 수가 5이면 반올림 할 때 앞자리의 숫자가 짝수면 내림하고 홀수면 올림 한다.

  ```py
  round(3.5) # 4
  round(4.5) # 4

  # 반올림의 다른 방법
  # ave는 평균
  ave=ave+0.5
  ave=int(ave)
  ```

## 질문

### 파이썬은 scope

- javascript에서 var 개념과 비슷하다. 함수 레벨을 따른다
- 변수를 찾는 우선순위는 Local -> Enclosed -> Global -> Built-in

- [ ] 문제풀이 보기
