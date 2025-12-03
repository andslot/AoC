

def part1(input_file):
    file = open(input_file, 'r')
    banks = [x for x in file.read().strip().split('\n')]

    joltage = 0 

    for bank in banks:
        max_digit = max(bank)
        best_result = 0
        for i in range(len(bank)):
            if bank[i] == max_digit:
                if i + 1 < len(bank):
                    remaining = bank[i + 1:]
                    max2 = max(remaining)
                    two_digit_num = int(max_digit + max2)
                    best_result = max(best_result, two_digit_num)
                else:
                    previous = bank[:i]
                    max2 = max(previous)
                    two_digit_num = int(max2 + max_digit)
                    best_result = max(best_result, two_digit_num)

        joltage += best_result
            
    return joltage


def part2(input_file):
    file = open(input_file, 'r')
    banks = [x for x in file.read().strip().split('\n')]

    joltage = 0

    for bank in banks:
        k = len(bank) - 12
        stack = []
        
        for digit in bank:
            while stack and k > 0 and stack[-1] < digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        while k > 0:
            stack.pop()
            k -= 1
        
        joltage += int(''.join(stack))

    return joltage


if __name__ == "__main__":
    input_file = "day3/input.txt"
    print("Part 1:", part1(input_file))
    print("Part 2:", part2(input_file))