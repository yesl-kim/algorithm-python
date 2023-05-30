# 그래프 자료구조

- vertex와 edge로 이루어짐
- vertex(정점): 데이터를 저장하는 노드
- edge(간선): 노드 사이의 관계 정보를 포함. 값을 가지기도 함

## 정의 및 종류

- **directed vs undirected** graph: 그래프의 edge가 방향성을 갖는지 vs 안갖는지
- **weighted** graph (가중그래프):

  - edge가 값을 갖는 그래프
  - ex. 각 지점 간의 이동시간
  - <image src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Weighted_Graph.svg/1200px-Weighted_Graph.svg.png' width='50%' alt='위키백과 | 가중그래프 예시' />

- **인접**: edge로 이어진 두 정점은 "인접"하다고 할 수 있다.
- **cycle**:

## 인접 행렬과 인접 리스트 구현

그래프에서 정점들의 인접 여부를 인접 행렬(2차원 배열)과 인접리스트로 구현할 수 있다.

### 인접 행렬

<image src='https://velog.velcdn.com/images%2Ffalling_star3%2Fpost%2Fc20e690d-9674-49e7-b450-c3e15ed36268%2F22.JPG' alt='hyuna song 블로그 | 인접행렬 예시' />

```py
# 위 이미지에서 우측 "가중치가 없는 무향 그래프"의 인접 행렬
[
  [0,1,0,0,0],
  [1,0,1,1,0],
  [0,1,0,0,1],
  [0,1,0,0,0],
  [0,0,1,0,0]
]
```

- 각 정점을 행번호와 열번호로 하는 2차원 배열에서 각 칸의 값은 인접 여부 혹은 간선의 가중치를 나타낸다.
- 가중치가 없는 그래프라면 인접여부를 (인접하면 1, 인접하지 않으면 0 또는 무한대)
- 가중치가 있는 그래프라면 가중치를 값으로 갖는다.
- 유향 그래프는 행 -> 열 의 방향으로 값을 기입하고
- 양방향인 무향 그래프는 우하향 하는 대각선을 기준으로 대칭한 행렬로 표현된다.

### 인접 리스트

<image src='https://t1.daumcdn.net/cfile/tistory/2146CC4457BC140B2C' alt='cinux 블로그 | 가중치 없는 그래프의 인접리스트 예시'>

<image src='https://blog.kakaocdn.net/dn/bksksy/btq7CSWdhZQ/8JYm16QKaIDRylIijK1TK1/img.jpg' alt='개척 라이프 블로그 | 가중치 있는 그래프의 인접리스트 예시' />

```py
# 첫번째 이미지 그래프의 인접 리스트
{
  0: [2,3,4],
  1: [3],
  2: [2],
  3: [2],
  4: [4],
  5: [2]
}
```

- 정점의 모든 인접상태를 표현한 인접행렬과 달리 인접한 정점에 대한 정보만 나타내는 형태로,
- 인접행렬보다 가볍고 메모리를 조금 덜 사용한다는 장점이 있다.

## 참고

- [위키독스 | 파이썬 사전](https://wikidocs.net/131176)
- [유튜브 | 깊이우선탐색(DFS, Depth First Search) - 5 minutes algorithm - python [상상개발자]](https://www.youtube.com/watch?v=BLc3wzvycH8&t=24s)
- [코드없는 프로그래밍 유튜브 | 코딩테스트, 기초, 그래프, Graph](https://www.youtube.com/watch?v=4izGhUk2L1s&list=PLDV-cCQnUlIZH0wklfVG1IN9ks4g92oN7&index=2)
- [세오토리 블로그 | 자바스크립트로 구현하는 그래프, 인접행렬, 인접리스트](https://seo-tory.tistory.com/50)
