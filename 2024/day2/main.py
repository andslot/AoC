def safe(ints):
    diffs = [j-i for i, j in zip(ints, ints[1:])]

    if all(d > 0 for d in diffs) and all(1 <= abs(d) <= 3 for d in diffs):
        return True
    if all(d < 0 for d in diffs) and all(1 <= abs(d) <= 3 for d in diffs):
        return True

def part1():
    with open("inputs.txt", "r") as f:
        data = f.read().splitlines()

    result = 0
    for line in data:
        report = list(map(int, line.split()))
        if safe(report):
            result += 1
            continue

    print(result)
        


def part2():
    with open("inputs.txt", "r") as f:
        data = f.read().splitlines()

    result = 0
    for line in data:
        report = list(map(int, line.split()))
        if safe(report):
            result += 1
            continue

        for i in range(len(report)):
            x = report[:i] + report[i+1:]
            
            if safe(x):
                result += 1
                break
    print(result)

if __name__ == "__main__":
    part1()
    part2()