def part1(text: str) -> int:
    history = [(0,0)]
    for i, c in enumerate(text):
        last = history[-1]
        if c == "v":
            history.append((last[0], last[1]-1))
        if c == "^":
            history.append((last[0], last[1]+1))
        if c == "<":
            history.append((last[0]+1, last[1]))
        if c == ">":
            history.append((last[0]-1, last[1]))

    return len(set(history))

def part2(text: str) -> int:
    history = [(0,0), (0,0)]
    for i, c in enumerate(text):
        last = history[-2]
        if c == "v":
            history.append((last[0], last[1]-1))
        if c == "^":
            history.append((last[0], last[1]+1))
        if c == "<":
            history.append((last[0]+1, last[1]))
        if c == ">":
            history.append((last[0]-1, last[1]))

    return len(set(history))

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        line = f.readline()
        print(part1(line))
        print(part2(line))
    f.close()