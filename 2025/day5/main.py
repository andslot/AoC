

def part1(input_file: str):
    file = open(input_file, "r")
    lines = file.read().strip().split("\n")

    ranges = []
    for i, line in enumerate(lines):
        if "-" in line:
            ranges.append(line.strip().split("-"))
        else:
            lines = lines[i+1:]
            break

    fresh_count = 0
    for line in lines:
        for l, r in ranges:
            if int(l) <= int(line) <= int(r):
                fresh_count += 1
                break
    return fresh_count


def part2(input_file: str):
    file = open(input_file, 'r')
    lines = file.read().strip().split("\n")

    ranges = []
    for line in lines:
        if "-" in line:
            ranges.append(line.strip().split("-"))
        else:
            break

    merged_ranges = []
    ranges.sort(key=lambda x: int(x[0]))
    current_start, current_end = ranges[0]
    for l, r in ranges[1:]:
        if int(l) <= int(current_end) + 1:
            current_end = max(int(current_end), int(r))
        else:
            merged_ranges.append((int(current_start), int(current_end)))
            current_start, current_end = l, r
    merged_ranges.append((int(current_start), int(current_end)))
        
        
    total_count = 0
    for l, r in merged_ranges:
        total_count += (r - l + 1)

    return total_count

if __name__ == "__main__":
    input_file = "day5/input.txt"
    print("Part 1:", part1(input_file))
    print("Part 2:", part2(input_file))