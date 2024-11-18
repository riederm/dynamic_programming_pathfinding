# dynamic_programming_pathfinding
simple example to apply top-down dynamic programming

## Problem Description: 2D Maze Pathfinding
You are given a 2D grid representing a maze. Each cell in the grid can either be:
- Free (denoted by ' ')
- Wall (denoted by #)
- the Start cell (denoted by S)
- the End cell (denoted by E)
You can walk on a free-cell, you cannot walk on a wall-cell. The maze will be surrounded by walls.

The maze has a starting point S and an ending point E. Your task is to write a program that calculates the shortest path from S to E. The path can only move up, down, left, or right, and cannot pass through blocked cells (walls).


## Example Maze:

```
######################
#                    #
#          S         #
#     ###########    #
#      #        #    #
#      #        #    #
########    #   #    #
#      ##   #        #
#      #    #        #
#           ##########
#                  E #
######################
```

## Class Diagram
```mermaid
classDiagram
    class Cell {
        -x: int
        -y: int
        -cell_type: char
        +is_free() bool
        +is_wall() bool
        +is_start() bool
        +is_end() bool
    }

    class Maze {
        +get_neighbors(Cell) Cell[]
        +get_cell_at(int, int)
        +print() void
        +load_from_file(String) Maze
    }

    class Walker {
        +find_path(Maze) Path
    }

    class Path {
        +add_step(Cell) void
        +step_back() void
        +get_len() int
    }

    Path "1" --> "*" Cell: consists of


    Maze"1" *-- "*"Cell : consists of 
    Walker --> Maze
    Walker"1" --> "1"Path: path
    Walker"1" --> "1"Path: best_path

    Walker"1" --> "1"Cell: start
    Walker"1" --> "1"Cell: end 
```