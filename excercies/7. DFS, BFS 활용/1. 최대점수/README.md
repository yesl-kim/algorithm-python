## 접근방식

> DFS

- 부분집합을 푸는 문제와 동일
- 이진 상태트리의 완전탐색 문제

### NOTE

TODO

```py
def dfs(L=0,s=0,t=M):
    global res
    remain=sum([x[0] for x in n[L:-1]])
    if s+remain<res: return
    if L==N or t==0:
        if res<s: res=s
    else:
        dfs(L+1,s,t) # 1.
        need=n[L][1]
        if not t-need<0: dfs(L+1, s+n[L][0],t-need) # 2.

def dfs(L=0,s=0,t=M):
    global res
    if t<0: return
    remain=sum([x[0] for x in n[L:-1]])
    if s+remain<res: return
    if L==N or t==0:
        if res<s: res=s
    else:
        dfs(L+1,s,t)
        dfs(L+1,s+n[L][0],t-n[L][1])

```

- 원래는 위의 처럼 문제를 풀기 위해 필요한 시간이 현재 남은 시간보다 클경우,
- 현재 문제를 푸는 선택은 하지 않는다- 라는 논리로 로직을 작성했는데
- 그것보다는 다음 DFS에서 바로 함수를 종료시키는 것이 더 좋은 걸까? 문제가 생길 줄 알았는데- 안생기는게 헷갈려
