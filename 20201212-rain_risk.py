# --- Day 12: Rain Risk ---
# Your ferry made decent progress toward the island, but the storm came in faster than anyone expected. The ferry needs to take evasive actions!
#
# Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route directly to safety, it produced extremely circuitous instructions. When the captain uses the PA system to ask if anyone can help, you quickly volunteer.
#
# The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with integer input values. After staring at them for a few minutes, you work out what they probably mean:
#
# Action N means to move north by the given value.
# Action S means to move south by the given value.
# Action E means to move east by the given value.
# Action W means to move west by the given value.
# Action L means to turn left the given number of degrees.
# Action R means to turn right the given number of degrees.
# Action F means to move forward by the given value in the direction the ship is currently facing.
# The ship starts by facing east. Only the L and R actions change the direction the ship is facing. (That is, if the ship is facing east and the next instruction is N10, the ship would move north 10 units, but would still move east if the following action were F.)
#
# For example:
#
# F10
# N3
# F7
# R90
# F11
# These instructions would be handled as follows:
#
# F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
# N3 would move the ship 3 units north to east 10, north 3.
# F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
# R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
# F11 would move the ship 11 units south to east 17, south 8.
# At the end of these instructions, the ship's Manhattan distance (sum of the absolute values of its east/west position and its north/south position) from its starting position is 17 + 8 = 25.
#
# Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's starting position?
#
# Your puzzle answer was 1838.
#
# --- Part Two ---
# Before you can give the destination to the captain, you realize that the actual action meanings were printed on the back of the instructions the whole time.
#
# Almost all of the actions indicate how to move a waypoint which is relative to the ship's position:
#
# Action N means to move the waypoint north by the given value.
# Action S means to move the waypoint south by the given value.
# Action E means to move the waypoint east by the given value.
# Action W means to move the waypoint west by the given value.
# Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
# Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
# Action F means to move forward to the waypoint a number of times equal to the given value.
# The waypoint starts 10 units east and 1 unit north relative to the ship. The waypoint is relative to the ship; that is, if the ship moves, the waypoint moves with it.
#
# For example, using the same instructions as above:
#
# F10 moves the ship to the waypoint 10 times (a total of 100 units east and 10 units north), leaving the ship at east 100, north 10. The waypoint stays 10 units east and 1 unit north of the ship.
# N3 moves the waypoint 3 units north to 10 units east and 4 units north of the ship. The ship remains at east 100, north 10.
# F7 moves the ship to the waypoint 7 times (a total of 70 units east and 28 units north), leaving the ship at east 170, north 38. The waypoint stays 10 units east and 4 units north of the ship.
# R90 rotates the waypoint around the ship clockwise 90 degrees, moving it to 4 units east and 10 units south of the ship. The ship remains at east 170, north 38.
# F11 moves the ship to the waypoint 11 times (a total of 44 units east and 110 units south), leaving the ship at east 214, south 72. The waypoint stays 4 units east and 10 units south of the ship.
# After these operations, the ship's Manhattan distance from its starting position is 214 + 72 = 286.
#
# Figure out where the navigation instructions actually lead. What is the Manhattan distance between that location and the ship's starting position?
#
# Your puzzle answer was 89936.
#
# Both parts of this puzzle are complete! They provide two gold stars: **


def process_instructions():
    global route_list
    global instruction_list
    global l_is_east_dict, l_is_west_dict, l_is_south_dict, l_is_north_dict
    global r_is_east_dict, r_is_west_dict, r_is_south_dict, r_is_north_dict

    for i in instruction_list:

        current_pos = route_list[-1]

        x = current_pos.get('x')
        x_dir = x[:1]
        x_val = int(x[1:])

        y = current_pos.get('y')
        y_dir = y[:1]
        y_val = int(y[1:])

        dir = current_pos.get('direction')

        # N means to move north by the given value.
        if i.get('action') == 'N':

            if y_dir == 'N':
                y_val += i.get('value')
            elif y_dir == 'S':
                y_val -= i.get('value')
                if y_val < 0:
                    y_val *= -1
                    y_dir = 'N'

        # Action S means to move south by the given value.
        elif i.get('action') == 'S':

            if y_dir == 'S':
                y_val += i.get('value')
            elif y_dir == 'N':
                y_val -= i.get('value')
                if y_val < 0:
                    y_val *= -1
                    y_dir = 'S'

        # Action E means to move east by the given value.
        elif i.get('action') == 'E':

            if x_dir == 'E':
                x_val += i.get('value')
            elif x_dir == 'W':
                x_val -= i.get('value')
                if x_val < 0:
                    x_val *= -1
                    x_dir = 'E'

        # Action W means to move west by the given value.
        elif i.get('action') == 'W':

            if x_dir == 'W':
                x_val += i.get('value')
            elif x_dir == 'E':
                x_val -= i.get('value')
                if x_val < 0:
                    x_val *= -1
                    x_dir = 'W'

        # Action L means to turn left the given number of degrees.
        elif i.get('action') == 'L':

            if dir == 'N':
                dir = l_is_north_dict.get(i.get('value'))
            elif dir == 'S':
                dir = l_is_south_dict.get(i.get('value'))
            elif dir == 'E':
                dir = l_is_east_dict.get(i.get('value'))
            elif dir == 'W':
                dir = l_is_west_dict.get(i.get('value'))

        # Action R means to turn right the given number of degrees.
        elif i.get('action') == 'R':

            if dir == 'N':
                dir = r_is_north_dict.get(i.get('value'))
            elif dir == 'S':
                dir = r_is_south_dict.get(i.get('value'))
            elif dir == 'E':
                dir = r_is_east_dict.get(i.get('value'))
            elif dir == 'W':
                dir = r_is_west_dict.get(i.get('value'))

        # Action F means to move forward by the given value in the direction the ship is currently facing.
        elif i.get('action') == 'F':

            if dir == 'N':
                if y_dir == 'N':
                    y_val += i.get('value')
                elif y_dir == 'S':
                    y_val -= i.get('value')
                    if y_val < 0:
                        y_val *= -1
                        y_dir = 'N'
            elif dir == 'S':
                if y_dir == 'S':
                    y_val += i.get('value')
                elif y_dir == 'N':
                    y_val -= i.get('value')
                    if y_val < 0:
                        y_val *= -1
                        y_dir = 'S'
            elif dir == 'E':
                if x_dir == 'E':
                    x_val += i.get('value')
                elif x_dir == 'W':
                    x_val -= i.get('value')
                    if x_val < 0:
                        x_val *= -1
                        x_dir = 'E'
            elif dir == 'W':
                if x_dir == 'W':
                    x_val += i.get('value')
                elif x_dir == 'E':
                    x_val -= i.get('value')
                    if x_val < 0:
                        x_val *= -1
                        x_dir = 'W'

        else:
            print("ERROR: Failed")
            return

        new_pos = {'direction': dir, 'x': x_dir + str(x_val), 'y': y_dir + str(y_val)}
        route_list.append(new_pos)


def process_instructions2():
    global waypoint_list
    global ship_pos_list
    global instruction_list

    global l_is_east_dict, l_is_west_dict, l_is_south_dict, l_is_north_dict
    global r_is_east_dict, r_is_west_dict, r_is_south_dict, r_is_north_dict

    counter = 0

    for i in instruction_list:

        counter += 1

        current_ship_pos = ship_pos_list[-1]

        x = current_ship_pos.get('x')
        x_dir = x[:1]
        x_val = int(x[1:])

        y = current_ship_pos.get('y')
        y_dir = y[:1]
        y_val = int(y[1:])

        current_waypoint_pos = waypoint_list[-1]

        xw = current_waypoint_pos.get('x')
        xw_dir = xw[:1]
        xw_val = int(xw[1:])

        yw = current_waypoint_pos.get('y')
        yw_dir = yw[:1]
        yw_val = int(yw[1:])

        # Action N means to move the waypoint north by the given value.
        if i.get('action') == 'N':

            if yw_dir == 'N':
                yw_val += i.get('value')
            elif yw_dir == 'S':
                yw_val -= i.get('value')
                if yw_val < 0:
                    yw_val *= -1
                    yw_dir = 'N'

        # Action S means to move the waypoint south by the given value.
        elif i.get('action') == 'S':

            if yw_dir == 'S':
                yw_val += i.get('value')
            elif yw_dir == 'N':
                yw_val -= i.get('value')
                if yw_val < 0:
                    yw_val *= -1
                    yw_dir = 'S'

        # Action E means to move the waypoint east by the given value.
        elif i.get('action') == 'E':

            if xw_dir == 'E':
                xw_val += i.get('value')
            elif xw_dir == 'W':
                xw_val -= i.get('value')
                if xw_val < 0:
                    xw_val *= -1
                    xw_dir = 'E'

        # Action W means to move the waypoint west by the given value.
        elif i.get('action') == 'W':

            if xw_dir == 'W':
                xw_val += i.get('value')
            elif xw_dir == 'E':
                xw_val -= i.get('value')
                if xw_val < 0:
                    xw_val *= -1
                    xw_dir = 'W'

        # Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
        # Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
        elif i.get('action') == 'L' or i.get('action') == 'R':

            if i.get('action') == 'L':
                is_north_dict = l_is_north_dict
                is_south_dict = l_is_south_dict
                is_east_dict = l_is_east_dict
                is_west_dict = l_is_west_dict
            elif i.get('action') == 'R':
                is_north_dict = r_is_north_dict
                is_south_dict = r_is_south_dict
                is_east_dict = r_is_east_dict
                is_west_dict = r_is_west_dict

            tmp_xw_dir = xw_dir
            tmp_xw_val = xw_val
            tmp_yw_dir = yw_dir
            tmp_yw_val = yw_val

            if i.get('value') == 90 or i.get('value') == 270:

                if tmp_yw_dir == 'N':
                    xw_dir = is_north_dict.get(i.get('value'))
                elif tmp_yw_dir == 'S':
                    xw_dir = is_south_dict.get(i.get('value'))

                if tmp_xw_dir == 'E':
                    yw_dir = is_east_dict.get(i.get('value'))
                elif tmp_xw_dir == 'W':
                    yw_dir = is_west_dict.get(i.get('value'))

                xw_val = tmp_yw_val
                yw_val = tmp_xw_val

            elif i.get('value') == 180:

                if tmp_yw_dir == 'N':
                    yw_dir = is_north_dict.get(i.get('value'))
                elif tmp_yw_dir == 'S':
                    yw_dir = is_south_dict.get(i.get('value'))

                if tmp_xw_dir == 'E':
                    xw_dir = is_east_dict.get(i.get('value'))
                elif tmp_xw_dir == 'W':
                    xw_dir = is_west_dict.get(i.get('value'))

        # Action F means to move forward by the given value in the direction the ship is currently facing.
        elif i.get('action') == 'F':

            xmove = xw_val * i.get('value')
            ymove = yw_val * i.get('value')

            if yw_dir == 'N':
                if y_dir == 'N':
                    y_val += ymove
                elif y_dir == 'S':
                    y_val -= ymove
                    if y_val < 0:
                        y_val *= -1
                        y_dir = 'N'
            elif yw_dir == 'S':
                if y_dir == 'S':
                    y_val += ymove
                elif y_dir == 'N':
                    y_val -= ymove
                    if y_val < 0:
                        y_val *= -1
                        y_dir = 'S'

            if xw_dir == 'E':
                if x_dir == 'E':
                    x_val += xmove
                elif x_dir == 'W':
                    x_val -= xmove
                    if x_val < 0:
                        x_val *= -1
                        x_dir = 'E'
            elif xw_dir == 'W':
                if x_dir == 'W':
                    x_val += xmove
                elif x_dir == 'E':
                    x_val -= xmove
                    if x_val < 0:
                        x_val *= -1
                        x_dir = 'W'

        else:
            print("ERROR: Failed")
            return

        new_ship_pos = {'x': x_dir + str(x_val), 'y': y_dir + str(y_val)}
        new_waypoint_pos = {'x': xw_dir + str(xw_val), 'y': yw_dir + str(yw_val)}

        #print("new_ship_pos: ", new_ship_pos)
        #print("new_waypoint_pos: ", new_waypoint_pos)

        ship_pos_list.append(new_ship_pos)
        waypoint_list.append(new_waypoint_pos)



if __name__ == '__main__':

    files = ['20201212-example.txt', '20201212-input.txt']

    for file_name in files:
        print("\n****************************\n" + file_name)
        with open(file_name) as f:
            instructions = f.readlines()

        len_instructions = len(instructions)
        #print("len_instructions :", len_instructions)

        instruction_count = 0
        instruction_list = []

        while instruction_count < len_instructions:
            instruction_dict = {}
            #print("instructions[instruction_count]: ", instructions[instruction_count].strip())
            instruction = instructions[instruction_count].strip()
            #print("instruction: ", instruction)
            instruction_dict['pos'] = instruction_count
            instruction_dict['action'] = instruction[:1]
            instruction_dict['value'] = int(instruction[1:])
            # [ { pos: 0, action: N, value: 3}, ... ]
            #print('instruction_dict: ', instruction_dict)
            instruction_list.append(instruction_dict)
            instruction_count += 1
        #print('instruction_list: ', instruction_list)

        # part one
        print("\npart one")

        l_is_east_dict = {90: 'N', 180: 'W', 270: 'S'}
        l_is_west_dict = {90: 'S', 180: 'E', 270: 'N'}
        l_is_south_dict = {90: 'E', 180: 'N', 270: 'W'}
        l_is_north_dict = {90: 'W', 180: 'S', 270: 'E'}

        r_is_east_dict = {90: 'S', 180: 'W', 270: 'N'}
        r_is_west_dict = {90: 'N', 180: 'E', 270: 'S'}
        r_is_south_dict = {90: 'W', 180: 'N', 270: 'E'}
        r_is_north_dict = {90: 'E', 180: 'S', 270: 'W'}

        route_list = [{'direction': 'E', 'x': "E0", 'y': "N0"}]
        #print('route_list:')
        #print("\n".join(str(j) for j in route_list))

        process_instructions()

        #print('route_list:')
        #print("\n".join(str(j) for j in route_list))
        print('route_list[-1]: ', route_list[-1])

        print("result: ", int(route_list[-1].get('x')[1:]) + int(route_list[-1].get('y')[1:]))

        # part two
        print("\npart two")

        ship_pos_list = [{'x': "E0", 'y': "N0"}]
        waypoint_list = [{'x': "E10", 'y': "N1"}]

        #print('ship_pos_list:')
        #print("\n".join(str(j) for j in ship_pos_list))

        #print('waypoint_list:')
        #print("\n".join(str(j) for j in waypoint_list))

        process_instructions2()

        #print('ship_pos_list:')
        #print("\n".join(str(j) for j in ship_pos_list))

        #print('waypoint_list:')
        #print("\n".join(str(j) for j in waypoint_list))

        print('ship_pos_list[-1]: ', ship_pos_list[-1])

        print("result: ", int(ship_pos_list[-1].get('x')[1:]) + int(ship_pos_list[-1].get('y')[1:]))
