def part1(l: int, w: int, h: int) -> int:
    side1 = l * w
    side2 = w * h
    side3 = h * l

    slack = min(side1, side2, side3)
    return 2*side1 + 2*side2 + 2*side3 + slack

def part2(l: int, w: int, h: int) -> int:
    sides = [l, w, h]
    min_side1 = min(sides)
    sides.remove(min_side1)
    min_side2 = min(sides)
    return  2*min_side1 + 2*min_side2 + l * w * h


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        total = 0
        total2 = 0
        for line in f.readlines():
            inputs = list(map(int, line.split("x")))
            total += part1(*inputs)
            total2 += part2(*inputs)
        print(total)
        print(total2)