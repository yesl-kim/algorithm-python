from heapq import heappop, heappush

def solution(maps):
    def adj(x, y):
        for dx, dy in ((1,0), (0, 1), (-1,0), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] != 'X':
                yield nx, ny

    def min_path(start, end):
        q = []
        heappush(q, (0, start)) # (dist, (x, y))
        visited = set()
        while q:
            dist, cur = heappop(q)
            if cur == end:
                return dist
            if cur in visited:
                continue
            visited.add(cur)
            for next in adj(*cur):
                heappush(q, (dist + 1, next))
        return -1
    

    def find_cell(s):
        for x, row in enumerate(maps):
            for y, cell in enumerate(row):
                if cell == s:
                    return x, y

    h, w = len(maps), len(maps[0])
    start, via, end = find_cell('S'), find_cell('L'), find_cell('E')

    a, b = min_path(start, via), min_path(via, end)
    if a == -1 or b == -1:
        return -1
    return a + b