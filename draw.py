import pygame

white = (255,255,255)

def drawLoop(screen, grid):
    screen.fill(white)
    for i in range(100):
        for j in range(100):
            pygame.draw.rect(screen, grid[i][j].color, (i * 5,j * 5,5,5))
    pygame.display.update()