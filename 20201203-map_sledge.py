# --- Day 3: Toboggan Trajectory ---
# With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy, it's certainly not safe: there's very minimal steering and the area is covered in trees. You'll need to see which angles will take you near the fewest trees.
#
# Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your puzzle input) of the open squares (.) and trees (#) you can see. For example:
#
# ..##.......
# #...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
# #.##...#...
# #...##....#
# .#..#...#.#
# These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times:
#
# ..##.........##.........##.........##.........##.........##.......  --->
# #...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
# .#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
# ..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
# .#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
# ..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
# .#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
# .#........#.#........#.#........#.#........#.#........#.#........#
# #.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
# #...##....##...##....##...##....##...##....##...##....##...##....#
# .#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
# You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).
#
# The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:
#
# From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.
#
# The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:
#
# ..##.........##.........##.........##.........##.........##.......  --->
# #..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
# .#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
# ..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
# .#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
# ..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
# .#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
# .#........#.#........X.#........#.#........#.#........#.#........#
# #.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
# #...##....##...##....##...#X....##...##....##...##....##...##....#
# .#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
# In this example, traversing the map using this slope would cause you to encounter 7 trees.
#
# Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
#
# Your puzzle answer was 156.
#
# --- Part Two ---
# Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.
#
# Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:
#
# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
# In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.
#
# What do you get if you multiply together the number of trees encountered on each of the listed slopes?
#
# Your puzzle answer was 3521829480.
#
# Both parts of this puzzle are complete! They provide two gold stars: **


def get_tree_hit_count(right, down):

    tree_hit_count = 0
    col_selected = 0
    row_counter = 0

    for row in coordinates:

        skip = False

        if down == 2 and row_counter % down != 0:
            skip = True

        if not skip:

            # print("row_counter: ", row_counter)
            # print("col_selected: ", col_selected)
            # print("row[col_selected]: ", row[col_selected])
            if row[col_selected] == '#':
                #print("Tree hit!")
                row[col_selected] = 'X'
                tree_hit_count += 1
            #if row[col_selected] == '.':
            # print("No tree hit")
            # row[col_selected] = 'O'
            col_selected += right

        row_counter += 1

    #print("tree_hit_count: ", tree_hit_count)
    return tree_hit_count


if __name__ == '__main__':

    files = ['20201203-example.txt', '20201203-input.txt']

    for file_name in files:
        print("\n" + file_name)
        with open(file_name) as f:
            lines = f.readlines()

        row_count = 0

        len_rows = len(lines)
        #print("len_rows: ", len_rows)
        len_cols = len(lines[row_count].strip())
        #print("len_cols: ", len_cols)

        # For part two 7 as maximum right is required
        multiply_col = len_rows / len_cols * 7
        #print("multiply_col: ", multiply_col)

        multiply_col_int = int(multiply_col) + 1
        #print("multiply_col_int: ", multiply_col_int)

        rows, cols = (len_rows, len_cols * multiply_col_int)
        coordinates = [[0 for i in range(cols)] for j in range(rows)]

        while row_count < len_rows:
            #print("row_count: ", row_count)
            new_row = lines[row_count].strip() * multiply_col_int
            #print(new_row)
            #print(len(new_row))

            col_count = 0

            while col_count < len_cols * multiply_col_int:
                #print("col_count: ", col_count)
                #print("new_row[col_count]: ", new_row[col_count])
                coordinates[row_count][col_count] = new_row[col_count]
                #print("coordinates[row_count][col_count]: ", coordinates[row_count][col_count])
                col_count += 1

            row_count += 1

        tree_hit_count_part_one = get_tree_hit_count(3, 1)
        print("tree_hit_count_part_one: ", tree_hit_count_part_one)

        tree_hit_counts_part_two = [get_tree_hit_count(1, 1), tree_hit_count_part_one, get_tree_hit_count(5, 1),
                                    get_tree_hit_count(7, 1), get_tree_hit_count(1, 2)]

        product = 1
        for i in tree_hit_counts_part_two:
            product *= i

        print("tree_hit_counts_part_two: ", tree_hit_counts_part_two)
        print("product: ", product)
