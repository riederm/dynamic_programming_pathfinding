from maze import Maze
from cell import Cell
from path import Path

class Walker:
    def __init__(self, maze: Maze):
        """
        Initializes the Walker with a given maze.

        Args:
            maze: The maze represented as a 2D list where each element is an integer.

        Attributes:
            maze: The maze to be solved.
            path (Path): The current path being explored.
            best_path (Path or None): The best path found so far.
            memory (dict): A dictionary to store previously computed results for optimization.
        """
        self.maze = maze
        self.path = Path()
        self.best_path = None
        self.memory = {}

    def find_path(self, maze: Maze, step: Cell):
        """
        Recursively finds the shortest path in a maze from the current step to the end.
        Args:
            maze (Maze): The maze object containing the grid and methods to get neighbors.
            step (Cell): The current cell in the maze being evaluated.
        Returns:
            None: The function updates the best_path attribute with the shortest path found.
        """
        # TODO Implement this method
            



        