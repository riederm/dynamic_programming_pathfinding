from cell import Cell
from path import Path

class Maze:
    def __init__(self, grid):
        self.grid = [[Cell(x, y, cell) for x, cell in enumerate(row)] for y, row in enumerate(grid)]
        self.start = self.find_start()
        self.end = self.find_end()

    def find_start(self):
        for row in self.grid:
            for cell in row:
                if cell.is_start():
                    return cell
        return None

    def find_end(self):
        for row in self.grid:
            for cell in row:
                if cell.is_end():
                    return cell
        return None

    def get_neighbors(self, cell):
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = cell.x + dx, cell.y + dy
            if 0 <= nx < len(self.grid[0]) and 0 <= ny < len(self.grid):
                n = self.grid[ny][nx]
                if not n.is_wall():
                    neighbors.append(n)
        return neighbors
    
    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as file:
            grid = [list(line.strip()) for line in file.readlines()]
        return cls(grid)
    
    def print_maze(self, path:Path):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell in path:
                    print('.', end='')
                else:
                    print(cell.cell_type, end='')
            print()