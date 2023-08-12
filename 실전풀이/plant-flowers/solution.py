# https://docs.google.com/document/d/1XwIyKOYnAzWoyyZM8zAHQ7zODWSB7eSGVkNMhc50UX8/edit

'''
n: int - map 사이즈 (n*n)
map: List[List[str]] - 지도
'''

def plant(n, map):
    # 3) 유효성 검사
    def is_all_empty(x, y):
        return all([map[x][_] != 'X' and map[_][y] != 'X' for _ in range(n)])

    # 2) 식물 심기: 깊이 탐색
    def find(L = 0):
        if L == len(houses): # todo
            print(map)
        else:
            i, j = houses[L]
            for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < n and map[x][y] == '0' and is_all_empty(x, y):
                    map[x][y] = 'X'
                    find(L+1)
                    map[x][y] = '0'
    
    # 1) find a house
    houses = []
    for i in range(n):
        for j in range(n):
            if map[i][j] == 'H': 
                houses.append((i, j))
    
    find()

# -----
map = [['H', '0', '0', '0'], 
       ['H', '0', '0', '0'], 
       ['0', '0', '0', 'H'],
       ['0', '0', '0', 'H']]
map2 = [['0', '0', 'H', '0'], ['0', '0', '0', '0'], ['0', 'H', '0', '0'],['H', 'H', '0', '0']]
map3 = [['0', '0', '0', '0', 'H'],['0', '0', '0', '0', '0'], ['0', '0', 'H', '0', 'H'], ['H', '0', '0', '0', '0'], ['H', '0', '0', '0', '0']]

ns = [4, 4, 5]
maps = [map, map2, map3]

for i in range(3):
    print('-'*10)
    plant(ns[i], maps[i])