# 씨름선수

> 그리디, O(N)

### 문제

> 씨름 선수의 키(`h`)와 몸무게(`w`)가 주어질 때
>
> n은 N명의 씨름 선수의 키와 몸무게가 적힌 2차원 배열 ([`h`, `w`][])
>
> 다른 씨름 선수보다 키가 크거나, 몸무게가 많이 나가는 선수의 최대 인원을 구하라

## 접근 방식

1. 키를 기준으로 내림차순 정렬
2. 현재 요소보다 앞선 요소의 몸무게 비교
3. 앞선 요소보다 몸무게가 크다면 카운팅

### NOTE

- 앞선 요소와의 몸무게 비교시 아래 코드는 **N 제곱의 시간 복잡도**를 가짐 (앞선 요소와의 몸무게를 모두 비교)

  ```py
  # ❌
   n.sort(reverse=True)
   c=0
   for i in range(len(n)):
      ww=n[i][1]
      for j in range(0,i):
         w=n[j][1]
         if ww<=w: break
      else: c+=1
   return c
  ```

- 최대 몸무게를 구하는 방식과 같은 방법으로 접근하면 O(N)의 시간복잡도로 정답을 구할 수 있다. (최대 몸무게를 갱신할 때마다 카운팅)
