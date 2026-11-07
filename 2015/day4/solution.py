import hashlib

def part1(text: str) -> int:
    i = 0
    solved = False
    while not solved:
        res = hashlib.md5(f"{text}{i}".encode())
        if res.hexdigest()[:5] == "00000":
            solved = True
            break
        i += 1
    return i

def part2(text: str) -> int:
    i = 0
    while True:
        res = hashlib.md5(f"{text}{i}".encode())
        if res.hexdigest()[:6] == "000000":
            break
        i += 1
    return i


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        line = f.readline()
        print(part1(line))
        print(part2(line))
    f.close()