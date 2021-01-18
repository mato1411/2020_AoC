# --- Day 5: Binary Boarding ---
# You board your plane only to discover a new problem: you dropped your boarding pass! You aren't sure which seat is yours, and all of the flight attendants are busy with the flood of people that suddenly made it through passport control.
#
# You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input); perhaps you can find your seat through process of elimination.
#
# Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".
#
# The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.
#
# For example, consider just the first seven characters of FBFBBFFRLR:
#
# Start by considering the whole range, rows 0 through 127.
# F means to take the lower half, keeping rows 0 through 63.
# B means to take the upper half, keeping rows 32 through 63.
# F means to take the lower half, keeping rows 32 through 47.
# B means to take the upper half, keeping rows 40 through 47.
# B keeps rows 44 through 47.
# F keeps rows 44 through 45.
# The final F keeps the lower of the two, row 44.
# The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.
#
# For example, consider just the last 3 characters of FBFBBFFRLR:
#
# Start by considering the whole range, columns 0 through 7.
# R means to take the upper half, keeping columns 4 through 7.
# L means to take the lower half, keeping columns 4 through 5.
# The final R keeps the upper of the two, column 5.
# So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.
#
# Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.
#
# Here are some other boarding passes:
#
# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.
# As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?
#
# Your puzzle answer was 926.
#
# --- Part Two ---
# Ding! The "fasten seat belt" signs have turned on. Time to find your seat.
#
# It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.
#
# Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.
#
# What is the ID of your seat?
#
# Your puzzle answer was 657.
#
# Both parts of this puzzle are complete! They provide two gold stars: **


def get_row(seat_decoded):
    row_min = 0
    row_max = 127
    for i in range(0, 7):
        diff = row_max - row_min
        if seat_decoded[i] == 'F':
            row_max = diff//2 + row_min
        elif seat_decoded[i] == 'B':
            row_min = (diff+1)//2 + row_min

        #print("row_min: ", row_min)
        #print("row_max: ", row_max)

    if row_min == row_max:
        return row_min


def get_col(seat_decoded):
    col_min = 0
    col_max = 7
    for i in range(7, 10):
        diff = col_max - col_min
        if seat_decoded[i] == 'L':
            col_max = diff // 2 + col_min
        elif seat_decoded[i] == 'R':
            col_min = (diff + 1) // 2 + col_min

        #print("col_min: ", col_min)
        #print("col_max: ", col_max)

    if col_min == col_max:
        return col_min


if __name__ == '__main__':

    files = ['20201205-example.txt', '20201205-input.txt']

    for file_name in files:
        print("\n" + file_name)
        with open(file_name) as f:
            seats = f.readlines()

        seats_decoded = {}
        for i in range(len(seats)):
            seat = seats[i].strip()
            seats_encoded = {'row': get_row(seat), 'col': get_col(seat)}
            seats_encoded['seat_id'] = seats_encoded['row'] * 8 + seats_encoded['col']
            seats_decoded[seat] = seats_encoded
            #print("seats_encoded: ", seats_encoded)
        #print("seats_decoded: ", seats_decoded)

        # Your seat wasn't at the very front or back, though;
        # Ignore first (0) and last row (127)
        seat_map = [[0 for i in range(0, 8)] for j in range(1, 127)]

        highest_seat_id = 0
        for seat_dec, seats_enc in seats_decoded.items():
            current_seat_id = seats_enc.get('seat_id')
            if highest_seat_id < current_seat_id:
                highest_seat_id, h_row, h_col= current_seat_id, seats_enc.get('row'), seats_enc.get('col')
            seat_map[seats_enc.get('row')][seats_enc.get('col')] = 1

        print("Part One: Highest seat id: {}, row: {}, col: {}".format(highest_seat_id, h_row, h_col))

        row_counter = 0
        for row in seat_map:
            col = 0
            while col <= 7:
                if row[col] == 0:
                    seat_id = row_counter * 8 + col
                    # Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.
                    if len([seats_enc.get('seat_id') for seats_enc in seats_decoded.values() if seat_id -1 <= seats_enc.get('seat_id') <= seat_id +1]) == 2:
                        print("Part Two: Free seat at row {} and col {} with ID {}.".format(row_counter, col, seat_id))
                        break
                col += 1
            row_counter += 1
