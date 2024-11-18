class Path:
    def __init__(self):
        self.steps = []

    def add_step(self, cell):
        self.steps.append(cell)

    def step_back(self):
        self.steps.pop()

    def get_position(self):
        return self.steps[-1]

    def __iter__(self):
        return iter(self.steps)
    
    def contains(self, cell):
        return cell in self.steps
    
    def copy(self):
        new_path = Path()
        new_path.steps = self.steps.copy()
        return new_path
    
    def __len__(self):
        return len(self.steps)