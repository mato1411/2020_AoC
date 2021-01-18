# --- Day 6: Custom Customs ---
# As your flight approaches the regional airport where you'll switch to a much larger plane, customs declaration forms are distributed to the passengers.
#
# The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify the questions for which anyone in your group answers "yes". Since your group is just you, this doesn't take very long.
#
# However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. For each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:
#
# abcx
# abcy
# abcz
# In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers to the same question don't count extra; each question counts at most once.)
#
# Another group asks for your help, then another, and eventually you've collected answers from every group on the plane (your puzzle input). Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:
#
# abc
#
# a
# b
# c
#
# ab
# ac
#
# a
# a
# a
# a
#
# b
# This list represents answers from five groups:
#
# The first group contains one person who answered "yes" to 3 questions: a, b, and c.
# The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
# The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
# The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
# The last group contains one person who answered "yes" to only 1 question, b.
# In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.
#
# For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?
#
# Your puzzle answer was 6947.
#
# --- Part Two ---
# As you finish the last group's customs declaration, you notice that you misread one word in the instructions:
#
# You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!
#
# Using the same example as above:
#
# abc
#
# a
# b
# c
#
# ab
# ac
#
# a
# a
# a
# a
#
# b
# This list represents answers from five groups:
#
# In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
# In the second group, there is no question to which everyone answered "yes".
# In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
# In the fourth group, everyone answered yes to only 1 question, a.
# In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
# In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.
#
# For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?
#
# Your puzzle answer was 3398.
#
# Both parts of this puzzle are complete! They provide two gold stars: **


def get_yes_count_part_two(input_list):
    input_set = set("".join(input_list))
    #print("input_list: ", input_list)
    yes_count = 0
    #print("input_set: ", input_set)
    for i in set(input_set):
        count = 0
        for j in input_list:
            if i in j:
                count += 1
        if count == len(input_list):
            yes_count += 1
    #print(yes_count)
    return yes_count


def get_yes_count_part_one(input_list):
    input_set = set("".join(input_list))
    #print("input_set: ", input_set)
    yes_count = len(input_set)
    #print(yes_count)
    return yes_count


if __name__ == '__main__':

    files = ['20201206-example.txt', '20201206-input.txt']

    for file_name in files:
        print("\n" + file_name)
        with open(file_name) as f:
            group_answers = f.readlines()

        len_rows = len(group_answers)

        answers_per_group_list = []
        yes_count_per_group_list_p1 = []
        yes_count_per_group_list_p2 = []
        row_count = 0
        while row_count < len_rows:
            # Each row is an answer
            answer = group_answers[row_count].strip()

            # Add all answers belonging to a group to a list
            if answer != "":
                answers_per_group_list.append(answer)

            if answer == "" or row_count + 1 == len_rows:
                yes_count_per_group_list_p1.append(get_yes_count_part_one(answers_per_group_list))
                yes_count_per_group_list_p2.append(get_yes_count_part_two(answers_per_group_list))
                answers_per_group_list = []

            row_count += 1

        print("Part 1: ", sum(yes_count_per_group_list_p1))
        print("Part 2: ", sum(yes_count_per_group_list_p2))
