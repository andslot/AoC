import numpy as np

def get_adjacent(x, y, grid):
    adjecent_counts = np.zeros(grid.shape, dtype=int)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    
    for direction in directions:
        if y == 0 and direction[0] == -1:
            continue
        elif y == len(grid) - 1 and direction[0] == 1:
            continue
        elif x == 0 and direction[1] == -1:
            continue
        elif x == len(grid[0]) - 1 and direction[1] == 1:
            continue
        else:
            if grid[y + direction[0]][x + direction[1]] == '@':
                adjecent_counts[y][x] += 1

    return adjecent_counts
def part1(input_file: str):
    file = open(input_file, 'r')
    grid = np.array([[x for x in line.strip()] for line in file.readlines()])
    
    adjacent = np.zeros(grid.shape,  dtype=int)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                adjacent += get_adjacent(j, i, grid)
    mask = (grid == '@')
    valid_adjacent = adjacent[mask]
    
    return np.sum(valid_adjacent < 4)



def part2(input_file: str):
    file = open(input_file, 'r')
    grid = np.array([[x for x in line.strip()] for line in file.readlines()])

    total_count = 0
    while True:
        adjacent = np.zeros(grid.shape,  dtype=int)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '@':
                    adjacent += get_adjacent(j, i, grid)
        mask = (grid == '@')
        valid_adjacent = adjacent[mask]
        grid_mask = (grid == '@') & (adjacent < 4)
        grid[grid_mask] = '.' 

        if np.sum(valid_adjacent < 4) == 0:
            break
        
        total_count += np.sum(valid_adjacent < 4)
    return total_count

if __name__ == "__main__":
    input_file = "day4/input.txt"
    print("Part 1:", part1(input_file))
    print("Part 2:", part2(input_file))