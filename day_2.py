def main():
    file = open("day_2_input_test.txt")
    print(part_1(file))
    file.close()
    return


def part_1(file):
    input_list = input_to_list(file)
    safe = 0
    for line in input_list:
        if check_diff_and_dir(line):
            safe += 1
    return safe


def check_diff_and_dir(line):
    previous = 0
    for i in range(len(line) - 1):
        difference = line[i] - line[i + 1]
        # check if the difference is not in the safe range
        if not 1 <= abs(difference) <= 3:
            print("Unsafe 1")
            return False
        # check that the sign of the current difference is the same as the previous difference
        if previous == 0 or previous < 0 and difference < 0 or previous > 0 and difference > 0:
            previous = difference
        else:
            print("Unsafe 2")
            return False
    # if both valid
    print("Safe")
    return True


def input_to_list(file):
    input_list = []
    for line in file:
        input_list.append(list(map(int, line.split())))
    return input_list

if __name__ == "__main__":
    main()