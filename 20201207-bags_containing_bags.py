# --- Day 7: Handy Haversacks ---
# You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to issues in luggage processing.
#
# Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!
#
# For example, consider the following rules:
#
# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.
# These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.
#
# You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)
#
# In the above rules, the following options would be available to you:
#
# A bright white bag, which can hold your shiny gold bag directly.
# A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
# A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
# A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
# So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.
#
# How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)
#
# Your puzzle answer was 248.
#
# --- Part Two ---
# It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!
#
# Consider again your shiny gold bag and the rules from the above example:
#
# faded blue bags contain 0 other bags.
# dotted black bags contain 0 other bags.
# vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
# dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.
# So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!
#
# Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!
#
# Here's another example:
#
# shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags.
# In this example, a single shiny gold bag must contain 126 other bags.
#
# How many individual bags are required inside your single shiny gold bag?
#
# Your puzzle answer was 57281.
#
# Both parts of this puzzle are complete! They provide two gold stars: **


import re


def get_bag_count_part1(bag_name, search_dict):

    #print('search_bag: ', search_bag)
    #print('search_dict: ', search_dict)

    global matched_bags

    for out_bag, in_bags in search_dict.items():
        #print('out_bag: ', out_bag)
        for in_bag, in_bag_count in in_bags.items():
            if bag_name == in_bag:
                #print("match in_bag!!!")
                matched_bags.add(out_bag)
                #print('matched_bags: ', matched_bags)
                get_bag_count_part1(out_bag, search_dict)

    return len(matched_bags)


def get_bag_count_part2_final(bag_name, search_dict):
    global count
    #print('search_dict[bag_name].values(): ', search_dict[bag_name].values())
    count += sum(search_dict[bag_name].values())
    #print('count: ', count)
    for in_bag, in_bag_count in search_dict[bag_name].items():
        #print('in_bag: ', in_bag)
        #print('in_bag_count: ', in_bag_count)
        for i in range(in_bag_count):
            #print('i: ', i)
            get_bag_count_part2_final(in_bag, search_dict)

    return count


if __name__ == '__main__':

    files = ['20201207-example.txt', '20201207-input.txt']

    for file_name in files:
        print("\n" + file_name)
        with open(file_name) as f:
            bag_rules = f.readlines()

        len_rows = len(bag_rules)

        row_count = 0
        outer_bags = {}
        while row_count < len_rows:
            #print("bag_rules[row_count]: ", bag_rules[row_count].strip())
            row_content = bag_rules[row_count].strip()
            #print("row_content: ", row_content)
            # Dictionary structure
            # { '<bag0>': {<bag1>:<count1>, ..., <bagn>:<countn>},  ... ,'<bagm>': {<bag1>:<count1>, ..., <bagn>:<countn>},
            outer_bag = row_content[:row_content.find('bag')].strip()
            #print('outer_bag: ', outer_bag)
            #print('len(outer_bag): ', len(outer_bag))
            inner_bags = {}
            for inner_bag in row_content[row_content.find('contain') + len('contain'):].split(','):
                inner_bag = inner_bag.strip().replace(".", "")
                #print('inner_bag: ', inner_bag)
                regex_inner_bag = '(^[0-9]|^[0-9]+)(.*)(bag.*$)'
                regex_result = re.search(regex_inner_bag, inner_bag)
                #print('regex_result: ', regex_result)
                if regex_result:
                    inner_bag_count = int(regex_result.group(1).strip())
                    inner_bag_name = regex_result.group(2).strip()
                    #print('inner_bag_count :', inner_bag_count)
                    #print('inner_bag_name :', inner_bag_name)
                    inner_bags[inner_bag_name] = inner_bag_count
            outer_bags[outer_bag] = inner_bags
            #print("row_count: ", row_count)
            row_count += 1

        search_bag = 'shiny gold'
        matched_bags = set()
        print("Part 1: ", get_bag_count_part1(search_bag, outer_bags))
        count = 0
        print("Part 2: ", get_bag_count_part2_final(search_bag, outer_bags))
