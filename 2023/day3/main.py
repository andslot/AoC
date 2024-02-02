def read_file():
    file = open("input.txt", "r").readlines()
    symbols = {}
    digits = []
    for i, line in enumerate(file):
        digit = 0
        d_len = 0
        for j, elem in enumerate(line):
            if elem.isnumeric():
                digit *= 10
                digit += int(elem)
                d_len += 1
            elif not elem.isnumeric() and d_len != 0:
                digits.append([digit, set([(c, k) for k in range(j - d_len - 1, j + 1) for c in range(i - 1, i + 2)])])
                digit = 0
                d_len = 0
            if not elem.isnumeric() and elem not in ".\n":
                symbols[(i, j)] = elem
    return digits, symbols

def part1():
    result = 0
    digits, symbols = read_file()
    for digit, grid in digits:
        if any(cord in symbols for cord in grid):
            result += digit
    return result

def part2():
    result = 0
    digits, symbols = read_file()
    gears = {}
    for k, v in symbols.items():
        if v == "*":
            gears[k] = v
    for gear in gears:
        d = []
        for digit, grid in digits:
            if gear in grid:
                d.append(digit)
        if len(d) == 2:
            result += d[0] * d[1]

    return result

if __name__ == "__main__":
    print(part1())
    print(part2())