# --- Day 17: Conway Cubes ---
# As your flight slowly drifts through the sky, the Elves at the Mythical Information Bureau at the North Pole contact you. They'd like some help debugging a malfunctioning experimental energy source aboard one of their super-secret imaging satellites.
# 
# The experimental energy source is based on cutting-edge technology: a set of Conway Cubes contained in a pocket dimension! When you hear it's having problems, you can't help but agree to take a look.
#
# The pocket dimension contains an infinite 3-dimensional grid. At every integer 3-dimensional coordinate (x,y,z), there exists a single cube which is either active or inactive.
#
# In the initial state of the pocket dimension, almost all cubes start inactive. The only exception to this is a small flat region of cubes (your puzzle input); the cubes in this region start in the specified active (#) or inactive (.) state.
#
# The energy source then proceeds to boot up by executing six cycles.
#
# Each cube only ever considers its neighbors: any of the 26 other cubes where any of their coordinates differ by at most 1. For example, given the cube at x=1,y=2,z=3, its neighbors include the cube at x=2,y=2,z=2, the cube at x=0,y=2,z=3, and so on.
#
# During a cycle, all cubes simultaneously change their state according to the following rules:
#
# If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
# If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
# The engineers responsible for this experimental energy source would like you to simulate the pocket dimension and determine what the configuration of cubes should be at the end of the six-cycle boot process.
#
# For example, consider the following initial state:
#
# .#.
# ..#
# ###
# Even though the pocket dimension is 3-dimensional, this initial state represents a small 2-dimensional slice of it. (In particular, this initial state defines a 3x3x1 region of the 3-dimensional space.)
#
# Simulating a few cycles from this initial state produces the following configurations, where the result of each cycle is shown layer-by-layer at each given z coordinate (and the frame of view follows the active cells in each cycle):
#
# Before any cycles:
#
# z=0
# .#.
# ..#
# ###
#
#
# After 1 cycle:
#
# z=-1
# #..
# ..#
# .#.
#
# z=0
# #.#
# .##
# .#.
#
# z=1
# #..
# ..#
# .#.
#
#
# After 2 cycles:
#
# z=-2
# .....
# .....
# ..#..
# .....
# .....
#
# z=-1
# ..#..
# .#..#
# ....#
# .#...
# .....
#
# z=0
# ##...
# ##...
# #....
# ....#
# .###.
#
# z=1
# ..#..
# .#..#
# ....#
# .#...
# .....
#
# z=2
# .....
# .....
# ..#..
# .....
# .....
#
#
# After 3 cycles:
#
# z=-2
# .......
# .......
# ..##...
# ..###..
# .......
# .......
# .......
#
# z=-1
# ..#....
# ...#...
# #......
# .....##
# .#...#.
# ..#.#..
# ...#...
#
# z=0
# ...#...
# .......
# #......
# .......
# .....##
# .##.#..
# ...#...
#
# z=1
# ..#....
# ...#...
# #......
# .....##
# .#...#.
# ..#.#..
# ...#...
#
# z=2
# .......
# .......
# ..##...
# ..###..
# .......
# .......
# .......
# After the full six-cycle boot process completes, 112 cubes are left in the active state.
#
# Starting with your given initial configuration, simulate six cycles. How many cubes are left in the active state after the sixth cycle?
#
# Your puzzle answer was 372.
#
# --- Part Two ---
# For some reason, your simulated results don't match what the experimental energy source engineers expected. Apparently, the pocket dimension actually has four spatial dimensions, not three.
#
# The pocket dimension contains an infinite 4-dimensional grid. At every integer 4-dimensional coordinate (x,y,z,w), there exists a single cube (really, a hypercube) which is still either active or inactive.
#
# Each cube only ever considers its neighbors: any of the 80 other cubes where any of their coordinates differ by at most 1. For example, given the cube at x=1,y=2,z=3,w=4, its neighbors include the cube at x=2,y=2,z=3,w=3, the cube at x=0,y=2,z=3,w=4, and so on.
#
# The initial state of the pocket dimension still consists of a small flat region of cubes. Furthermore, the same rules for cycle updating still apply: during each cycle, consider the number of active neighbors of each cube.
#
# For example, consider the same initial state as in the example above. Even though the pocket dimension is 4-dimensional, this initial state represents a small 2-dimensional slice of it. (In particular, this initial state defines a 3x3x1x1 region of the 4-dimensional space.)
#
# Simulating a few cycles from this initial state produces the following configurations, where the result of each cycle is shown layer-by-layer at each given z and w coordinate:
#
# Before any cycles:
#
# z=0, w=0
# .#.
# ..#
# ###
#
#
# After 1 cycle:
#
# z=-1, w=-1
# #..
# ..#
# .#.
#
# z=0, w=-1
# #..
# ..#
# .#.
#
# z=1, w=-1
# #..
# ..#
# .#.
#
# z=-1, w=0
# #..
# ..#
# .#.
#
# z=0, w=0
# #.#
# .##
# .#.
#
# z=1, w=0
# #..
# ..#
# .#.
#
# z=-1, w=1
# #..
# ..#
# .#.
#
# z=0, w=1
# #..
# ..#
# .#.
#
# z=1, w=1
# #..
# ..#
# .#.
#
#
# After 2 cycles:
#
# z=-2, w=-2
# .....
# .....
# ..#..
# .....
# .....
#
# z=-1, w=-2
# .....
# .....
# .....
# .....
# .....
#
# z=0, w=-2
# ###..
# ##.##
# #...#
# .#..#
# .###.
#
# z=1, w=-2
# .....
# .....
# .....
# .....
# .....
#
# z=2, w=-2
# .....
# .....
# ..#..
# .....
# .....
#
# z=-2, w=-1
# .....
# .....
# .....
# .....
# .....
#
# z=-1, w=-1
# .....
# .....
# .....
# .....
# .....
#
# z=0, w=-1
# .....
# .....
# .....
# .....
# .....
#
# z=1, w=-1
# .....
# .....
# .....
# .....
# .....
#
# z=2, w=-1
# .....
# .....
# .....
# .....
# .....
#
# z=-2, w=0
# ###..
# ##.##
# #...#
# .#..#
# .###.
#
# z=-1, w=0
# .....
# .....
# .....
# .....
# .....
#
# z=0, w=0
# .....
# .....
# .....
# .....
# .....
#
# z=1, w=0
# .....
# .....
# .....
# .....
# .....
#
# z=2, w=0
# ###..
# ##.##
# #...#
# .#..#
# .###.
#
# z=-2, w=1
# .....
# .....
# .....
# .....
# .....
#
# z=-1, w=1
# .....
# .....
# .....
# .....
# .....
#
# z=0, w=1
# .....
# .....
# .....
# .....
# .....
#
# z=1, w=1
# .....
# .....
# .....
# .....
# .....
#
# z=2, w=1
# .....
# .....
# .....
# .....
# .....
#
# z=-2, w=2
# .....
# .....
# ..#..
# .....
# .....
#
# z=-1, w=2
# .....
# .....
# .....
# .....
# .....
#
# z=0, w=2
# ###..
# ##.##
# #...#
# .#..#
# .###.
#
# z=1, w=2
# .....
# .....
# .....
# .....
# .....
#
# z=2, w=2
# .....
# .....
# ..#..
# .....
# .....
# After the full six-cycle boot process completes, 848 cubes are left in the active state.
#
# Starting with your given initial configuration, simulate six cycles in a 4-dimensional space. How many cubes are left in the active state after the sixth cycle?
#
# Your puzzle answer was 1896.
#
# Both parts of this puzzle are complete! They provide two gold stars: **


import pprint
import copy


def check_expected(expected_list):

    global output

    # print("All active in output: ")
    active_list = [o for o in output if o.get('state') == '#']
    # print("\n".join(sorted(str(a) for a in active_list)))

    expected_found = []
    expected_not_found = []
    active_not_expected = []

    for active in active_list:
        found = False
        for expected in expected_list:
            if active == expected:
                found = True
                break
        if found:
            expected_found.append(active)
        else:
            active_not_expected.append(active)

    for expected in expected_list:
        found = False
        for active in active_list:
            if expected == active:
                found = True
                break
        if not found:
            expected_not_found.append(expected)

    #print("Expected found: ")
    #print("\n".join(sorted(str(i) for i in expected_found)))

    #print("Expected not found: ")
    #print("\n".join(sorted(str(i) for i in expected_not_found)))

    #print("Active not expected: ")
    #print("\n".join(sorted(str(i) for i in active_not_expected)))

    if len(expected_found) != len(expected_list) and len(expected_not_found) > 0 and len(active_not_expected) > 0:
        print("ERROR: Expected coordinates do not match actual coordinates.")
        # exit()


def determine_neighbors(input_coordinates):
    global output
    global input

    #print("input_coordinates: ", input_coordinates)
    active_neighbors = 0
    count_total_neighbors = 0
    # Determine active neighbors for input_coordinates
    for i in input:
        if i.get('state') == '#':
            # x == x
            if i.get('x') == input_coordinates.get('x'):
                # y == y
                if i.get('y') == input_coordinates.get('y'):
                    # z == z
                    if i.get('z') == input_coordinates.get('z'):
                        # w == w + 1 or w == w -1
                        if i.get('w') == input_coordinates.get('w') - 1 or i.get('w') == input_coordinates.get('w') + 1:
                            # i coordinate is active
                            if i.get('state') == '#':
                                active_neighbors += 1
                                #print("i: ", i)
                                count_total_neighbors += 1
                    # all z: z == z-1 or z == z or z == z +1
                    elif i.get('z') == input_coordinates.get('z') - 1 or i.get('z') == input_coordinates.get('z') \
                         or i.get('z') == input_coordinates.get('z') + 1:
                        # all w: w == w + 1 or w == w or w == w -1
                        if i.get('w') == input_coordinates.get('w') - 1 or i.get('w') == input_coordinates.get('w') \
                                or i.get('w') == input_coordinates.get('w') + 1:
                            # i coordinate is active
                            if i.get('state') == '#':
                                active_neighbors += 1
                                # print("i: ", i)
                                count_total_neighbors += 1

                # all y: y == y-1 or y == y or y == y +1
                elif i.get('y') == input_coordinates.get('y') - 1 or i.get('y') == input_coordinates.get('y') \
                            or i.get('y') == input_coordinates.get('y') + 1:
                    # all z: z == z-1 or z == z or z == z +1
                    if i.get('z') == input_coordinates.get('z') - 1 or i.get('z') == input_coordinates.get('z') \
                         or i.get('z') == input_coordinates.get('z') + 1:
                        # all w: w == w + 1 or w == w or w == w -1
                        if i.get('w') == input_coordinates.get('w') - 1 or i.get('w') == input_coordinates.get('w') \
                                or i.get('w') == input_coordinates.get('w') + 1:
                            # i coordinate is active
                            if i.get('state') == '#':
                                active_neighbors += 1
                                # print("i: ", i)
                                count_total_neighbors += 1
            # all x: x == x-1 or x == x +1
            elif i.get('x') == input_coordinates.get('x') - 1 or i.get('x') == input_coordinates.get('x') + 1:
                # all y: y == y-1 or y == y or y == y +1
                if i.get('y') == input_coordinates.get('y') - 1 or i.get('y') == input_coordinates.get('y') \
                            or i.get('y') == input_coordinates.get('y') + 1:
                    # all z: z == z-1 or z == z or z == z +1
                    if i.get('z') == input_coordinates.get('z') - 1 or i.get('z') == input_coordinates.get('z') \
                         or i.get('z') == input_coordinates.get('z') + 1:
                        # all w: w == w + 1 or w == w or w == w -1
                        if i.get('w') == input_coordinates.get('w') - 1 or i.get('w') == input_coordinates.get('w') \
                                or i.get('w') == input_coordinates.get('w') + 1:
                            # i coordinate is active
                            if i.get('state') == '#':
                                active_neighbors += 1
                                # print("i: ", i)
                                count_total_neighbors += 1

    #print("active_neighbors: ", active_neighbors)
    #print("count_total_neighbors: ", count_total_neighbors)

    # find input_coordinates in output and update state in output
    for o in output:
        if input_coordinates['x'] == o['x'] and input_coordinates['y'] == o['y'] and \
                input_coordinates['z'] == o['z'] and input_coordinates['w'] == o['w']:
        #if input_coordinates['x'] == o['x'] + 1 and input_coordinates['y'] == o['y'] and input_coordinates['z'] == o['z']:
            #print("output_coordinates: ", o)
            # active + exactly 2 or 3 neighbors are active = remain active => otherwise inactive
            if input_coordinates.get('state') == '#' and (active_neighbors == 2 or active_neighbors == 3):
                o['state'] = '#'
                #print("..remains active")
            elif input_coordinates.get('state') == '#' and active_neighbors != 2 and active_neighbors != 3:
                o['state'] = '.'
                #print("..becomes inactive")
            # inactive + exactly 3 neighbors are active = become active => otherwise inactive
            elif input_coordinates.get('state') == '.' and active_neighbors == 3:
                o['state'] = '#'
                #print("..becomes active")
            #print("output_coordinates: ", o)
            break
    #print("All active in output: ")
    #print("\n".join(str(o) for o in output if o.get('state') == '#'))


# Slow solution but works, requires refactoring
if __name__ == '__main__':

    files = ['20201217-example.txt', '20201217-input.txt']

    for file_name in files:
        print("\n****************************\n" + file_name)
        with open(file_name) as f:
            lines = f.readlines()

        #print(lines)

        # 1. Create initial x, y, z -3D array for before any cycles
        cycles = 6
        # Based on cycles the end of array
        min_z = 0 - cycles
        max_z = 0 + cycles + 1
        min_w = 0 - cycles
        max_w = 0 + cycles + 1
        min_x = 0 - cycles
        max_x = len(lines) + cycles
        min_y = 0 - cycles
        max_y = len(lines[0].strip()) + cycles

        coordinates = []

        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                for z in range(min_z, max_z):
                    for w in range(min_w, max_w):
                        if -1 < x < len(lines) and -1 < y < len(lines[0].strip()) and z == 0 and w == 0:
                            state = lines[x].strip()[y]
                        else:
                            state = '.'
                        coordinates_dict = {'x': x, 'y': y, 'z': z, 'w': w, 'state': state}
                        coordinates.append(coordinates_dict)

        #print("coordinates:")
        #pprint.pprint(coordinates)

        #print("len(coordinates): ", len(coordinates))

        # 2. Create initial copy for input and output so that all cubes can be processed simultaneously
        input = copy.deepcopy(coordinates)
        output = copy.deepcopy(coordinates)
        for o in output:
            if o.get('state') == '#':
                o['state'] = '.'

        print("All active in input: ")
        print("\n".join(sorted(str(i) for i in input if i.get('state') == '#')))

        # 3. Prepare expected result lists for example part 1
        expected_cycle_1 = [{'x': 0, 'y': 0, 'z': -1, 'state': '#'}, {'x': 1, 'y': 2, 'z': -1, 'state': '#'},
                            {'x': 2, 'y': 1, 'z': -1, 'state': '#'}, {'x': 0, 'y': 0, 'z': 0, 'state': '#'},
                            {'x': 0, 'y': 2, 'z': 0, 'state': '#'}, {'x': 1, 'y': 1, 'z': 0, 'state': '#'},
                            {'x': 1, 'y': 2, 'z': 0, 'state': '#'}, {'x': 2, 'y': 1, 'z': 0, 'state': '#'},
                            {'x': 0, 'y': 0, 'z': 1, 'state': '#'}, {'x': 1, 'y': 2, 'z': 1, 'state': '#'},
                            {'x': 2, 'y': 1, 'z': 1, 'state': '#'}]

        expected_cycle_2 = [{'x': 1, 'y': 1, 'z': -2, 'state': '#'}, {'x': -1, 'y': 1, 'z': -1, 'state': '#'},
                            {'x': 0, 'y': 0, 'z': -1, 'state': '#'}, {'x': 0, 'y': 3, 'z': -1, 'state': '#'},
                            {'x': 1, 'y': 3, 'z': -1, 'state': '#'}, {'x': 2, 'y': 0, 'z': -1, 'state': '#'},
                            {'x': -1, 'y': -1, 'z': 0, 'state': '#'}, {'x': -1, 'y': 0, 'z': 0, 'state': '#'},
                            {'x': 0, 'y': 0, 'z': 0, 'state': '#'}, {'x': 0, 'y': -1, 'z': 0, 'state': '#'},
                            {'x': 1, 'y': -1, 'z': 0, 'state': '#'}, {'x': 2, 'y': 3, 'z': 0, 'state': '#'},
                            {'x': 3, 'y': 0, 'z': 0, 'state': '#'}, {'x': 3, 'y': 1, 'z': 0, 'state': '#'},
                            {'x': 3, 'y': 2, 'z': 0, 'state': '#'}, {'x': -1, 'y': 1, 'z': 1, 'state': '#'},
                            {'x': 0, 'y': 0, 'z': 1, 'state': '#'}, {'x': 0, 'y': 3, 'z': 1, 'state': '#'},
                            {'x': 1, 'y': 3, 'z': 1, 'state': '#'}, {'x': 2, 'y': 0, 'z': 1, 'state': '#'},
                            {'x': 1, 'y': 1, 'z': 2, 'state': '#'}]

        expected_cycle_list = [expected_cycle_1, expected_cycle_2]

        # 4. Process cycles
        cycle = 0
        #min_z = 0
        #max_z = 0

        #print("Input for z = {}: ".format(0))
        #print("\n".join(str(i) for i in input if i.get('z') == 0))

        while cycle < cycles:
            print("{}. cycle".format(cycle + 1))
            for i in input:
                determine_neighbors(i)

            #min_z -= 1
            #max_z += 1

            #for zi in range(min_z, max_z+1):
            #    print("Output for z = {}: ".format(zi))
            #    print("\n".join(str(o) for o in output if o.get('z') == zi))

            # 4. Conduct test for each cycle
            #if cycle < 2 and file_name == "20201217-example.txt":
            #    check_expected(expected_cycle_list[cycle])

            input = copy.deepcopy(output)
            cycle += 1

        # 5. Count of all active
        count_active = len([o for o in output if o.get('state') == '#'])
        #count_z0_active = len([o for o in output if o.get('state') == '#' and o.get('z') == 0])
        print("Count of active: ", count_active)
        #print("Count of only z = 0 active: ", count_z0_active)
        #print("Final count: ", (count_active - count_z0_active)*2 + count_z0_active)
