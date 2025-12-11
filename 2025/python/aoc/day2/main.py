import concurrent.futures
import itertools


def check_value(value):
    value_string = str(value)
    l = (len(value_string) // 2) + 1
    for i in range(1, l):
        batched = list(map(lambda x: "".join(x), itertools.batched(value_string, i)))
        if all(x == batched[0] for x in batched):
            return value
    return None


def check_ranges(left, right):
    for value in range(left, right + 1):
        if check_value(value):
            yield value


def check_input(input):
    left, right = map(int, input.split("-"))
    invalid_ids = []
    for id in check_ranges(left, right):
        invalid_ids.append(id)
    return invalid_ids


def process(input):
    invalid_ids = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        results = executor.map(check_input, input.split(","))
        for element in results:
            invalid_ids.extend(element)

    return sum(invalid_ids)


def readfile(filename):
    with open(filename, "r") as file:
        return file.readline()


if __name__ == '__main__':
    input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

    result = process(readfile("input.txt"))
    # 27469417404
    print(result)
