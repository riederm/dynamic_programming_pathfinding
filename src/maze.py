from cell import Cell
from path import Path
from colorama import Fore, Back, Style

class Maze:
    
    def __init__(self, grid):
        """
        Initializes the Maze with a grid of cells, and finds the start and end points.

        Args:
            grid (list of list of Cell): A 2D list representing the maze grid where each cell is an integer.

        Attributes:
            grid (list of list of Cell): A 2D list of Cell objects representing the maze.
            start (Cell): The starting cell of the maze.
            end (Cell): The ending cell of the maze.
        """
        self.grid = [[Cell(x, y, cell) for x, cell in enumerate(row)] for y, row in enumerate(grid)]
        self.start = self.find_start()

    def find_start(self):
        """
        Find the starting cell in the maze.

        Returns:
            Cell: The starting cell of the maze.
        """
        for row in self.grid:
            for cell in row:
                if cell.is_start():
                    return cell

    
    def get_neighbors(self, cell: Cell):
        """
        Get the list of neighboring cells that are not walls.

        Args:
            cell (Cell): The current cell for which to find neighbors.

        Returns:
            List[Cell]: A list of neighboring cells that are not walls.
        """
        
        max_row = len(self.grid)
        max_cell = len(self.grid[0])

        current_x = cell.x
        current_y = cell.y

        neighbors = []

        # x neighbors
        if (current_x > 0): # we are NOT at the left border
            n = self.grid[current_y][current_x - 1]
            if not n.is_wall():
                neighbors.append(n)

        if (current_x < max_cell): # we are NOT at the right border
            n = self.grid[current_y][current_x + 1]
            if not n.is_wall():
                neighbors.append(n)

        # y neighbors
        if (current_y > 0): # we are NOT at the upper border
            n = self.grid[current_y - 1][current_x]
            if not n.is_wall():
                neighbors.append(n)
            
        if (current_y < max_row): # we are NOT at the lower border
            n = self.grid[current_y + 1][current_x]
            if not n.is_wall():
                neighbors.append(n)
        return neighbors
    
    
    @classmethod
    def from_file(cls, filename):
        """
        Create a Maze instance from a file.

        Args:
            filename (str): The path to the file containing the maze grid.

        Returns:
            Maze: An instance of the Maze class initialized with the grid from the file.

        The file should contain a grid representation of the maze, where each line
        corresponds to a row in the grid and each character corresponds to a cell
        in the maze.
        """
        with open(filename, 'r') as file:
            grid = [list(line.strip()) for line in file.readlines()]
        return cls(grid)
    

    def print_maze(self, path: Path):
        """
        Prints the maze to the console, marking the path with dots (.).
        Args:
            path (Path): The path to be marked in the maze.
        """
        for row in self.grid:
            for cell in row:
                if path.contains(cell):
                     print(Back.GREEN + ".",end="")     
                else:
                    print(Back.BLACK + cell.get_representation(),end="")
            print()