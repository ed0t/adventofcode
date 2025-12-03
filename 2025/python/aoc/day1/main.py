import itertools
import string


def acc_fn(start, value):
    direction = value[0]
    amount = int(value[1:])
    if direction == "L":
        amount = amount * -1
    start = start + amount
    start = start % 100
    return start


def calculate(input):
    matches = itertools.accumulate(input, acc_fn, initial=50)
    value = sum(1 for i in matches if i == 0)
    return value


def acc_fn_level_2(accumulator, value):
    start = accumulator[0]
    counter = 0
    direction = value[0]
    amount = int(value[1:])

    # if the entry is bigger than 99 then increase the counter n times, with n is the number of full cycles.
    if amount > 99:
        counter += amount // 100
    # keep only the difference
    amount = amount - counter * 100

    if direction == "L":
        amount = amount * -1

    start = start + amount
    if start == 0:
        counter += 1
    if start < 1 and (start != amount):
        counter += (start // 100) * -1

    if start > 99 and (start != amount):
        counter += start // 100

    # compute the new value
    start = start % 100

    return start, counter


def calculate_level2(input):
    matches = itertools.accumulate(input, acc_fn_level_2, initial=(50, 0))
    value = sum(i[1] for i in matches)
    return value


def readfile(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line


if __name__ == '__main__':
    input = ["L68",
             "L30",
             "R48",
             "L5",
             "R60",
             "L55",
             "L1",
             "L99",
             "R14",
             "L82",
             ]
    total = calculate_level2(readfile("input.txt"))
    print(total)
