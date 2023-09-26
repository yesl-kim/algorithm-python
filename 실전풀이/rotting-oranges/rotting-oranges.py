# https://leetcode.com/problems/rotting-oranges/submissions/

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rotten = deque()
        for x, row in enumerate(grid):
            for y, orange in enumerate(row):
                if orange == 2:
                    rotten.append((0,x,y))
                if orange == 1:
                    fresh += 1
        m = 0
        w, h = len(grid), len(grid[0])
        while rotten:
            m, x, y = rotten.popleft()
            for dx, dy in ((0,1), (1,0), (0,-1), (-1,0)):
                xx, yy = x+dx, y+dy
                if 0<=xx<w and 0<=yy<h and grid[xx][yy] == 1:
                    grid[xx][yy] = 2
                    fresh -= 1
                    rotten.append((m+1, xx, yy))
        
        return m if fresh == 0 else -1
    

'''
난이도: 미디엄, 푸는데 걸린 시간: 30분
- 썩은 오렌지는 1분 후 상하좌우에 위치한 오렌지를 썩게한다.
- 이때 모든 오렌지가 썩는 데에 걸리는 최소 시간 (분)
=> 오렌지가 썩는 데 걸리는 시간은 트리의 레벨과 같음 -> 큐에 좌표와 함께 레벨도 저장
=> 모든 오렌지가 썩는지 -> 신선한 오렌지의 개수 필요
'''