# --- Day 11: Seating System ---
# Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!
#
# By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).
#
# The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). For example, the initial seat layout might look like this:
#
# L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL
# Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:
#
# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.
# Floor (.) never changes; seats don't move, and nobody sits on the floor.
#
# After one round of these rules, every seat in the example layout becomes occupied:
#
# #.##.##.##
# #######.##
# #.#.#..#..
# ####.##.##
# #.##.##.##
# #.#####.##
# ..#.#.....
# ##########
# #.######.#
# #.#####.##
# After a second round, the seats with four or more occupied adjacent seats become empty again:
#
# #.LL.L#.##
# #LLLLLL.L#
# L.L.L..L..
# #LLL.LL.L#
# #.LL.LL.LL
# #.LLLL#.##
# ..L.L.....
# #LLLLLLLL#
# #.LLLLLL.L
# #.#LLLL.##
# This process continues for three more rounds:
#
# #.##.L#.##
# #L###LL.L#
# L.#.#..#..
# #L##.##.L#
# #.##.LL.LL
# #.###L#.##
# ..#.#.....
# #L######L#
# #.LL###L.L
# #.#L###.##
# #.#L.L#.##
# #LLL#LL.L#
# L.L.L..#..
# #LLL.##.L#
# #.LL.LL.LL
# #.LL#L#.##
# ..L.L.....
# #L#LLLL#L#
# #.LLLLLL.L
# #.#L#L#.##
# #.#L.L#.##
# #LLL#LL.L#
# L.#.L..#..
# #L##.##.L#
# #.#L.LL.LL
# #.#L#L#.##
# ..L.L.....
# #L#L##L#L#
# #.LLLLLL.L
# #.#L#L#.##
# At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count 37 occupied seats.
#
# Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?
#
# To begin, get your puzzle input.
#
# Your puzzle answer was 2289.
#
# The first half of this puzzle is complete! It provides one gold star: *
#
# --- Part Two ---
# As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats - they care about the first seat they can see in each of those eight directions!
#
# Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight directions. For example, the empty seat below would see eight occupied seats:
#
# .......#.
# ...#.....
# .#.......
# .........
# ..#L....#
# ....#....
# .........
# #........
# ...#.....
# The leftmost empty seat below would only see one empty seat, but cannot see any of the occupied ones:
#
# .............
# .L.L.#.#.#.#.
# .............
# The empty seat below would see no occupied seats:
#
# .##.##.
# #.#.#.#
# ##...##
# ...L...
# ##...##
# #.#.#.#
# .##.##.
# Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats for an occupied seat to become empty (rather than four or more from the previous rules). The other rules still apply: empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.
#
# Given the same starting layout as above, these new rules cause the seating area to shift around as follows:
#
# L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL
# #.##.##.##
# #######.##
# #.#.#..#..
# ####.##.##
# #.##.##.##
# #.#####.##
# ..#.#.....
# ##########
# #.######.#
# #.#####.##
# #.LL.LL.L#
# #LLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLL#
# #.LLLLLL.L
# #.LLLLL.L#
# #.L#.##.L#
# #L#####.LL
# L.#.#..#..
# ##L#.##.##
# #.##.#L.##
# #.#####.#L
# ..#.#.....
# LLL####LL#
# #.L#####.L
# #.L####.L#
# #.L#.L#.L#
# #LLLLLL.LL
# L.L.L..#..
# ##LL.LL.L#
# L.LL.LL.L#
# #.LLLLL.LL
# ..L.L.....
# LLLLLLLLL#
# #.LLLLL#.L
# #.L#LL#.L#
# #.L#.L#.L#
# #LLLLLL.LL
# L.L.L..#..
# ##L#.#L.L#
# L.L#.#L.L#
# #.L####.LL
# ..#.#.....
# LLL###LLL#
# #.LLLLL#.L
# #.L#LL#.L#
# #.L#.L#.L#
# #LLLLLL.LL
# L.L.L..#..
# ##L#.#L.L#
# L.L#.LL.L#
# #.LLLL#.LL
# ..#.L.....
# LLL###LLL#
# #.LLLLL#.L
# #.L#LL#.L#
# Again, at this point, people stop shifting around and the seating area reaches equilibrium. Once this occurs, you count 26 occupied seats.
#
# Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached, how many seats end up occupied?
#
# Answer: 2059
# That's the right answer! You are one gold star closer to saving your vacation.
#
# You have completed Day 11!


import copy


def play_round_part_one(list_2d_input):
    row_counter = 0

    len_row = len(list_2d_input)
    len_col = len(list_2d_input[row_counter])

    global list_output

    while row_counter < len_row:
        #print("row_counter: ", row_counter)
        col_counter = 0
        while col_counter < len_col:
            adjacent_occupied_count = 0
            for r in range(row_counter - 1, row_counter + 2):
                for c in range(col_counter - 1, col_counter + 2):
                    #print("r: ", r)
                    #print("row_counter:", row_counter)
                    #print("c: ", c)
                    #print("col_counter: ", col_counter)
                    #print("list_2d[r][c]: ", list_2d[r][c])
                    if 0 <= r < len_row and 0 <= c < len_col and (r != row_counter or c != col_counter) and list_2d_input[r][c] == '#':
                        #print("c: ", c)
                        #print("r: ", r)
                        adjacent_occupied_count += 1
                        #print("adjacent_occupied_count: ", adjacent_occupied_count)

            #print("list_2d[row_counter][col_counter]: ", list_2d_input[row_counter][col_counter])

            if list_2d_input[row_counter][col_counter] == '#' and adjacent_occupied_count >= 4:
                list_output[row_counter][col_counter] = 'L'

            if list_2d_input[row_counter][col_counter] == 'L' and adjacent_occupied_count == 0:
                list_output[row_counter][col_counter] = '#'

            #print("list_output: ", list_output)

            col_counter += 1
            #break
        row_counter += 1
        #break

    return list_output



def play_round_part_two(list_2d_input):
    row_counter = 0

    len_row = len(list_2d_input)
    len_col = len(list_2d_input[row_counter])

    global list_output

    directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    direction_words = ['left up', 'up', 'right up', 'left', 'right', 'left down', 'down', 'right down']

    while row_counter < len_row:
        col_counter = 0

        while col_counter < len_col:


            if list_2d_input[row_counter][col_counter] == '.':
                col_counter += 1
                continue

            #print("Base: {},{}: {}".format(row_counter, col_counter, list_2d_input[row_counter][col_counter]))

            adjacent_occupied_count = 0
            adjacent_empty_count = 0
            direction_index = 0

            for direction in directions:

                r = direction[0]
                c = direction[1]
                #print("Direction: ", direction)
                # Search seat in this direction
                # Only search when inside of array
                while True:
                    try:
                        if 0 <= row_counter + r < len_row and 0 <= col_counter + c < len_col:
                            # Is occupied?
                            #print("Search: {},{}: {}".format(row_counter + r, col_counter + c, list_2d_input[row_counter + r][col_counter + c]))
                            if list_2d_input[row_counter + r][col_counter + c] == '#':
                                # print("c: ", c)
                                # print("r: ", r)
                                adjacent_occupied_count += 1
                            # Is empty?
                            if list_2d_input[row_counter + r][col_counter + c] == 'L':
                                adjacent_empty_count += 1
                            # Stop searching occupied/empty in this direction, because is empty or occupied and not floor
                            if list_2d_input[row_counter + r][col_counter + c] != '.':
                                break
                        else:
                            break
                    except IndexError as e:
                        break

                    # Seat not found, search scale of -1/+1 more away from current seat
                    if direction_words[direction_index].find('up') >= 0:
                        r += -1

                    if direction_words[direction_index].find('down') >= 0:
                        r += 1

                    if direction_words[direction_index].find('left') >= 0:
                        c += -1

                    if direction_words[direction_index].find('right') >= 0:
                        c += 1

                direction_index += 1

            #print("adjacent_occupied_count: ", adjacent_occupied_count)
            #print("adjacent_empty_count: ", adjacent_empty_count)

            if list_2d_input[row_counter][col_counter] == '#' and adjacent_occupied_count >= 5:
                list_output[row_counter][col_counter] = 'L'

            if list_2d_input[row_counter][col_counter] == 'L' and adjacent_occupied_count == 0:
                list_output[row_counter][col_counter] = '#'

            #print("list_output: ", list_output)
            #print("list_output:\n", "\n".join(str(j) for j in list_output).replace(" ", "").replace(",", "").replace("[", "").replace("]", "").replace("'", ""))

            col_counter += 1
            #break
        row_counter += 1
        #break

    return list_output


if __name__ == '__main__':

    files = ['20201211-example.txt', '20201211-input.txt']

    for file_name in files:
        print("\n****************************\n" + file_name)
        with open(file_name) as f:
            waiting_area = f.readlines()

        len_waiting_area = len(waiting_area)
        #print("len_waiting_area :", len_waiting_area)

        waiting_area_count = 0

        width_waiting_area = len(waiting_area[waiting_area_count].strip())
        #print("width_waiting_area: ", width_waiting_area)

        rows, cols = (len_waiting_area, width_waiting_area)
        waiting_area_coordinates = [[0 for i in range(cols)] for j in range(rows)]

        for row in range(len(waiting_area)):
            #print("waiting_area[row]: ", waiting_area[row].strip())
            for col in range(width_waiting_area):
                waiting_area_coordinates[row][col] = waiting_area[row].strip()[col]

        #print("waiting_area: ", waiting_area)
        #print("waiting_area_coordinates: ", waiting_area_coordinates)

        print("\npart 1")

        #print("Create deepcopy of waiting_area_coordinates")
        list_input = copy.deepcopy(waiting_area_coordinates)
        list_output = [['.' for i in range(cols)] for j in range(rows)]

        #print("list_input: ", list_input)
        print("list_input:\n", "\n".join(str(j) for j in list_input))

        round_counter = 0
        lists_are_equal = False

        while not lists_are_equal:
            round_counter += 1
            #print("round_counter: ", round_counter)

            play_round_part_one(list_input)
            #print("list_output: ", list_output)
            #print("list_output:\n", "\n".join(str(j) for j in list_output))

            if list_input == list_output:
                lists_are_equal = True
            else:
                list_input = copy.deepcopy(list_output)
                #print("list_input: ", list_input)
                #print("list_input:\n", "\n".join(str(j) for j in list_input))

            #if round_counter == 2:
            #    break

        #print("list_input: ", list_input)
        #print("list_input:\n", "\n".join(str(j) for j in list_input))
        #print("list_output: ", list_output)
        print("\nlist_output:\n", "\n".join(str(j) for j in list_output))
        print("round_counter: ", round_counter)
        print("occupied_seats in list_output: ", len([n for j in list_output for n in j if n == '#']))

        print("\npart 2")

        #print("Create deepcopy of waiting_area_coordinates")
        list_input = copy.deepcopy(waiting_area_coordinates)
        list_output = [['.' for i in range(cols)] for j in range(rows)]

        #print("list_input: ", list_input)
        print("list_input:\n", "\n".join(str(j) for j in list_input).replace(" ", "").replace(",", "").replace("[", "").replace("]", "").replace("'", ""))

        round_counter = 0
        lists_are_equal = False

        while not lists_are_equal:
            round_counter += 1
            #print("round_counter: ", round_counter)

            play_round_part_two(list_input)
            #print("list_output: ", list_output)
            #print("list_output:\n", "\n".join(str(j) for j in list_output).replace(" ", "").replace(",", "").replace("[", "").replace("]", "").replace("'", ""))
            if list_input == list_output:
                lists_are_equal = True
            else:
                list_input = copy.deepcopy(list_output)
                #print("list_input: ", list_input)
                #print("list_input:\n", "\n".join(str(j) for j in list_input).replace(" ", "").replace(",", "").replace("[", "").replace("]", "").replace("'", ""))

            #if round_counter == 2:
            #    break

        #print("list_input: ", list_input)
        #print("list_input:\n", "\n".join(str(j) for j in list_input).replace(" ", "").replace(",", "").replace("[", "").replace("]", "").replace("'", ""))
        #print("list_output: ", list_output)
        print("\nlist_output:\n", "\n".join(str(j) for j in list_output).replace(" ", "").replace(",", "").replace("[", "").replace("]", "").replace("'", ""))
        print("round_counter: ", round_counter)
        print("occupied_seats in list_output: ", len([n for j in list_output for n in j if n == '#']))
