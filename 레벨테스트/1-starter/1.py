def solution(park, routes):
    park = [list(x) for x in park]
    h, w = len(park), len(park[0])

    for x in range(h):
        for y in range(w):
            if park[x][y] == 'S':
                break

    for r in routes:
        direction, distance = r.split()
        distance = int(distance)
        
        if direction == 'N':
            if 0 <= x - distance < h and all([park[x - d][y] != 'X' for d in range(1, distance + 1)]):
                x -= distance

        if direction == 'S':
            if 0 <= x + distance < h and all([park[x + d][y] != 'X' for d in range(1, distance + 1)]):
                x += distance

        if direction == 'W':
            if 0 <= y - distance < w and all([park[x][y - d] != 'X' for d in range(1, distance + 1)]):
                y -= distance

        if direction == 'E':
            if 0 <= y + distance < w and all([park[x][y + d] != 'X' for d in range(1, distance + 1)]):
                y += distance


    return [x, y]