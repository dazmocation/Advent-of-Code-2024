import re

def main():
    file = open("day_3_input.txt")
    file_as_string = str(file.read())
    print(part_1(file_as_string))
    print(part_2(file_as_string))
    file.close()


def part_1(file):
    matches = re.findall(r"mul\((\d+),(\d+)\)", file)
    sum = 0
    for item in matches:
        sum += int(item[0]) * int(item[1])
    return sum


def part_2(file):
    file = file.split("do()")
    sum = 0
    for i in file:
        i = i.split("don't()")[0]
        i = re.findall(r"mul\((\d+),(\d+)\)", i)
        for item in i:
            sum += int(item[0]) * int(item[1])
    return sum


if __name__ == "__main__":
    main()