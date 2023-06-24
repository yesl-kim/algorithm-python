# 깊이 우선 탐색 (DFS)

- 그래프 탐색 알고리즘 (트리에서도 쓰임)
- 한 방향으로 탐색하다가 더이상 같은 방향의 탐색할 노드가 없을 경우 가장 가까운 갈림길로 돌아와 다시 깊이 탐색하는 기법
- 각각의 노드를 **중복없이** 탐색
- Fist In, Last Out policy 를 따름 (=> 스택 자료구조 사용)
- 재귀를 활용할 수도 있다
- 완전탐색으로 문제를 해결할 때는 **순회를 일찍 종료할 수 있는 예외케이스**를 생각하는 것이 좋다.

## 참고

- [그림자료](https://github.com/trekhleb/javascript-algorithms/tree/master/src/algorithms/tree/depth-first-search)
- [코드 참고](https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html)
- [코드없는 프로그래밍 유튜브 | 코딩테스트, 초급, DFS, BFS 그래프 탐색, Graph Traverse](https://www.youtube.com/watch?v=gl5RhtU2mF8&list=PLDV-cCQnUlIZH0wklfVG1IN9ks4g92oN7&index=3)
