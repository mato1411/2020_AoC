# --- Day 24: Lobby Layout ---
# Your raft makes it to the tropical island; it turns out that the small crab was an excellent navigator. You make your way to the resort.
#
# As you enter the lobby, you discover a small problem: the floor is being renovated. You can't even reach the check-in desk until they've finished installing the new tile floor.
#
# The tiles are all hexagonal; they need to be arranged in a hex grid with a very specific color pattern. Not in the mood to wait, you offer to help figure out the pattern.
#
# The tiles are all white on one side and black on the other. They start with the white side facing up. The lobby is large enough to fit whatever pattern might need to appear there.
#
# A member of the renovation crew gives you a list of the tiles that need to be flipped over (your puzzle input). Each line in the list identifies a single tile that needs to be flipped by giving a series of steps starting from a reference tile in the very center of the room. (Every line starts from the same reference tile.)
#
# Because the tiles are hexagonal, every tile has six neighbors: east, southeast, southwest, west, northwest, and northeast. These directions are given in your list, respectively, as e, se, sw, w, nw, and ne. A tile is identified by a series of these directions with no delimiters; for example, esenee identifies the tile you land on if you start at the reference tile and then move one tile east, one tile southeast, one tile northeast, and one tile east.
#
# Each time a tile is identified, it flips from white to black or from black to white. Tiles might be flipped more than once. For example, a line like esew flips a tile immediately adjacent to the reference tile, and a line like nwwswee flips the reference tile itself.
#
# Here is a larger example:
#
# sesenwnenenewseeswwswswwnenewsewsw
# neeenesenwnwwswnenewnwwsewnenwseswesw
# seswneswswsenwwnwse
# nwnwneseeswswnenewneswwnewseswneseene
# swweswneswnenwsewnwneneseenw
# eesenwseswswnenwswnwnwsewwnwsene
# sewnenenenesenwsewnenwwwse
# wenwwweseeeweswwwnwwe
# wsweesenenewnwwnwsenewsenwwsesesenwne
# neeswseenwwswnwswswnw
# nenwswwsewswnenenewsenwsenwnesesenew
# enewnwewneswsewnwswenweswnenwsenwsw
# sweneswneswneneenwnewenewwneswswnese
# swwesenesewenwneswnwwneseswwne
# enesenwswwswneneswsenwnewswseenwsese
# wnwnesenesenenwwnenwsewesewsesesew
# nenewswnwewswnenesenwnesewesw
# eneswnwswnwsenenwnwnwwseeswneewsenese
# neswnwewnwnwseenwseesewsenwsweewe
# wseweeenwnesenwwwswnew
# In the above example, 10 tiles are flipped once (to black), and 5 more are flipped twice (to black, then back to white). After all of these instructions have been followed, a total of 10 tiles are black.
#
# Go through the renovation crew's list and determine which tiles they need to flip. After all of the instructions have been followed, how many tiles are left with the black side up?
#
# Your puzzle answer was 320.
#
# --- Part Two ---
# The tile floor in the lobby is meant to be a living art exhibit. Every day, the tiles are all flipped according to the following rules:
#
# Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
# Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
# Here, tiles immediately adjacent means the six tiles directly touching the tile in question.
#
# The rules are applied simultaneously to every tile; put another way, it is first determined which tiles need to be flipped, then they are all flipped at the same time.
#
# In the above example, the number of black tiles that are facing up after the given number of days has passed is as follows:
#
# Day 1: 15
# Day 2: 12
# Day 3: 25
# Day 4: 14
# Day 5: 23
# Day 6: 28
# Day 7: 41
# Day 8: 37
# Day 9: 49
# Day 10: 37
#
# Day 20: 132
# Day 30: 259
# Day 40: 406
# Day 50: 566
# Day 60: 788
# Day 70: 1106
# Day 80: 1373
# Day 90: 1844
# Day 100: 2208
# After executing this process a total of 100 times, there would be 2208 black tiles facing up.
#
# How many tiles will be black after 100 days?
#
# Your puzzle answer was 3777.
#
# Both parts of this puzzle are complete! They provide two gold stars: **


import operator
from pprint import pprint


def get_neighbors(pos):
    n = []
    for i in range(len(hexagon_directions_labeling)):
        neighbor_pos = tuple(map(operator.add, pos, hexagon_directions_tuples[i]))
        n.append(neighbor_pos)
    return n


if __name__ == '__main__':

    files = ['20201224-example.txt', '20201224-input.txt']

    for file_name in files:
        print("\n****************************\n" + file_name)
        with open(file_name) as f:
            lines = f.readlines()

        tile_directions = []

        hexagon_directions_labeling = ['e', 'se', 'sw', 'w', 'nw', 'ne']
        hexagon_directions_tuples = [(0,-1),(-1,0),(-1,1),(0,1),(1,0),(1,-1)]

        for i in range(len(lines)):
            tile_moves = []
            line = lines[i].strip()
            for l in range(len(line)):
                previous_l = ''
                if l > 0:
                    previous_l = line[l-1]
                current_l = line[l]
                if previous_l != 'n' and previous_l != 's':
                    if current_l == 'e' or current_l == 'w':
                        tile_moves.append(current_l)
                    else:
                        tile_moves.append(current_l + line[l+1])

            tile_directions.append({'moves': tile_moves})

        #print("tile_directions:")
        #pprint(tile_directions)

        print("\nPart One")

        tile_colors = []

        for t in tile_directions:
            current_pos = (0, 0)
            for m in t.get('moves'):

                for i in range(len(hexagon_directions_labeling)):
                    if m == hexagon_directions_labeling[i]:
                        # Calculation with coordinates of tuple
                        current_pos = tuple(map(operator.add, current_pos, hexagon_directions_tuples[i]))

            match_existing_pos = [i for i, tc in enumerate(tile_colors) if tc.get('pos') == current_pos]
            if len(match_existing_pos) > 0:
                i = match_existing_pos[0]
                tile_colors[i]['white'] = not tile_colors[i].get('white')
                tile_colors[i]['flips'] = tile_colors[i].get('flips', 0) +1
            else:
                tile_colors.append({'pos': current_pos, 'white': False, 'flips': 1})

        #print("tile_colors:")
        #pprint(tile_colors)
        black_tiles = set(tc.get('pos') for tc in tile_colors if tc.get('white') == False)
        print("black tiles: ", len(black_tiles))

        print("\nPart Two")

        days = 100

        for d in range(days):

            turn_white_list = []
            white_with_black_neighbor = {}

            for bt in black_tiles:
                neighbors = get_neighbors(bt)
                black_neighbors = [n for n in neighbors for b in black_tiles if n == b]
                black_neighbors_count = len(black_neighbors)
                # Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
                if black_neighbors_count == 0 or black_neighbors_count > 2:
                    turn_white_list.append(bt)
                # Add white neighbors to separate dict
                for n in neighbors:
                    if n in black_neighbors:
                        continue
                    # Add count of black neighbors
                    white_with_black_neighbor[n] = white_with_black_neighbor.get(n, 0) + 1

            # Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
            for k, v in white_with_black_neighbor.items():
                if v == 2 and k not in black_tiles:
                    black_tiles.add(k)

            for tw in turn_white_list:
                black_tiles.remove(tw)

            print("Day {}: {} black tiles". format(d + 1, len(black_tiles)))
