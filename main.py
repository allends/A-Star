import math
import time
import pygame

from Cell import Cell
from draw import drawLoop

# pgyame init
pygame.init()
pygame.display.set_mode((500,500))
pygame.display.set_caption("A-Star Simulation")
screen = pygame.display.get_surface()

# setting up the game loop
FPS = 60
clock = pygame.time.Clock()
run = True

# colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# grid setup
openSet = []
closedSet = []
grid = [[]]
for i in range(100):
    for j in range(100):
        grid[i].append(Cell(i,j))
    grid.append([])

for i in range(100):
    for j in range(100):
        grid[i][j].create_neighbors(grid)

#some flags
pressed = False
started = False

#start and goal points as well as the queue
startPoint = grid[0][0]
endPoint = grid[98][98]
startPoint.color = green
endPoint.color = green

# a star functions
def distance(a,b):
    x = a.x - b.x
    y = a.y - b.y
    dist = math.sqrt(x**2 + y**2)
    return dist

def makePath(endPoint):
    pointer = endPoint
    path = []
    while pointer:
        pointer.color = red
        path.append(pointer)
        pointer = pointer.prev
    return path

def astar(entry, goal):
    entry.g = 0
    openSet.append(entry)
    while openSet:
        #drawLoop(screen, grid)
        #get the lowest fscore for our next move
        currentVal = math.inf
        current = None
        for node in openSet:
            if node.f < currentVal:
                currentVal = node.f
                current = node

        print(str(current.x) + " " + str(current.y))

        if current.x == goal.x and current.y == goal.y:
            return makePath(current)

        openSet.remove(current)

        for neighbor in current.neighbors:
            if not neighbor.color == black:
                    tempG = current.g + 1
                    if tempG < neighbor.g:
                        neighbor.prev = current
                        neighbor.g = tempG
                        neighbor.f = neighbor.g + distance(neighbor, endPoint)
                        neighbor.color = green
                        if not openSet.__contains__(neighbor):
                            openSet.append(neighbor)

    return None



while run:
    clock.tick(FPS)
    drawLoop(screen, grid)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed = True
        if event.type == pygame.MOUSEMOTION:
            if pressed:
                pos = pygame.mouse.get_pos()
                grid[int(pos[0]/5)][int(pos[1]/5)].color = black
        if event.type == pygame.MOUSEBUTTONUP:
            pressed = False
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        if not started:
            started = True
            astar(startPoint, endPoint)



pygame.quit()
