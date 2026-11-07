from typing import List

def part1(texts: List[str]) -> int:
    count = 0
    for text in texts:
        has_double = any(text[i] == text[i+1] for i in range(len(text) - 1))
        has_forbidden = any(sub in text for sub in ["ab", "cd", "pq", "xy"])
        vowels = sum(1 for c in text if c in "aeiou") >= 3
        if vowels and has_double and not has_forbidden:
            count += 1
    return count

def part2(texts: List[str]) -> int:
    count = 0
    for text in texts:
        has_pair = any(text[i : i + 2] in text[i + 2 :] for i in range(len(text) - 2))
        has_sandwich = any(text[i] == text[i + 2] for i in range(len(text) - 2))
        if has_pair and has_sandwich:
            count += 1
    return count

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
        print(part1(lines))
        print(part2(lines))
    f.close()