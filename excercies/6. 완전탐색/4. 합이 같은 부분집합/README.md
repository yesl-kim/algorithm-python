# 합이 같은 부분집합

TODO

## 접근방식

- 부분집합을 만드는 방식과 동일
- 두 부분집합은 서로소 관계이며, 결국 구하는 것은 각 부분집합의 **총합**이 서로 같은지를 구하는 것이기 때문에
- 하나의 부분집합 a의 총합(sum)을 바로 구하고 원본 집합의 총합(total)과 sum과의 차를 통해 다른 부분집합의 총합을 구한다

### TIP

**스택에 쌓인 함수들을 모두 완료하지 않고 바로 끝내버리는 방법**

```
sys.exit(0)
```

- `sys.exit(0)`: 프로그램이 정상적으로 종료
- `sys.exit(1)`: 프로그램이 비정상적으로 종료
- 인자로 0,1만 줄 수 있는 것은 아님

**timeout 방지: 예외케이스 생각하기**

- 해당문제에서
- sum이 total의 절반값을 넘어가는 경우 더 진행하지 않고 종료해도 무방
- \*단 sum이 total의 절반값이 되는 경우 (sum==total//2) 바로 답을 출력하는 것은 섣부른 판단이다. (반례가 있음. ex. 홀수)
