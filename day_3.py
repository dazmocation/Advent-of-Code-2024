import re

def main():
    file = open("day_3_input.txt")
    file_as_string = str(file.read())
    print(part_1(file_as_string))
    file.close()


def part_1(file):
    matches = re.findall(r"mul\((\d+),(\d+)\)", file)
    count = 0
    for item in matches:
        count += int(item[0]) * int(item[1])
    return count

if __name__ == "__main__":
    main()