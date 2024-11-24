from colorama import init, Fore, Back, Style

def main():
    init()
    
    filename = '/workspaces/dynamic_programming_pathfinding/src/mazes/maze1.txt';
    #read file into two dim char array
    with open(filename, 'r') as file:
        # Read lines and create a 2D array (list of lists)
        maze = [list(line.strip()) for line in file]


    x,y = find_start(maze)

    path = walk(maze, x, y)
    print_maze(maze, path)
 
def walk(maze, x, y, path=[]):
    if maze[y][x] == 'E':
        return path

    if maze[y][x] == '#':
        return None

    shortestRoute = None
    for dx, dy, direction in [(0, 1, 'v'), (1, 0, '>'), (0, -1, '^'), (-1, 0, '<')]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze):
            if not any(pos[0] == nx and pos[1] == ny for pos in path):
                res = walk(maze, nx, ny, path + [(x, y, direction)])
                if res and (shortestRoute is None or len(res) < len(shortestRoute)):
                    shortestRoute = res
    return shortestRoute


def find_start(maze):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 'S':
                return x, y
    return None, None


def print_maze(maze, route):
    path_positions = {(x, y): direction for x, y, direction in route}
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 'S':
                print(Back.BLACK + Fore.YELLOW + 'S' + Style.RESET_ALL, end='')
            elif (x, y) in path_positions:
                arrow = path_positions[(x, y)]
                print(Back.BLACK + Fore.GREEN + arrow + Style.RESET_ALL, end='')
            elif cell == 'E':
                print(Back.BLACK + Fore.YELLOW + 'E' + Style.RESET_ALL, end='')
            elif cell == '#':
                print(Back.BLACK + Fore.RED + cell + Style.RESET_ALL, end='')
            else:
                print(Back.BLACK + cell + Style.RESET_ALL, end='')
        print()

if __name__ == "__main__":
    main()