def main():
    file = open("day_2_input.txt")
    input_list = input_to_list(file)
    print(part_1(input_list))
    print(part_2(input_list))
    file.close()
    return


def part_1(input_list):
    safe = 0
    for line in input_list:
        if check_diff_and_dir(line):
            safe += 1
    return safe


def part_2(input_list):
    safe = 0
    for line in input_list:
        if check_diff_and_dir_2(line):
            safe += 1
    return safe


def check_diff_and_dir(line):
    previous = 0
    for i in range(len(line) - 1):
        difference = line[i] - line[i + 1]
        # check if the difference is not in the safe range
        if not 1 <= abs(difference) <= 3:
            return False
        # check that the sign of the current difference is the same as the previous difference
        if previous == 0 or previous < 0 and difference < 0 or previous > 0 and difference > 0:
            previous = difference
        else:
            return False
    # if both valid
    return True


def check_diff_and_dir_2(line):
    previous = 0
    for i in range(len(line) - 1):
        difference = line[i] - line[i + 1]
        # check if the difference is not in the safe range
        if not 1 <= abs(difference) <= 3:
            if check_damper(line) == False:
                return False
            else:
                return True
        # check that the sign of the current difference is the same as the previous difference
        if previous == 0 or previous < 0 and difference < 0 or previous > 0 and difference > 0:
            previous = difference
        else:
            if check_damper(line) == False:
                return False
            else:
                return True
    # if both valid
    return True


def check_damper(line):
    for i in range(len(line)):
        temp = line.pop(i)
        if check_diff_and_dir(line):
            return True
        else:
            line.insert(i, temp)
    return False


def input_to_list(file):
    input_list = []
    for line in file:
        input_list.append(list(map(int, line.split())))
    return input_list


if __name__ == "__main__":
    main()