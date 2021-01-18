# --- Day 15: Rambunctious Recitation ---
# You catch the airport shuttle and try to book a new flight to your vacation island. Due to the storm, all direct flights have been cancelled, but a route is available to get around the storm. You take it.
#
# While you wait for your flight, you decide to check in with the Elves back at the North Pole. They're playing a memory game and are ever so excited to explain the rules!
#
# In this game, the players take turns saying numbers. They begin by taking turns reading from a list of starting numbers (your puzzle input). Then, each turn consists of considering the most recently spoken number:
#
# If that was the first time the number has been spoken, the current player says 0.
# Otherwise, the number had been spoken before; the current player announces how many turns apart the number is from when it was previously spoken.
# So, after the starting numbers, each turn results in that player speaking aloud either 0 (if the last number is new) or an age (if the last number is a repeat).
#
# For example, suppose the starting numbers are 0,3,6:
#
# Turn 1: The 1st number spoken is a starting number, 0.
# Turn 2: The 2nd number spoken is a starting number, 3.
# Turn 3: The 3rd number spoken is a starting number, 6.
# Turn 4: Now, consider the last number spoken, 6. Since that was the first time the number had been spoken, the 4th number spoken is 0.
# Turn 5: Next, again consider the last number spoken, 0. Since it had been spoken before, the next number to speak is the difference between the turn number when it was last spoken (the previous turn, 4) and the turn number of the time it was most recently spoken before then (turn 1). Thus, the 5th number spoken is 4 - 1, 3.
# Turn 6: The last number spoken, 3 had also been spoken before, most recently on turns 5 and 2. So, the 6th number spoken is 5 - 2, 3.
# Turn 7: Since 3 was just spoken twice in a row, and the last two turns are 1 turn apart, the 7th number spoken is 1.
# Turn 8: Since 1 is new, the 8th number spoken is 0.
# Turn 9: 0 was last spoken on turns 8 and 4, so the 9th number spoken is the difference between them, 4.
# Turn 10: 4 is new, so the 10th number spoken is 0.
# (The game ends when the Elves get sick of playing or dinner is ready, whichever comes first.)
#
# Their question for you is: what will be the 2020th number spoken? In the example above, the 2020th number spoken will be 436.
#
# Here are a few more examples:
#
# Given the starting numbers 1,3,2, the 2020th number spoken is 1.
# Given the starting numbers 2,1,3, the 2020th number spoken is 10.
# Given the starting numbers 1,2,3, the 2020th number spoken is 27.
# Given the starting numbers 2,3,1, the 2020th number spoken is 78.
# Given the starting numbers 3,2,1, the 2020th number spoken is 438.
# Given the starting numbers 3,1,2, the 2020th number spoken is 1836.
# Given your starting numbers, what will be the 2020th number spoken?
#
# Your puzzle answer was 981.
#
# --- Part Two ---
# Impressed, the Elves issue you a challenge: determine the 30000000th number spoken. For example, given the same starting numbers as above:
#
# Given 0,3,6, the 30000000th number spoken is 175594.
# Given 1,3,2, the 30000000th number spoken is 2578.
# Given 2,1,3, the 30000000th number spoken is 3544142.
# Given 1,2,3, the 30000000th number spoken is 261214.
# Given 2,3,1, the 30000000th number spoken is 6895259.
# Given 3,2,1, the 30000000th number spoken is 18.
# Given 3,1,2, the 30000000th number spoken is 362.
# Given your starting numbers, what will be the 30000000th number spoken?
#
# Your puzzle answer was 164878.
#
# Both parts of this puzzle are complete! They provide two gold stars: **


import time


# Working but too slow for part 2 so stop refactoring
def calc_spoken_number_for_turn(starting_numbers, turn_lookup):
    turns = []
    first_time_spoken = 0
    print_limit = 100000
    turn = 0

    last_pos_before_prev_cache = {}

    while turn < turn_lookup:
        # Start with starting numbers
        if turn < len(starting_numbers):
            spoken_number = starting_numbers[turn]
        else:
            last_spoken_number = turns[-1]
            #print("last_spoken_number: ", last_spoken_number)

            if turns.count(last_spoken_number) > 1:
                #print("last_pos_before_prev_cache: ", last_pos_before_prev_cache)

                if last_pos_before_prev_cache.get(last_spoken_number, 0) == 0:
                    reversed_range = reversed(range(0, len(turns)-1))
                    #print("reversed_range: ", list(reversed_range))
                    for t in reversed_range:
                        #print("t: ", t)
                        if turns[t] == last_spoken_number:
                            last_pos_before_prev_cache[last_spoken_number] = str(t) + "," + str(turn)
                            #print("last_pos_before_prev_cache: ", last_pos_before_prev_cache)
                            #print("t {} matches last_spoken_number {} in current turn {}".format(t, last_spoken_number, turn))
                            spoken_number = turn - 1 - t
                            break
                else:
                    last_t = int(last_pos_before_prev_cache.get(last_spoken_number).split(',')[1])
                    #print("turn: ", turn)
                    #print("last_t: ", last_t)
                    spoken_number = turn - last_t
                    last_pos_before_prev_cache[last_spoken_number] = str(turn-1) + ',' + str(turn)
                    #print("last_pos_before_prev_cache: ", last_pos_before_prev_cache)
            else:
                spoken_number = first_time_spoken

        #print("spoken_number: ", spoken_number)
        turns.append(spoken_number)
        turn += 1
        if turn % print_limit == 0:
            print("turn: ", turn)
    #print("turns: ", turns)
    #print("turns[-1]: ", turns[-1])
    #print("len_t_list: ", len_t_list)
    #print("max: ", max(len_t_list))
    return turns[-1]


def fast_calc_spoken_number_for_turn(numbers, stop):
    spoken = dict()

    turns_played = len(numbers)
    # Add starting numbers to dict
    # {0:1, 3:2, 6:3}
    # {8:1, 0:2, 17:3, 4:4, 1:5, 12:6}
    for turn in range(turns_played):
        # Key = number
        # Value = turn
        spoken[numbers[turn]] = turn + 1

    print("spoken: ", spoken)

    # Next is 0
    next_no = 0

    for turn in range(turns_played + 1, stop):
        # Was the number already spoken?
        if next_no in spoken.keys():
            # Yes, calculate new next number and store in temp variable
            # Next number = current turn count - turn count when the number was last spoken
            tmp_no = turn - spoken.get(next_no)
            # Now override when number was last spoken
            spoken[next_no] = turn
            # Assign tmp_no to next_no var for next iteration
            next_no = tmp_no
        else:
            # No, number was not spoken before. Add number as key with value turn count
            spoken[next_no] = turn
            # New next number will be 0
            next_no = 0
    return next_no


if __name__ == '__main__':

    start = time.perf_counter()

    starting_numbers = [8, 0, 17, 4, 1, 12] # 981, 164878
    #starting_numbers = [0, 3, 6] # 436, 175594
    #starting_numbers = [1, 3, 2] # 1, 2578
    #starting_numbers = [2, 1, 3] # 10, 3544142
    #starting_numbers = [1, 2, 3] # 27, 261214
    #starting_numbers = [2, 3, 1] # 78, 6895259
    #starting_numbers = [3, 2, 1] # 438, 18
    #starting_numbers = [3, 1, 2] # 1836, 362

    turn_lookup_part_one = 2020
    turn_lookup_part_two = 30000000

    part_one = calc_spoken_number_for_turn(starting_numbers, turn_lookup_part_one)
    print("part one: ", part_one)

    end = time.perf_counter()
    print("time: ", end - start)

    start = time.perf_counter()
    part_two = fast_calc_spoken_number_for_turn(starting_numbers, turn_lookup_part_two)
    print("part two: ", part_two)

    end = time.perf_counter()
    print("time: ", end - start)
