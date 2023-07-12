import turtle as t
import random as r
import time

class Brick():
    def __init__(self):
        self.y=0
        self.x=r.randint(1,13)
        self.color=r.randint(1,6)

def draw_grid(block,grid):
    block.clear()
    top=250
    left=-150
    colors=['black','red','blue','green','yellow','purple','orange','white']
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            block.goto(left+(22*x),top-(22*y))
            block.color(colors[grid[y][x]])
            block.stamp()

if __name__=="__main__":
    sc=t.Screen()
    sc.tracer(False)
    sc.bgcolor('black')
    sc.setup(width=600,height=700)
    block=t.Turtle()
    block.penup()
    block.speed(0)
    block.shape('square')
    block.setundobuffer(None)

    grid=[[0]*12 for _ in range(24)]
    for i in range(24):
        grid[i].insert(0,7)
        grid[i].append(7)
    for i in range(1,4):
        for j in range(1,13):
            grid[-i][j]=r.randint(1,6)
    grid.append([7]*14)

    brick=Brick()
    grid[brick.y][brick.x]=brick.color
    draw_grid(block, grid)

    while True:
        sc.update()
        if grid[brick.y+1][brick.x+1]==0:
            grid[brick.y][brick.x]=0
            brick.y+=1
            grid[brick.y][brick.x]=brick.color
        # else:
        #     brick=Brick()
        #     grid[brick.y][brick.x]=brick.color
        for x in grid:
            print(x)
        draw_grid(block,grid)
        time.sleep(0.1)



    sc.mainloop()