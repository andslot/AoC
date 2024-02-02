def read_file():
    f = open("test.txt", "r").readlines()
    seeds = []
    destinations = {}
    seed_mapping = False
    for i, line in enumerate(f):
        line = line.rstrip()
        if i == 0:
            seeds = line.split(": ")[1].split(" ")
            continue
        if "to" in line:
            mapping = line.split(" ")[0]
            destinations[mapping] = []
            seed_mapping = True
            continue
        if seed_mapping:
            dest_start, source_start, range_len = line.split(" ")
            for j in range(int(range_len)):
                print(j)
                destinations[mapping].append({int(source_start) + j: int(dest_start) + j})
                continue
                # locations.append(([int(dest_start) + d for d in range(int(range_len))], [int(source_start) + s for s in range(int(range_len))]))
        if " " in line:
            seed_mapping = False
    return seeds, destinations

def part1():
    result = float('inf')
    seeds, destinations = read_file()
    print(destinations)
    # for seed in seeds:
        # if int(seed) in locations.keys():
        #     result = min(result, locations[int(seed)])
    # return result

if __name__ == "__main__":
    print(part1())