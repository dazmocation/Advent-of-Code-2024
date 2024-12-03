def main():
    file = open("day_2_input.txt")
    print(part_1(file))
    file.close()
    return


def part_1(file):
    # scan line by line
    # check each difference
    # check each direction
    # if safe
        # return safe
    input_to_list(file)


def check_direction(previous, difference):
    # check that the sign of the current difference is the same as the previous difference
    for i in range(len(line) - 1):
        difference = line[i] - line[i + 1]
        if previous == 0:
            return True
        elif difference < 0 and previous < 0 or difference > 0 and previous > 0:
            return True
        else:
            return False

def check_difference():
    pass


def input_to_list(file):
    input_list = []
    for line in file:
        input_list.append(line.split())
<<<<<<< HEAD
=======
    print(input_list)
>>>>>>> 33c82b7 (created and verified input_to_list())
    return

if __name__ == "__main__":
    main()