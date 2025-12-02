def part1(input_file: str):
    file = open(input_file, 'r')
    ranges = file.readline().strip().split(',')
    file.close()

    ranges = [tuple(map(int, r.split('-'))) for r in ranges]

    invalid_password = 0
    for r in ranges:
        for n in range(r[0], r[1] + 1):
            if len(str(n)) % 2 != 0:
                continue

            n_len = len(str(n))
            n1 = str(n)[: n_len // 2]
            n2 = str(n)[n_len // 2 :]
            if int(n1) == int(n2):
                invalid_password += n

    print(invalid_password)

def part2(input_file: str):
    file = open(input_file, 'r')
    ranges = file.readline().strip().split(',')
    file.close()

    ranges = [tuple(map(int, r.split('-'))) for r in ranges]

    invalid_password = 0
    for r in ranges:
        for n in range(r[0], r[1] + 1):
            n_len = len(str(n))

            for i in range(1, n_len):
                # check substring repeatings
                if str(n)[:i] * (n_len // i) == str(n):
                    invalid_password += n
                    break

    print(invalid_password)

if __name__ == "__main__":
    part1('./day2/input.txt')
    part2('./day2/input.txt')