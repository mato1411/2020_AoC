# --- Day 23: Crab Cups ---
# The small crab challenges you to a game! The crab is going to mix up some cups, and you have to predict where they'll end up.
#
# The cups will be arranged in a circle and labeled clockwise (your puzzle input). For example, if your labeling were 32415, there would be five cups in the circle; going clockwise around the circle from the first cup, the cups would be labeled 3, 2, 4, 1, 5, and then back to 3 again.
#
# Before the crab starts, it will designate the first cup in your list as the current cup. The crab is then going to do 100 moves.
#
# Each move, the crab does the following actions:
#
# The crab picks up the three cups that are immediately clockwise of the current cup. They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle.
# The crab selects a destination cup: the cup with a label equal to the current cup's label minus one. If this would select one of the cups that was just picked up, the crab will keep subtracting one until it finds a cup that wasn't just picked up. If at any point in this process the value goes below the lowest value on any cup's label, it wraps around to the highest value on any cup's label instead.
# The crab places the cups it just picked up so that they are immediately clockwise of the destination cup. They keep the same order as when they were picked up.
# The crab selects a new current cup: the cup which is immediately clockwise of the current cup.
# For example, suppose your cup labeling were 389125467. If the crab were to do merely 10 moves, the following changes would occur:
#
# -- move 1 --
# cups: (3) 8  9  1  2  5  4  6  7
# pick up: 8, 9, 1
# destination: 2
#
# -- move 2 --
# cups:  3 (2) 8  9  1  5  4  6  7
# pick up: 8, 9, 1
# destination: 7
#
# -- move 3 --
# cups:  3  2 (5) 4  6  7  8  9  1
# pick up: 4, 6, 7
# destination: 3
#
# -- move 4 --
# cups:  7  2  5 (8) 9  1  3  4  6
# pick up: 9, 1, 3
# destination: 7
#
# -- move 5 --
# cups:  3  2  5  8 (4) 6  7  9  1
# pick up: 6, 7, 9
# destination: 3
#
# -- move 6 --
# cups:  9  2  5  8  4 (1) 3  6  7
# pick up: 3, 6, 7
# destination: 9
#
# -- move 7 --
# cups:  7  2  5  8  4  1 (9) 3  6
# pick up: 3, 6, 7
# destination: 8
#
# -- move 8 --
# cups:  8  3  6  7  4  1  9 (2) 5
# pick up: 5, 8, 3
# destination: 1
#
# -- move 9 --
# cups:  7  4  1  5  8  3  9  2 (6)
# pick up: 7, 4, 1
# destination: 5
#
# -- move 10 --
# cups: (5) 7  4  1  8  3  9  2  6
# pick up: 7, 4, 1
# destination: 3
#
# -- final --
# cups:  5 (8) 3  7  4  1  9  2  6
# In the above example, the cups' values are the labels as they appear moving clockwise around the circle; the current cup is marked with ( ).
#
# After the crab is done, what order will the cups be in? Starting after the cup labeled 1, collect the other cups' labels clockwise into a single string with no extra characters; each number except 1 should appear exactly once. In the above example, after 10 moves, the cups clockwise from 1 are labeled 9, 2, 6, 5, and so on, producing 92658374. If the crab were to complete all 100 moves, the order after cup 1 would be 67384529.
#
# Using your labeling, simulate 100 moves. What are the labels on the cups after cup 1?
#
# Your puzzle answer was 52864379.
#
# --- Part Two ---
# Due to what you can only assume is a mistranslation (you're not exactly fluent in Crab), you are quite surprised when the crab starts arranging many cups in a circle on your raft - one million (1000000) in total.
#
# Your labeling is still correct for the first few cups; after that, the remaining cups are just numbered in an increasing fashion starting from the number after the highest number in your list and proceeding one by one until one million is reached. (For example, if your labeling were 54321, the cups would be numbered 5, 4, 3, 2, 1, and then start counting up from 6 until one million is reached.) In this way, every number from one through one million is used exactly once.
#
# After discovering where you made the mistake in translating Crab Numbers, you realize the small crab isn't going to do merely 100 moves; the crab is going to do ten million (10000000) moves!
#
# The crab is going to hide your stars - one each - under the two cups that will end up immediately clockwise of cup 1. You can have them if you predict what the labels on those cups will be when the crab is finished.
#
# In the above example (389125467), this would be 934001 and then 159792; multiplying these together produces 149245887792.
#
# Determine which two cups will end up immediately clockwise of cup 1. What do you get if you multiply their labels together?
#
# Your puzzle answer was 11591415792.
#
# Both parts of this puzzle are complete! They provide two gold stars: **
#
# At this point, you should return to your Advent calendar and try another puzzle.
#
# Your puzzle input was 318946572.


import time


# Refactored from list to dict, because of ten million moves in part 2, first list implementation in comments
def play_game(moves, cup_label, part_two):
    start = time.perf_counter()

    cup_list = [int(i) for i in list(cup_label)]
    if part_two:
        highest_value = 1000000
        cup_list += list(range(max(cup_list) + 1, highest_value + 1))

    highest_value = max(cup_list)

    # Keys = cup_list
    # Value = cup_list but starting from second value
    cup_dict = dict(zip(cup_list, cup_list[1:]))
    # Assign last value
    cup_dict[cup_list[-1]] = cup_list[0]

    current_move_value = cup_list[0]

    m = 0
    while m < moves:
        # len(cup_list) equals highest_value
        #index_circle = m % highest_value

        if part_two and m % 1000000 == 0:
            print("-- move {} --".format(m+1))
        elif not part_two:
            print("-- move {} --".format(m + 1))
            #print("cup_list: ", cup_list)
            print("cup_dict: ", cup_dict)

        #if not part_two:
        #    cups_str_list = "cups_list:"
        #    for i in range(highest_value):
        #        if i == index_circle or i == current_move_value:
        #            cups_str_list += " (" + str(cup_list[i]) + ")"
        #        else:
        #            cups_str_list += " " + str(cup_list[i])
        #    print(cups_str_list)

        #pick_up_list = cup_list[index_circle + 1:index_circle + 4]
        pick_up_dict = []

        next_pickup = current_move_value
        #print("next_pickup: ", next_pickup)
        for p in range(3):
            pick_up_dict.append(cup_dict.get(next_pickup))
            next_pickup = cup_dict.get(next_pickup)

        #pickup_missing_len = 3 - len(pick_up_list)
        #if pickup_missing_len != 0:
        #    pick_up_list += cup_list[:pickup_missing_len]

        #destination_not_determined_list = True
        #destination_list = cup_list[index_circle] - 1

        destination_not_determined_dict = True

        destination_dict_value = current_move_value -1

        #print("pick_up_list: ", pick_up_list)
        #print("destination_list: ", destination_list)

        #print("destination_dict_value: ", destination_dict_value)

        #while destination_not_determined_list:
        #    if destination_list not in cup_list:
        #        # Get highest value instead
        #        destination_list = highest_value
        #        #destination_not_determined = False
        #    elif destination_list in pick_up_list:
        #        destination_list -= 1
        #    else:
        #        destination_not_determined_list = False

        #print("pick_up_list: ", pick_up_list)
        #print("destination_list: ", destination_list)

        while destination_not_determined_dict:
            if destination_dict_value < 1:
                # Get highest value instead
                destination_dict_value = highest_value
                #destination_not_determined = False
            elif destination_dict_value in pick_up_dict:
                destination_dict_value -= 1
            else:
                destination_not_determined_dict = False

        if not part_two:
            print("pick up: ", pick_up_dict)
            print("destination: ", destination_dict_value)

        #print("destination_dict_value: ", destination_dict_value)

        # Add to current key the new value as follower
        cup_dict[current_move_value] = cup_dict.get(pick_up_dict[-1])
        #print("cup_dict[current_move_value] = cup_dict.get(pick_up_dict[-1]): ", cup_dict.get(pick_up_dict[-1]))
        # New key will be assigned as follower of last pick up key
        cup_dict[pick_up_dict[-1]] = cup_dict.get(destination_dict_value)
        #print("cup_dict[pick_up_dict[-1]] = cup_dict.get(destination_dict_value): ", cup_dict.get(destination_dict_value))
        # For new value add the first pick_up value
        cup_dict[destination_dict_value] = pick_up_dict[0]
        #print("cup_dict[destination_dict_value] = pick_up_dict[0]: ", pick_up_dict[0])
        # Update current_move_value
        current_move_value = cup_dict[current_move_value]
        #print("current_move_value = cup_dict[current_move_value]: ", cup_dict[current_move_value])

        #next_val_index = index_circle + 1 + 3
        #if  next_val_index >= highest_value:
        #    next_val_index = (highest_value - next_val_index) * -1

        #next_val_list = cup_list[next_val_index]
        #cup_list = cup_list[pickup_missing_len:index_circle + 1] + cup_list[index_circle + 4:]

        #destination_index_list = cup_list.index(destination_list)
        #cup_list = cup_list[:destination_index_list + 1] + pick_up_list + cup_list[destination_index_list + 1:]

        #offset_list = cup_list.index(next_val_list) - (index_circle + 1)
        #cup_list = cup_list[offset_list:] + cup_list[:offset_list]

        m += 1

    result = ""
    if part_two:
        result = [cup_dict.get(1), cup_dict.get(cup_dict.get(1))]
    else:
        k = 1
        for i in range(highest_value-1):
            result += str(cup_dict.get(k))
            k = cup_dict.get(k)
    end = time.perf_counter()
    print("duration: ", end - start)

    return result


if __name__ == '__main__':

    part_one_result_example_one = play_game(10, "389125467", False)
    part_one_result_example_two = play_game(100, "389125467", False)
    part_one_result = play_game(100, "318946572", False)

    print("part_one_result_example_one: ", part_one_result_example_one)
    print("part_one_result_example_two: ", part_one_result_example_two)
    print("part_one_result: ", part_one_result)

    assert "92658374" == part_one_result_example_one
    assert "67384529" == part_one_result_example_two
    assert "52864379" == part_one_result

    part_two_result_example = play_game(10000000, "389125467", True)
    print("part_two_result_example: ", part_two_result_example)
    product = part_two_result_example[0] * part_two_result_example[1]
    print("product: ", product)
    assert 934001 == part_two_result_example[0]
    assert 159792 == part_two_result_example[1]
    assert 149245887792 == product

    part_two_result = play_game(10000000, "318946572", True)
    print("part_two_result: ", part_two_result)
    product = part_two_result[0] * part_two_result[1]
    print("product: ", product)
