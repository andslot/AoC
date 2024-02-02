import re
result = 0
rep = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
string_fix = {"one": "onee", "two": "twoo", "five": "fivee", "seven": "sevenn", "eight": "eightt", "nine": "ninee"}
rep = dict((re.escape(k), v) for k, v in rep.items())
string_fix = dict((re.escape(k), v) for k, v in string_fix.items())
pattern = re.compile("|".join(rep.keys()))
fix_pattern = re.compile("|".join(string_fix.keys()))
for line in open("input.txt", "r"):
    line = fix_pattern.sub(lambda m: string_fix[re.escape(m.group(0))], line)
    # print(line)
    numbers = pattern.sub(lambda m: rep[re.escape(m.group(0))], line)
    # print(numbers)
    numbers = re.sub("[a-z]*|\\n", "", numbers)
    # print(numbers)
    result += int(numbers[0] + numbers[-1])
print(result)