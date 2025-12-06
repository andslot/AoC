import numpy as np

def part1(input_file):
    file = open(input_file, 'r')
    lines = [line.strip() for line in file.readlines()]
    file.close()

    ops = [o.strip() for o in lines[-1].split()]
    numbers = np.array([[int(n.strip()) for n in line.split()] for line in lines[:-1]])
    
    total = 0
    for i, op in enumerate(ops):
        if op == "+":
            total += sum(numbers[:, i])
        else:
            total += np.prod(numbers[:, i])

    return total

def part2(input_file):
    file = open(input_file, 'r')
    lines = [line.replace('\n', '') for line in file.readlines()]
    file.close()

    ops = [o.strip() for o in reversed(lines[-1].split())]
    numbers = np.array([l[::-1] for l in lines[:-1]])
    
    total = 0

    op_index = 0
    count_space = 0
    parsed_numbers = []
    while all(len(line) > 0 for line in numbers):
        
        parsed_number = ''
        for i, row in enumerate(numbers):
            if row[0] == ' ':
                count_space += 1
                numbers[i] = row[1:]
                continue
            parsed_number += row[0]
            numbers[i] = row[1:]
        
        if count_space != len(numbers):
            parsed_numbers.append(int(parsed_number))
            count_space = 0

        if count_space == len(numbers):
            if ops[op_index] == '+':
                total += sum(parsed_numbers)
            else:
                total += np.prod(parsed_numbers)
            
            count_space = 0
            op_index += 1
            parsed_numbers = []
            continue
        
    if ops[op_index] == '+':
        total += sum(parsed_numbers)
    else:
        total += np.prod(parsed_numbers)
    
    return total

if __name__ == "__main__":
    input_file = 'day6/input.txt'
    print("Part 1:", part1(input_file))
    print("Part 2:", part2(input_file))