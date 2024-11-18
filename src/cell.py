# src/field.py

class Cell:
    def __init__(self, x, y, cell_type):
        self.x = x
        self.y = y
        self.cell_type = cell_type  # ' ' for free, '#' for wall, 'S' for start, 'E' for end

    def is_free(self):
        return self.cell_type == ' '

    def is_wall(self):
        return self.cell_type == '#'

    def is_start(self):
        return self.cell_type == 'S'

    def is_end(self):
        return self.cell_type == 'E'
