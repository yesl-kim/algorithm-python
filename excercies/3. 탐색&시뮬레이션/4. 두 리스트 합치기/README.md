# 두 리스트 합치기

> O(N)

- 해당 문제는 병합정렬의 원리로 푼다
- 주어진 두 배열을 합친 뒤 내장함수인 sort를 사용하면 NlogN의 시간복잡도가 걸린다
- 하지만 이미 주어진 배열은 정렬된 배열이기 때문에 둘 중 한 배열만 순회하고도 정렬된 병합 배열을 얻을 수 있다 -> O(N)

### TIP

**슬라이스: a 부터 끝까지**

```py
arr=[1,2,3,4,5,6]
a=3
print(arr[a:]) # a부터 끝까지
```
