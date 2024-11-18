from maze import Maze
from cell import Cell
from path import Path

class Walker:
    def __init__(self, maze):
        self.maze = maze
        self.path = Path()
        self.best_path = None
        self.memory = {}

    def find_path(self, maze: Maze, step: Cell):
        if step.is_end():
            if self.best_path is None or len(self.path) < len(self.best_path):
                self.best_path = self.path.copy()
            return
        
        if not self.best_path is None and len(self.best_path) < len(self.path):
            return

        for neighbor in maze.get_neighbors(step):
            if self.path.contains(neighbor):
                continue

            if self.memory.get(neighbor) != None:
                if self.memory.get(neighbor) < len(self.path):
                    continue

            self.memory[neighbor] = len(self.path)
            self.path.add_step(neighbor)
            self.find_path(maze, neighbor)
            self.path.step_back()
            



        