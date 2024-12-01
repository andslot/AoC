import numpy as np

def part1():
    with open("input.txt") as f:
        data = f.read().splitlines()

    l1, l2 = [], []
    for d in data:
        d_split = d.split()
        l1.append(int(d_split[0]))
        l2.append(int(d_split[1]))

    l1.sort()
    l2.sort()
    l1 = np.array(l1)
    l2 = np.array(l2)

    print(np.abs(l1 - l2).sum())

def part2():
    with open("input.txt") as f:
        data = f.read().splitlines()

    l1, l2 = [], []
    for d in data:
        d_split = d.split()
        l1.append(int(d_split[0]))
        l2.append(int(d_split[1]))

    l1.sort()
    l2.sort()

    result = 0
    for i in l1:
        count = 0
        for j in l2:
            if i == j:
                count += 1
        result += i*count


    print(result)


if __name__ == "__main__":
    part1()
    part2()