def first(inputs: str):
    up = inputs.count("(")
    down = inputs.count(")")
    return up - down

def second(inputs: str):
    m = {"(": 1, ")": -1}
    floor = 0
    for i, c in enumerate(inputs):
        floor += m[c]
        if floor < 0:
            return i+1

if __name__ == "__main__":
    with open("input.txt") as f:
        text = f.readline()
        print(first(text))
        print(second(text))