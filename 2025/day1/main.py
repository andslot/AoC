def part1():
    f = open("./day1/input_part1.txt", "r")
    lines = f.readlines()

    zero_count = 0
    dial = 50
    for line in lines:
        line = line.strip()
        if line[0] == "R":
            dial = (dial + int(line[1:])) % 100
        elif line[0] == "L":
            dial = (dial - int(line[1:])) % 100

        if dial == 0:
            zero_count += 1
    print(zero_count)

def part2():
    f = open("./day1/input_part1.txt", "r")
    lines = f.readlines()

    zero_count = 0
    dial = 50
    for line in lines:
        line = line.strip()
        direction = line[0]
        n = int(line[1:])
        if direction == "R":
            dist = (100 - dial) % 100
        else:
            dist = dial

        if dist == 0:
            dist = 100

        if n >= dist:
            zero_count += 1 + ( n - dist ) // 100
        
        if direction == "R":
            dial = (dial + n) % 100
        else:
            dial = (dial - n) % 100
    print(zero_count)

if __name__ == "__main__":
    part1()
    part2()