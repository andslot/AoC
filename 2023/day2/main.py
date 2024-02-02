color_map = {"green": 0, "blue": 1, "red": 2}

def part1():
    colors = [13, 14, 12]
    result = 0
    for line in open("input.txt", "r"):
        id, game = line.rstrip().split(": ")
        id, picks = int(id.split(" ")[-1]), game.split("; ")
        impossible = False
        for pick in picks:
            cubes = pick.split(", ")
            for cube in cubes:
                number, color = cube.split(" ")
                if int(number) > colors[color_map[color]]:
                    impossible = True
        result += id if not impossible else 0
    return result

def part2():
    result = 0
    for line in open("input.txt", "r"):
        _, games = line.rstrip().split(":")
        green = blue = red = 0
        for game in games.split(";"):
            green_i = 1 if "green" not in game else int(game[game.index("green") - 3 : game.index("green")].strip())
            blue_i = 1 if "blue" not in game else int(game[game.index("blue")- 3 : game.index("blue")].strip())
            red_i = 1 if "red" not in game else int(game[game.index("red") - 3 : game.index("red")].strip())
            green = green_i if green_i > green else green
            blue = blue_i if blue_i > blue else blue
            red = red_i if red_i > red else red
        result += green * blue * red
    return result
            

if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")