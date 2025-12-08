from collections import defaultdict

def part1(input_file):
    file = open(input_file, 'r')
    lines = file.read().strip().splitlines()
    h = len(lines)

    grid = set()
    start = (0, 0)

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "^":
                grid.add((j, i))
            elif char == "S":
                start = (j, i)

    tips_positions = {start[0]}
    split_count = 0
    for i in range(start[1] + 1, h):
        if not any((j, i) in grid for j in tips_positions):
            continue

        new_tips_positions = set()
        for j in tips_positions:
            if (j, i) in grid:
                split_count += 1
                new_tips_positions.add(j - 1)
                new_tips_positions.add(j + 1)
            else:
                new_tips_positions.add(j)
        tips_positions = new_tips_positions

    return split_count



def part2(input_file):
    file = open(input_file, 'r')
    lines = file.read().strip().splitlines()
    h = len(lines)

    grid = set()
    start = (0, 0)

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "^":
                grid.add((j, i))
            elif char == "S":
                start = (j, i)

    tips_positions = defaultdict(int)
    tips_positions[start[0]] = 1
    for i in range(start[1] + 1, h):
        if not any((j, i) in grid for j in tips_positions):
            continue

        new_tips_positions = defaultdict(int)
        for j, count in tips_positions.items():
            if (j, i) in grid:
                new_tips_positions[j - 1] += count
                new_tips_positions[j + 1] += count
            else:
                new_tips_positions[j] += count
        tips_positions = new_tips_positions

    return sum(tips_positions.values())



if __name__ == "__main__":
    input_file = "day7/input.txt"
    print(part1(input_file))
    print(part2(input_file))