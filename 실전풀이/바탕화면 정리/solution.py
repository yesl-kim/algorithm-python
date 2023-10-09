def solution(wallpaper):
    lux = luy = float('inf')
    rdx = rdy = float('-inf')
    for i, row in enumerate(wallpaper):
        for j, cell in enumerate(row):
            if cell == '#':
                lux, luy = min(lux, i), min(luy, j)
                rdx, rdy = max(rdx, i+1), max(rdy, j+1)

    return [lux, luy, rdx, rdy] 