# --- Day 1: Report Repair ---
# After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.
#
# The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.
#
# To save your vacation, you need to get all fifty stars by December 25th.
#
# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
#
# Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.
#
# Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.
#
# For example, suppose your expense report contained the following:
#
# 1721
# 979
# 366
# 299
# 675
# 1456
# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.
#
# Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
#
# Your puzzle answer was 876459.
#
# --- Part Two ---
# The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.
#
# Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.
#
# In your expense report, what is the product of the three entries that sum to 2020?
#
# Your puzzle answer was 116168640.
#
# Both parts of this puzzle are complete! They provide two gold stars: **


def numbers_that_sum_up_to_2020(lines, is_part_2 = False):

    len_rows = len(lines)
    row_count1 = 0

    while row_count1 < len_rows:
        #print("lines1[row_count]: ", lines1[row_count1])
        number_one = int(lines[row_count1].strip())
        #print("number_one: ", number_one)
        row_count2 = 0
        while row_count2 < len_rows:
            #print("lines2[row_count]: ", lines2[row_count2])
            #print("number_one: ", number_one)
            number_two = int(lines[row_count2].strip())
            #print("number_two: ", number_two)
            sum = number_one + number_two
            #print("sum: ", sum)
            if not is_part_2 and sum == 2020:
                product = number_one * number_two
                print("Part 1: {} * {} = {}".format(number_one, number_two, product))
                return

            elif is_part_2:
                row_count3 = 0
                while row_count3 < len_rows:
                    #print("lines3[row_count]: ", lines3[row_count3])
                    number_three = int(lines[row_count3].strip())
                    #print("number_one: ", number_one)
                    #print("number_two: ", number_two)
                    #print("number_three: ", number_three)
                    sum = number_one + number_two + number_three
                    if sum == 2020:
                        product = number_one * number_two * number_three
                        print("Part 2: {} * {} * {} = {}".format(number_one, number_two, number_three, product))
                        return
                    row_count3 += 1
            row_count2 += 1
        row_count1 += 1


if __name__ == '__main__':

    files = ['20201201-example.txt', '20201201-input.txt']

    for file_name in files:
        print("\n" + file_name)
        with open(file_name) as f:
            lines = f.readlines()

        numbers_that_sum_up_to_2020(lines)
        numbers_that_sum_up_to_2020(lines, True)
