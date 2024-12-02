def main():
    left_list, right_list = separate_and_sort()
    
    print(part_1(left_list, right_list))
    print(part_2(left_list, right_list))

    file.close()
    return None

    
def part_1(left_list, right_list):
    # Find the difference between the corresponding numbers in each list
    # Find the sum of those differences
    total_distance = 0
    for i in range(len(left_list)):
        distance = abs(left_list[i] - right_list[i])
        total_distance += distance
    
    return total_distance


def part_2(left_list, right_list):
    # Multiply each number in the left list by the number of times it shows up in the right list
    # Add those products together
    similarity_score = 0
    for i in range(len(left_list)):
        similarity_score += (left_list[i] * right_list.count(left_list[i]))
    
    return similarity_score


def separate_and_sort():
    # Split a file into two lists
    # Sort the lists
    left_list = []
    right_list = []
    
    for line in file:
        left_list.append(int(line[0:5]))
        right_list.append(int(line[8:13]))
    left_list.sort()
    right_list.sort()
    
    return left_list, right_list


if __name__ == "__main__":
    file = open("day_1_input.txt")
    main()