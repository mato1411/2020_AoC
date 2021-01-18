# --- Day 20: Jurassic Jigsaw ---
# The high-speed train leaves the forest and quickly carries you south. You can even see a desert in the distance! Since you have some spare time, you might as well see if there was anything interesting in the image the Mythical Information Bureau satellite captured.
#
# After decoding the satellite messages, you discover that the data actually contains many small images created by the satellite's camera array. The camera array consists of many cameras; rather than produce a single square image, they produce many smaller square image tiles that need to be reassembled back into a single image.
#
# Each camera in the camera array returns a single monochrome image tile with a random unique ID number. The tiles (your puzzle input) arrived in a random order.
#
# Worse yet, the camera array appears to be malfunctioning: each image tile has been rotated and flipped to a random orientation. Your first task is to reassemble the original image by orienting the tiles so they fit together.
#
# To show how the tiles should be reassembled, each tile's image data includes a border that should line up exactly with its adjacent tiles. All tiles have this border, and the border lines up exactly when the tiles are both oriented correctly. Tiles at the edge of the image also have this border, but the outermost edges won't line up with any other tiles.
#
# For example, suppose you have the following nine tiles:
#
# Tile 2311:
# ..##.#..#.
# ##..#.....
# #...##..#.
# ####.#...#
# ##.##.###.
# ##...#.###
# .#.#.#..##
# ..#....#..
# ###...#.#.
# ..###..###
#
# Tile 1951:
# #.##...##.
# #.####...#
# .....#..##
# #...######
# .##.#....#
# .###.#####
# ###.##.##.
# .###....#.
# ..#.#..#.#
# #...##.#..
#
# Tile 1171:
# ####...##.
# #..##.#..#
# ##.#..#.#.
# .###.####.
# ..###.####
# .##....##.
# .#...####.
# #.##.####.
# ####..#...
# .....##...
#
# Tile 1427:
# ###.##.#..
# .#..#.##..
# .#.##.#..#
# #.#.#.##.#
# ....#...##
# ...##..##.
# ...#.#####
# .#.####.#.
# ..#..###.#
# ..##.#..#.
#
# Tile 1489:
# ##.#.#....
# ..##...#..
# .##..##...
# ..#...#...
# #####...#.
# #..#.#.#.#
# ...#.#.#..
# ##.#...##.
# ..##.##.##
# ###.##.#..
#
# Tile 2473:
# #....####.
# #..#.##...
# #.##..#...
# ######.#.#
# .#...#.#.#
# .#########
# .###.#..#.
# ########.#
# ##...##.#.
# ..###.#.#.
#
# Tile 2971:
# ..#.#....#
# #...###...
# #.#.###...
# ##.##..#..
# .#####..##
# .#..####.#
# #..#.#..#.
# ..####.###
# ..#.#.###.
# ...#.#.#.#
#
# Tile 2729:
# ...#.#.#.#
# ####.#....
# ..#.#.....
# ....#..#.#
# .##..##.#.
# .#.####...
# ####.#.#..
# ##.####...
# ##..#.##..
# #.##...##.
#
# Tile 3079:
# #.#.#####.
# .#..######
# ..#.......
# ######....
# ####.#..#.
# .#...#.##.
# #.#####.##
# ..#.###...
# ..#.......
# ..#.###...
# By rotating, flipping, and rearranging them, you can find a square arrangement that causes all adjacent borders to line up:
#
# #...##.#.. ..###..### #.#.#####.
# ..#.#..#.# ###...#.#. .#..######
# .###....#. ..#....#.. ..#.......
# ###.##.##. .#.#.#..## ######....
# .###.##### ##...#.### ####.#..#.
# .##.#....# ##.##.###. .#...#.##.
# #...###### ####.#...# #.#####.##
# .....#..## #...##..#. ..#.###...
# #.####...# ##..#..... ..#.......
# #.##...##. ..##.#..#. ..#.###...
#
# #.##...##. ..##.#..#. ..#.###...
# ##..#.##.. ..#..###.# ##.##....#
# ##.####... .#.####.#. ..#.###..#
# ####.#.#.. ...#.##### ###.#..###
# .#.####... ...##..##. .######.##
# .##..##.#. ....#...## #.#.#.#...
# ....#..#.# #.#.#.##.# #.###.###.
# ..#.#..... .#.##.#..# #.###.##..
# ####.#.... .#..#.##.. .######...
# ...#.#.#.# ###.##.#.. .##...####
#
# ...#.#.#.# ###.##.#.. .##...####
# ..#.#.###. ..##.##.## #..#.##..#
# ..####.### ##.#...##. .#.#..#.##
# #..#.#..#. ...#.#.#.. .####.###.
# .#..####.# #..#.#.#.# ####.###..
# .#####..## #####...#. .##....##.
# ##.##..#.. ..#...#... .####...#.
# #.#.###... .##..##... .####.##.#
# #...###... ..##...#.. ...#..####
# ..#.#....# ##.#.#.... ...##.....
# For reference, the IDs of the above tiles are:
#
# 1951    2311    3079
# 2729    1427    2473
# 2971    1489    1171
# To check that you've assembled the image correctly, multiply the IDs of the four corner tiles together. If you do this with the assembled tiles from the example above, you get 1951 * 3079 * 2971 * 1171 = 20899048083289.
#
# Assemble the tiles into an image. What do you get if you multiply together the IDs of the four corner tiles?
#
# Your puzzle answer was 18482479935793.
#
# --- Part Two ---
# Now, you're ready to check the image for sea monsters.
#
# The borders of each tile are not part of the actual image; start by removing them.
#
# In the example above, the tiles become:
#
# .#.#..#. ##...#.# #..#####
# ###....# .#....#. .#......
# ##.##.## #.#.#..# #####...
# ###.#### #...#.## ###.#..#
# ##.#.... #.##.### #...#.##
# ...##### ###.#... .#####.#
# ....#..# ...##..# .#.###..
# .####... #..#.... .#......
#
# #..#.##. .#..###. #.##....
# #.####.. #.####.# .#.###..
# ###.#.#. ..#.#### ##.#..##
# #.####.. ..##..## ######.#
# ##..##.# ...#...# .#.#.#..
# ...#..#. .#.#.##. .###.###
# .#.#.... #.##.#.. .###.##.
# ###.#... #..#.##. ######..
#
# .#.#.### .##.##.# ..#.##..
# .####.## #.#...## #.#..#.#
# ..#.#..# ..#.#.#. ####.###
# #..####. ..#.#.#. ###.###.
# #####..# ####...# ##....##
# #.##..#. .#...#.. ####...#
# .#.###.. ##..##.. ####.##.
# ...###.. .##...#. ..#..###
# Remove the gaps to form the actual image:
#
# .#.#..#.##...#.##..#####
# ###....#.#....#..#......
# ##.##.###.#.#..######...
# ###.#####...#.#####.#..#
# ##.#....#.##.####...#.##
# ...########.#....#####.#
# ....#..#...##..#.#.###..
# .####...#..#.....#......
# #..#.##..#..###.#.##....
# #.####..#.####.#.#.###..
# ###.#.#...#.######.#..##
# #.####....##..########.#
# ##..##.#...#...#.#.#.#..
# ...#..#..#.#.##..###.###
# .#.#....#.##.#...###.##.
# ###.#...#..#.##.######..
# .#.#.###.##.##.#..#.##..
# .####.###.#...###.#..#.#
# ..#.#..#..#.#.#.####.###
# #..####...#.#.#.###.###.
# #####..#####...###....##
# #.##..#..#...#..####...#
# .#.###..##..##..####.##.
# ...###...##...#...#..###
# Now, you're ready to search for sea monsters! Because your image is monochrome, a sea monster will look like this:
#
#                   #
# #    ##    ##    ###
#  #  #  #  #  #  #
# When looking for this pattern in the image, the spaces can be anything; only the # need to match. Also, you might need to rotate or flip your image before it's oriented correctly to find sea monsters. In the above image, after flipping and rotating it to the appropriate orientation, there are two sea monsters (marked with O):
#
# .####...#####..#...###..
# #####..#..#.#.####..#.#.
# .#.#...#.###...#.##.O#..
# #.O.##.OO#.#.OO.##.OOO##
# ..#O.#O#.O##O..O.#O##.##
# ...#.#..##.##...#..#..##
# #.##.#..#.#..#..##.#.#..
# .###.##.....#...###.#...
# #.####.#.#....##.#..#.#.
# ##...#..#....#..#...####
# ..#.##...###..#.#####..#
# ....#.##.#.#####....#...
# ..##.##.###.....#.##..#.
# #...#...###..####....##.
# .#.##...#.##.#.#.###...#
# #.###.#..####...##..#...
# #.###...#.##...#.##O###.
# .O##.#OO.###OO##..OOO##.
# ..O#.O..O..O.#O##O##.###
# #.#..##.########..#..##.
# #.#####..#.#...##..#....
# #....##..#.#########..##
# #...#.....#..##...###.##
# #..###....##.#...##.##.#
# Determine how rough the waters are in the sea monsters' habitat by counting the number of # that are not part of a sea monster. In the above example, the habitat's water roughness is 273.
#
# How many # are not part of a sea monster?
#
# Your puzzle answer was 2118.
#
# Both parts of this puzzle are complete! They provide two gold stars: **


import math
import operator
from pprint import pprint
import numpy as np


def fliplr_np(tile_id, tile_dict):
    t = tile_dict.get(tile_id)
    a = np.array(t.get('pixel'))
    ra = np.fliplr(a)
    t['pixel'] = ra.tolist()
    update_borders(tile_id, tile_dict)


def rot90_left_np(tile_id, tile_dict, rn=1):
    t = tile_dict.get(tile_id)
    a = np.array(t.get('pixel'))
    ra = np.rot90(a, rn)
    t['pixel'] = ra.tolist()
    for i in range(rn):
        update_borders(tile_id, tile_dict)


def update_borders(tile_id, tile_list):
    t = tile_list[tile_id]
    p = t.get('pixel')
    t['n'] = "".join(p[0])
    t['e'] = "".join([x[-1] for x in p])
    t['s'] = "".join(p[-1])
    t['w'] = "".join([x[0] for x in p])


def get_corners(d):

    corners = []

    for k, v in d.items():
        if len(v.get('neighbors', set())) == 2:
            corners.append(k)

    return corners


def print_tile_neighbors(d):
    message = "tile: {}, neighbors: {}, pos {}, common_borders: {}"
    for k, v in d.items():
        print(message.format(k, v.get('neighbors', set()), v.get('pos', tuple()), v.get('common_borders', set())))


def determine_neighbors_part_1():
    global tiles
    # For each tile
    for t_k, t_v in tiles.items():

        # ... check all 4 borders (rotation)
        for t_d in ['n', 'e', 's', 'w']:

            # For each potential neighbor tile
            for n_k, n_v in tiles.items():

                # Only if tile id does not match neighbor tile id proceed, otherwise continue with next tile
                if t_k == n_k:
                    continue

                # 2 time rotation results in reverse order of borders
                for n_r in [False, True]:
                    if n_r:
                        rot90_left_np(n_k, tiles, 2)
                        # Equals following but not all pixel would be rotated:
                        # n_v['n'] = n_v.get('n')[::-1]
                        # n_v['e'] = n_v.get('e')[::-1]
                        # n_v['s'] = n_v.get('s')[::-1]
                        # n_v['w'] = n_v.get('w')[::-1]
                    for n_d in ['n', 'e', 's', 'w']:

                        # Tile border matches neighbor border
                        if t_v[t_d] == n_v[n_d]:

                            #print("MATCH")
                            #print("T: id: {} cardinal: {}".format(t_k, t_d))
                            #print("N: id: {} cardinal: {} reverse: {}".format(n_k, n_d, n_r))

                            t_v.get('neighbors').add(n_k)
                            n_v.get('neighbors').add(t_k)
                            t_v.get('common_borders').add(t_v[t_d])
                            # Reverse order could be a common border and needs to be added
                            t_v.get('common_borders').add(t_v[t_d][::-1])
                            n_v.get('common_borders').add(n_v[n_d])
                            # Reverse order could be a common border and needs to be added
                            n_v.get('common_borders').add(n_v[n_d][::-1])


def build_row(tile, dir, d):
    global tiles_pos_identified
    global tile_count_width_height
    direction_tuples = {'n': (-1, 0), 'e': (0, 1), 'w': (0, -1), 's': (1, 0)} # x, y
    directions = ['n', 'e', 's', 'w']
    dir_opposite = directions[(directions.index(dir) + 2) % 4]
    tile_count = 1
    current_pos = d.get(tile).get('pos')
    while tile_count < tile_count_width_height:
        for n in d.get(tile).get('neighbors').difference(tiles_pos_identified):
            if d.get(tile).get(dir) in d.get(n).get('common_borders'):
                break # Neighbor for direction found
        #print("tile {} n {} dir {} dir_opposite {}".format(tile, n, dir, dir_opposite))
        #print("d.get(tile).get(dir) ", d.get(tile).get(dir))
        #print("d.get(n).get('common_borders') ", d.get(n).get('common_borders'))

        match = False
        for angle in range(8):
            #print("d.get(tile).get(dir): ")
            #print(d.get(tile).get(dir))
            #print("d.get(n).get(dir_opposite): ")
            #print(d.get(n).get(dir_opposite))
            if d.get(tile).get(dir) == d.get(n).get(dir_opposite):
                match = True
                break # Neighbor angle fine
            rot90_left_np(n, d)
            # After 3 rotations, let's flip, because it fails when flipping after 4 rotations
            if angle == 3:
                #print("d.get(n).get(dir_opposite): ")
                #print(d.get(n).get(dir_opposite))
                #print("Now flip")
                fliplr_np(n, d)
                #print("d.get(n).get(dir_opposite): ")
                #print(d.get(n).get(dir_opposite))
        if not match:
            print("Error: Neighbor does not match")
            exit()

        n_pos = tuple(map(operator.add, current_pos, direction_tuples.get(dir)))
        d.get(n)['pos'] = n_pos
        tiles_pos_identified.add(n)
        current_pos = n_pos
        tile = n
        tile_count += 1


def position_tiles_for_picture(d):
    global tiles_pos_identified
    global tile_count_width_height
    # Start with a corner
    c = get_corners(d)[0]
    # Add top left pos and rotate corner so that neighbors are south and east
    d.get(c)['pos'] = (0,0) # x, y
    #print("d.get(c).get('common_borders')")
    #print(d.get(c).get('common_borders'))
    match = False
    for j in range(8):
        se_border = { d.get(c).get('s'), d.get(c).get('e') }
        #print("se_border")
        #print(se_border)
        #print("se_border.difference(d.get(c).get('common_borders'))")
        #print(se_border.difference(d.get(c).get('common_borders')))
        if not se_border.difference(d.get(c).get('common_borders')):
        #if se_border.issubset(d.get(c).get('common_borders')):
            #print(d.get(c).get('s'))
            match = True
            break
        rot90_left_np(c, d)
        if j == 3:
            fliplr_np(c, d)
    if not match:
        print("Error: Top left does not match")
        exit()

    # Track tiles position identified
    tiles_pos_identified.add(c)

    # Build top row
    build_row(c, 'e', d)

    # Build next rows
    for x in range(0, tile_count_width_height -1):
        # get south neighbor
        second_tile_per_row_set = {k for k, v in d.items() if v.get('pos', (-1, -1)) == (x, 1)}
        #print("list(d.get(c).get('neighbors').difference(second_tile_per_row_set))")
        #print(d.get(c).get('neighbors').difference(second_tile_per_row_set))
        south_neighbor_tiles = d.get(c).get('neighbors').difference(second_tile_per_row_set).difference(tiles_pos_identified)
        #south_neighbor_tile = int(list(d.get(c).get('neighbors').difference(second_tile_per_row_set))[0])
        for south_neighbor_tile in south_neighbor_tiles:
            #print('pos: ', (x + 1, 0))
            d.get(south_neighbor_tile)['pos'] = (x + 1, 0)
            # rotate south neighbor tile to fit on common border before calculating the row
            match = False
            for i in range(8):
                #print("south_neighbor_tile: ", south_neighbor_tile)
                #print("d.get(c).get('s')")
                #print(d.get(c).get('s'))
                #print("d.get(south_neighbor_tile).get('n')")
                #print(d.get(south_neighbor_tile).get('n'))
                if d.get(c).get('s') == d.get(south_neighbor_tile).get('n'):
                    match = True
                    break
                rot90_left_np(south_neighbor_tile, d)
                if i == 3:
                    fliplr_np(south_neighbor_tile, d)
            if match:
                break
        if not match:
            print("Error: South neighbor does not match")
            exit()

        tiles_pos_identified.add(south_neighbor_tile)
        # Build row starting from south neighbor
        build_row(south_neighbor_tile, 'e', d)
        c = south_neighbor_tile

    print_tile_neighbors(d)


# Make pictures
# Trim off edges of all individual tiles
# Flatten into a single "tile"
def create_image_str(d, without_borders):
    global tile_count_width_height

    tile_pixel_width_height = len([v.get('pixel') for v in d.values() if v.get('pos') == (0, 0)][0])

    pic_string = ""

    if without_borders:
        offset = 1
    else:
        offset = 0

    for x in range(tile_count_width_height):

        for p_x in range(offset, tile_pixel_width_height - offset):

            for y in range(tile_count_width_height):

                for k, v in tiles.items():
                    if v.get('pos') == (x, y):
                        tile_pixel = v.get('pixel')
                        #print(k)
                        break
                #print("tile_pixel")
                #pprint(tile_pixel)

                for p_y in range(offset, tile_pixel_width_height - offset):
                    pic_string += tile_pixel[p_x][p_y]

                if not without_borders:
                    pic_string += ' '

            pic_string += '\n'

        if not without_borders:
            pic_string += '\n'

    return pic_string


def print_pic(array):
    pic_string = ""
    for x in range(len(array)):
        for y in range(len(array)):
            pic_string += array[x][y]
        pic_string += '\n'
    pprint(pic_string)


def search_sea_monster(sea_monster, pic):
    monster_hash_line_counts = []
    monster_hash_index = []
    line_count = 0
    match_count = 0
    for line in sea_monster.splitlines():
        monster_hash_index.append(list())
        for idx in range(len(line)):
            if line[idx] =='#':
                monster_hash_index[line_count].append(idx)
        monster_hash_line_counts.append(line.count("#"))
        line_count += 1

    #print(monster_hash_line_counts)
    #print(monster_hash_index)
    highest_monster_hash_index = max(max(val) for val in monster_hash_index)
    #print("highest_monster_hash_index: ", highest_monster_hash_index)
    #print("len(pic): ", len(pic))
    #print(sum(monster_hash_line_counts))
    sea_monster_count = 0
    for x in range(len(pic) -2):
        for y in range(len(pic) - highest_monster_hash_index):
            #print("x: {}, y: {}".format(x, y))
            #print("pic[x]:   ", pic[x])
            #print("pic[x+1]: ", pic[x+1])
            #print("pic[x+2]: ", pic[x+2])
            match_count = 0
            for mhi_line in range(len(monster_hash_index)):
                match_line_count = 0
                for mhi in range(len(monster_hash_index[mhi_line])):
                    #print("x: {}, mhi_line: {}, y: {}, mhi: {}".format(x,y,mhi_line,mhi))
                    #print("pic[x + mhi_line][y + mhi]: ", pic[x + mhi_line][y + mhi])
                    if pic[x + mhi_line][y + monster_hash_index[mhi_line][mhi]] == "#":
                        match_line_count += 1
                    #print("match_count: ", match_count)
                    #print("match_line_count: ", match_line_count)
                    #print("monster_hash_line_counts[mhi_line]: ", monster_hash_line_counts[mhi_line])
                    if monster_hash_line_counts[mhi_line] == match_line_count:
                        break
                match_count += match_line_count
            #print("match_count: ", match_count)
            if sum(monster_hash_line_counts) == match_count:
                sea_monster_count += 1

    return sea_monster_count


def read_tiles(file):

    tiles_dict = {}

    with open(file) as f:
        lines = f.readlines()

    # Read tiles
    for i in range(len(lines)):

        line = lines[i].strip()

        # New tile
        if line.startswith("Tile"):
            pixel = []
            id = int(line.split()[1].split(":")[0].strip())
            continue

        # Tile done
        if line.strip() == "":
            # North
            n = "".join(pixel[0])
            # East
            e = "".join([x[-1] for x in pixel])
            # South
            s = "".join(pixel[-1])
            # West
            w = "".join([x[0] for x in pixel])
            # [ id : { pixel, n, e, s, w, neighbors, common_borders } ]
            tiles_dict[id] = { 'pixel': pixel, 'n': n, 'e': e, 's': s, 'w': w, 'neighbors': set(), 'common_borders': set() }
            continue

        # Get all pixel
        y_values = []
        for y in range(len(line)):
            y_values.append(line[y])
        pixel.append(y_values)

    return tiles_dict


if __name__ == '__main__':

    files = ['20201220-example.txt', '20201220-input.txt']

    for f in files:
        print("\n****************************\n" + f)
        tiles = read_tiles(f)
        #print("Tiles:")
        #pprint(tiles)

        print("\nPart One")

        # Get neighbors for each tile
        determine_neighbors_part_1()
        print_tile_neighbors(tiles)
        corners = get_corners(tiles)
        print("Corners: ", corners)
        p = 1
        for c in corners:
            p *= c

        print("Product: ", p)

        if f.find("example") > 0:
            assert p == 20899048083289
        else:
            assert p == 18482479935793

        print("\nPart Two")

        # Build the whole picture
        tile_count_width_height = int(math.sqrt(len(tiles)))
        tiles_pos_identified = set()
        position_tiles_for_picture(tiles)

        # Create image
        pic_string = create_image_str(tiles, False)
        print("Image inclusive borders: ")
        pprint(pic_string)
        pic_string = create_image_str(tiles, True)
        print("Image without borders: ")
        pprint(pic_string)

        image_array = [list(line) for line in pic_string.splitlines()]

        # Define sea monster pattern
        # Count number of # in sea monster pattern
        sea_monster_str = "                  # \n#    ##    ##    ###\n #  #  #  #  #  #   "
        sea_monster_hash_count = sea_monster_str.count('#')
        print("sea_monster_str: ", sea_monster_str)
        print("sea_monster_hash_count: ", sea_monster_hash_count)
        # Rotate the tile in all 8 forms until find any sea monsters are found, then use that count
        image_array = [list(line) for line in pic_string.splitlines()]
        print("image_array:")
        print_pic(image_array)
        for i in range(8):
            # Search sea monster
            monster_count = search_sea_monster(sea_monster_str, image_array)
            if monster_count > 0:
                print("Image in proper position:")
                print_pic(image_array)
                print("monster_count: ", monster_count)
                break
            # Rotate and flip image
            a = np.array(image_array)
            ra = np.rot90(a)
            if i == 3:
                ra = np.fliplr(ra)
            image_array = ra.tolist()
            #print("Image rotated:")
            #print_pic(image_array)

        print("pic_string.count('#'): ", pic_string.count('#'))
        water_roughness = pic_string.count('#') - sea_monster_hash_count * monster_count
        print("water roughness: ", water_roughness)

        if f.find("example") > 0:
            assert water_roughness == 273
        else:
            assert water_roughness == 2118
