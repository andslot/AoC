import re
import time

with open("input.txt") as f:
    lines = f.read().replace("\n", "")

def part1():
    x = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", lines)
    
    result = 0
    for mul in x:
        a = re.findall("[0-9]{1,3}", mul)
        result += int(a[0]) * int(a[1])
    print(result)

def part2():
    x = re.findall("(do\(\)|don\'t\(\)|mul\([0-9]{1,3},[0-9]{1,3}\))", lines)

    result = 0
    allow = True
    for elem in x:
        if elem != "do()" and elem != "don't()" and allow:
            a = re.findall("[0-9]{1,3}", elem)
            result += int(a[0]) * int(a[1])
        elif elem == "do()":
            allow = True
        elif elem == "don't()":
            allow = False
    print(result)


if __name__ == "__main__":
    start = time.time()
    part1()
    end = time.time()
    print("Part 1: " + str(end - start) + "s")
    start = time.time()
    part2()
    end = time.time()
    print("Part 2: " + str(end - start) + "s")