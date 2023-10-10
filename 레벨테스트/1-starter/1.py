

def solution(park, routes):
    H, W = len(park), len(park[0])
    direction = {'E': (0, 1), 'S': (1, 0), 'W': (0, -1), 'N': (-1, 0)}

    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                x, y = i, j
                break

    movable = lambda x, y : 0 <= x < H and 0 <= y < W and park[x][y] != 'X'
    for r in routes:
        _, distance = r.split()
        dx, dy = direction[_]

        xx, yy = x, y
        for _ in range(int(distance)):
            xx += dx
            yy += dy
            if not movable(xx, yy):
                break
        else:
            x, y = xx, yy

    return [x, y]

park = ["OSO","OOO","OXO","OOO"]
routes = ["E 2","S 3","W 1"]
# park = ["SOO","OXX","OOO"]
# routes = ["E 2","S 2","W 1"]
# park = ["SOO","OOO","OOO"]
# routes = ["E 2","S 2","W 1"]
print('=>', solution(park, routes))