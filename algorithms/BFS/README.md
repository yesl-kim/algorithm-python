# 너비 우선 탐색 (BFS)

- 그래프 탐색 알고리즘
- 갈림길을 만나면 같은 레벨의 노드를 우선 탐색한 후 자식 노드를 탐색하는 기법
- First In, First Out policy를 따름 (=> **큐** 자료구조를 사용)
- 각각의 노드를 **중복없이** 탐색
- 시간복잡도는 O(V + E) (V=`vertex`, E=`edge`)
- 공간복잡도는 O(V)

## 참고

- [그림자료](https://github.com/trekhleb/javascript-algorithms/tree/master/src/algorithms/tree/breadth-first-search)
- [코드없는 프로그래밍 유튜브 | 코딩테스트, 초급, DFS, BFS 그래프 탐색, Graph Traverse](https://www.youtube.com/watch?v=gl5RhtU2mF8&list=PLDV-cCQnUlIZH0wklfVG1IN9ks4g92oN7&index=3)
- [코드 참고](https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html)
