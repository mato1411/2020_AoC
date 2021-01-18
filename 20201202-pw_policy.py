# --- Day 2: Password Philosophy ---
# Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.
#
# The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.
#
# Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.
#
# To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.
#
# For example, suppose you have the following list:
#
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
#
# In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.
#
# How many passwords are valid according to their policies?
#
# Your puzzle answer was 456.
#
# --- Part Two ---
# While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.
#
# The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.
#
# Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
#
# Given the same example list from above:
#
# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
# How many passwords are valid according to the new interpretation of the policies?
#
# Your puzzle answer was 308.
#
# Both parts of this puzzle are complete! They provide two gold stars: **


def is_pw_valid(policy_pw_line, is_part_2 = False):
    pw = policy_pw_line[policy_pw_line.find(":") + 1:].strip()
    character = policy_pw_line[:policy_pw_line.find(":")].strip().split()[1]

    min_occurrence = int(policy_pw_line[:policy_pw_line.find(":")].strip().split()[0].split("-")[0])
    max_occurrence = int(policy_pw_line[:policy_pw_line.find(":")].strip().split()[0].split("-")[1])

    char_index_pos_one = int(policy_pw_line[:policy_pw_line.find(":")].strip().split()[0].split("-")[0]) - 1
    char_index_pos_two = int(policy_pw_line[:policy_pw_line.find(":")].strip().split()[0].split("-")[1]) - 1

    # print("pw: ", pw)
    # print("character: ", character)
    if not is_part_2:
        # print("min_occurrence: ", min_occurrence)
        # print("max_occurrence: ", max_occurrence)

        pw_letter_count = 0
        char_match_count = 0

        while pw_letter_count < len(pw):
            if pw[pw_letter_count] == character:
                char_match_count += 1
            pw_letter_count += 1

        if min_occurrence <= char_match_count <= max_occurrence:
            return True, pw

    elif is_part_2:
        # print("char_index_pos_one: ", char_index_pos_one)
        # print("char_index_pos_two: ", char_index_pos_two)
        if char_index_pos_one <= len(pw) and char_index_pos_two <= len(pw):
            if pw[char_index_pos_one] == character and pw[char_index_pos_two] != character or pw[char_index_pos_one] != character and pw[char_index_pos_two] == character:
                return True, pw

    return False, pw


if __name__ == '__main__':

    files = ['20201202-example.txt', '20201202-input.txt']

    for file_name in files:
        print("\n" + file_name)
        with open(file_name) as f:
            lines = f.readlines()

        valid_pws_part_one = []
        valid_regex_print_part_one = []
        not_valid_pws_part_one = []
        not_valid_regex_print_part_one = []

        valid_pws_part_two = []
        valid_regex_print_part_two = []
        not_valid_pws_part_two = []
        not_valid_regex_print_part_two = []

        valid_pw_count_part_one = 0
        valid_pw_count_part_two = 0

        count = 0
        pws_to_be_validated = len(lines)
        while count < pws_to_be_validated:
            for is_part_two in [False, True]:
                valid_str = "not valid"
                is_valid, pw = is_pw_valid(lines[count], is_part_two)
                if is_valid:
                    valid_str = "valid"
                    if not is_part_two:
                        valid_pw_count_part_one += 1
                        valid_pws_part_one.append(pw)
                        valid_regex_print_part_one.append(lines[count])
                    elif is_part_two:
                        valid_pw_count_part_two += 1
                        valid_pws_part_two.append(pw)
                        valid_regex_print_part_two.append(lines[count])
                else:
                    if not is_part_two:
                        not_valid_pws_part_one.append(pw)
                        not_valid_regex_print_part_one.append(lines[count])
                    elif is_part_two:
                        not_valid_pws_part_two.append(pw)
                        not_valid_regex_print_part_two.append(lines[count])
                #policy_number = 2 if is_part_two else 1
                #print("Password {}/{}: Policy {} - '{}' is {}".format(count + 1, pws_to_be_validated, policy_number, lines[count].strip(), valid_str))

            count += 1

        print("\n*** Policy Part one ***")
        print("Valid passwords: ", valid_pws_part_one)
        print("Valid passwords check: ", valid_regex_print_part_one)
        print("Not valid passwords: ", not_valid_pws_part_one)
        print("Not valid passwords check: ", not_valid_regex_print_part_one)
        print("Valid password count: ", valid_pw_count_part_one)
        print("Not valid password count: ", pws_to_be_validated - valid_pw_count_part_one)

        print("\n*** Policy Part two ***")
        print("Valid passwords: ", valid_pws_part_two)
        print("Valid passwords check: ", valid_regex_print_part_two)
        print("Not valid passwords: ", not_valid_pws_part_two)
        print("Not valid passwords check: ", not_valid_regex_print_part_two)
        print("Valid password count: ", valid_pw_count_part_two)
        print("Not valid password count: ", pws_to_be_validated - valid_pw_count_part_two)

        # print("Not valid passwords regex check: ", "\n".join(not_valid_regex_print))
