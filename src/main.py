from maze import Maze
from walker import Walker

def main():
    maze = Maze.from_file('/workspaces/dynamic_programming_pathfinding/src/mazes/maze2.txt')
    

    walker = Walker(maze)
    walker.find_path(maze.find_start())

    maze.print_maze(walker.best_path)


if __name__ == "__main__":
    main()