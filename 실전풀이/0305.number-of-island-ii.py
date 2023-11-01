# https://docs.google.com/document/d/1N_dDKC1XXgyVkj3qOeKqK-yTusFKiK4kWFShfRWARqw/edit

from typing import List

class Island:
    def __init__(self):
        self.root = [0] # 1 indexed (0은 바다)
        self.height = [1]
    
    def add(self) -> int:
        label = len(self.root)
        self.root.append(label)
        self.height.append(1)
        return label

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def connect(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        
        hx, hy = self.height[rx], self.height[ry]
        if hx < hy:
            self.root[rx] = ry
        else:
            self.root[ry] = rx
            
            if hx == hy:
                self.height[rx] += 1

    # 서로소 집합 개수 반환
    def count(self):
        return len(set((self.find(node) for node in self.root[1:])))


def number_of_islands(h:int, w:int, positions: List[List[int]]) -> List[int]:
    grid = [[0]*w for _ in range(h)]

    def adj(x, y):
        for dx, dy in ((0,1), (1,0), (0,-1), (-1,0)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and 0 < grid[nx][ny]:
                yield nx, ny


    islands = Island() 
    res = []
    for x, y in positions:
        i = islands.add()
        grid[x][y] = i
        for nx, ny in adj(x, y):
            islands.connect(i, grid[nx][ny])
        res.append(islands.count())

    return res

m = 3
n = 3
positions = [[0, 0], [0, 1], [1, 2], [2, 1], [1, 1]]
# positions = [[0, 0], [0, 1], [1, 2], [2, 1]]
print('=>', number_of_islands(m, n, positions))

# 육지
    # islands[i] = i번째 육지의 섬 번호
    # 육지 추가 = islands.append
# 연결된 육지 연결
# 매 회 서로소 집합의 개수 반환