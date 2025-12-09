from pathlib import Path
import math

data_path = Path(__file__).parent / "input.txt"

list_of_batts = data_path.read_text().splitlines() 


def main(): 
    total = 0 
    for battery_string in list_of_batts:
        starting_int = 0 
        digits_left = 11
        joltage_string = ""
        index_of_first_int = -1 
        for x in range(0, len(battery_string)-11):
            current_int = int(battery_string[x])
            if current_int > starting_int:
                starting_int = current_int
                index_of_first_int = x

        joltage_string = joltage_string + (str(starting_int))
        current_last_index = index_of_first_int

        print("the current line is ", battery_string, " and the first int is ", starting_int, )

        while digits_left > 0:
            next_higest_int, next_highest_index = find_highest_int(battery_string, current_last_index + 1, digits_left)
            # print ("the output of the find higest int fucntion is ",  find_highest_int(battery_string, index_of_first_int, i), "\n")
            joltage_string = joltage_string + str(next_higest_int)
            current_last_index = next_highest_index
            
            print ("the current joltage string is ", joltage_string , "\n")
            digits_left -= 1 

        total += int(joltage_string)
    print(total)


def find_highest_int(current_line, index_of_last, nums_left):
    remaining_string = current_line[index_of_last : len(current_line)-nums_left + 1]
    print ("the remaining string is ", remaining_string)
    
    if not remaining_string:
        return 0, index_of_last
    
    highest_int = 1
    index_of_highest = index_of_last

    for i, char in enumerate(remaining_string):
        int_value = int(char)
        if int_value > highest_int:
            highest_int = int_value
            index_of_highest = index_of_last + i

    return highest_int, index_of_highest


main()
