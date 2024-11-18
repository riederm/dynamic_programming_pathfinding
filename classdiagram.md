```
classDiagram
    class Cell {
        +int x
        +int y
        +char cell_type
        +is_free() bool
        +is_wall() bool
        +is_start() bool
        +is_end() bool
    }

    class Maze {
        +Cell[][] grid
        +Cell start
        +Cell end
        +find_start() Cell
        +find_end() Cell
        +get_neighbors(Cell) Cell[]
        +from_file(String) Maze
        +print_maze() void
    }

    class Walker {
        +Maze maze
        +Cell[] path
        +find_path() void
    }

    class Path {
        +Cell[] steps
        +add_step(Cell) void
        +__iter__() iterator
    }

    Maze --> Cell
    Walker --> Maze
    Walker --> Path
```