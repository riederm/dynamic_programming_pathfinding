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

    def find_path(self, current_pos: Cell):
        """
        Recursively finds the shortest path in a maze from the current step to the end.
        Args:
            maze (Maze): The maze object containing the grid and methods to get neighbors.
            step (Cell): The current cell in the maze being evaluated.
        Returns:
            None: The function updates the best_path attribute with the shortest path found.
        """
        
        if current_pos.is_end():
            print("hurraaa")
            self.best_path = self.path.copy()
            return 
        
        options = self.maze.get_neighbors(current_pos)

        for option in options:
            if self.path.contains(option): # to NOT step back to a previous cell
                continue

            # while walking, we need to take a note, what the shortes path is
            # that already reached option
            # if our current path is longer thatn what we found so far, there is no
            # point in taking this route


            existingNote = self.memory.get(option)
            if existingNote is None:
                #we are the first one here
                self.memory[option] = len(self.path)
            elif existingNote > len(self.path):
                #we are faster than previous solutions
                self.memory[option] = len(self.path)
            else:
                # previous solution were faster
                continue


            self.path.add_step(option)
            self.find_path(option)
            self.path.step_back()


            



        