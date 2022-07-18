import copy


class Cell:
    def __init__(self, initial=False):
        self.alive = initial

    def revive(self):
        self.alive = True
        
    def kill(self):
        self.alive = False

    def is_alive(self):
        return self.alive


class Life:
    def __init__(self, width, height):
        self.grid = []
        self._width = width
        self._height = height
        
        for _ in range(0, self._height):
            self.grid.append([Cell() for _ in range(0, self._width)])
    
    def seed(self, seeds):
        for x, y in seeds:
            self.grid[y][x].revive()
    
    def tick(self):
        """
        Rules:
        - Any live cell with fewer than two live neighbors dies, as if by under-population.
        - Any live cell with two or three live neighbors lives on to the next generation.
        - Any live cell with more than three live neighbors dies, as if by overpopulation.
        - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        """
        
        future_grid = copy.deepcopy(self.grid)
        
        for y in range(0, self._height):
            for x in range(0, self._width):
                neighbors = 0
                    
                for ny in range(-1, 2):
                    for nx in range(-1, 2):
                        if ny == 0 and nx == 0:
                            continue
                        
                        test_y = y + ny
                        test_x = x + nx
                        
                        if test_y < 0 or test_y > self._height - 1:
                            continue
                        
                        if test_x < 0 or test_x > self._width -1:
                            continue
                        
                        if self.grid[test_y][test_x].is_alive():
                            neighbors += 1
                   
                if neighbors == 3:
                    future_grid[y][x].revive()
                    
                elif neighbors > 3:
                    future_grid[y][x].kill()
                
                elif neighbors < 2:
                    future_grid[y][x].kill()
        
        self.grid = future_grid

    def draw(self):
        for row in self.grid:
            out_row = []
            for cell in row:
                out_row.append("0" if cell.is_alive() else "-")
            print(out_row)
