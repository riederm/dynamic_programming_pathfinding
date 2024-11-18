class Path:
    """
    A class to represent a path in a pathfinding algorithm.
    
    Attributes
    ----------
    steps : list
        A list to store the steps (cells) in the path.

    """
    def __init__(self):
        self.steps = []

    def add_step(self, cell):
        """
        Adds a step to the path.
        """
        self.steps.append(cell)

    def step_back(self):
        """
        Removes the last step from the path.

        This method pops the last element from the steps list, effectively 
        stepping back to the previous position in the path.
        """
        self.steps.pop()
   
    def contains(self, cell):
        """
        Check if the given cell is present in the steps.

        Args:
            cell: The cell to check for presence in the steps.

        Returns:
            bool: True if the cell is in the steps, False otherwise.
        """
        return cell in self.steps
    
    def copy(self):
        """
        Creates a copy of the current Path instance.

        Returns:
            Path: A new Path instance with the same steps as the current instance.
        """
        new_path = Path()
        new_path.steps = self.steps.copy()
        return new_path
    
    def __len__(self):
        """
        Return the number of steps in the path.

        Returns:
            int: The number of steps.
        """
        return len(self.steps)