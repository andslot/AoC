def part1():
    sum = 0
    for line in open("input.txt", "r").readlines():
        numbers = line.split(": ")[1]
        winner_cards, my_cards = numbers.split(" | ")
        i = -1
        points = 0
        for card in [int(m_card.strip()) for m_card in my_cards.split(" ") if m_card not in " "]:
            i += 1 if card in [int(w_card.strip()) for w_card in winner_cards.split(" ") if w_card not in " "] else 0
        points = 2**i if i != -1 else points
        sum += points
    return sum

def part2():
    f = open("input.txt", "r").readlines()
    n_cards = [1] * len(f)
    for i, line in enumerate(f):
        cards = line.split(": ")[1]
        winner_num, my_num = [[int(num.strip()) for num in nums.split(" ") if num not in " "] for nums in cards.split(" | ")]
        wins = 0
        for num in my_num:
            wins += 1 if num in winner_num else 0
        for j in range(i + 1, i + wins + 1):
            n_cards[j] += n_cards[i]
    return sum(n_cards)


if __name__ == "__main__": 
    print(part1())
    print(part2())