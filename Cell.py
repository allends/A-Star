import math


class Cell:
    x = 0
    y = 0
    g = 99999999999
    f = 99999999999
    h = 99999999999
    color = (255, 255, 255)
    prev = None
    neighbors = []

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def create_neighbors(self, grid):
        self.neighbors = []
        if self.x < 99:
            self.neighbors.append(grid[self.x + 1][self.y])
        if self.x > 0:
            self.neighbors.append(grid[self.x - 1][self.y])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y - 1])
        if self.y < 99:
            self.neighbors.append(grid[self.x][self.y + 1])
        if self.y < 99 and self.x < 99:
            self.neighbors.append(grid[self.x + 1][self.y + 1])
        if self.y < 99 and self.x > 0:
            self.neighbors.append(grid[self.x - 1][self.y + 1])
        if self.y > 0 and self.x < 99:
            self.neighbors.append(grid[self.x + 1][self.y - 1])
        if self.y > 0 and self.x > 0:
            self.neighbors.append(grid[self.x - 1][self.y - 1])
        return
