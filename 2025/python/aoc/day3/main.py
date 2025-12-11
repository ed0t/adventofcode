def process_line(line, r=-11):
    line = line.strip()
    digits = []
    ints = list(map(int, line))
    for x in range(r, 1):
        if x == 0:
            left = max(ints)
            digits.append(left)
        else:
            left = max(ints[:x])
            digits.append(left)
            left_pos = ints.index(left)
            ints = ints[left_pos + 1:]
    return int("".join(map(str, digits)))


def process_lines(lines, r):
    return sum(process_line(line, r) for line in lines)


def readfile(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line


if __name__ == '__main__':
    result = process_lines(readfile("input.txt"), -11)
    print(result)
