# --- Day 18: Operation Order ---
# As you look out the window and notice a heavily-forested continent slowly appear over the horizon, you are interrupted by the child sitting next to you. They're curious if you could help them with their math homework.
#
# Unfortunately, it seems like this "math" follows different rules than you remember.
#
# The homework (your puzzle input) consists of a series of expressions that consist of addition (+), multiplication (*), and parentheses ((...)). Just like normal math, parentheses indicate that the expression inside must be evaluated before it can be used by the surrounding expression. Addition still finds the sum of the numbers on both sides of the operator, and multiplication still finds the product.
#
# However, the rules of operator precedence have changed. Rather than evaluating multiplication before addition, the operators have the same precedence, and are evaluated left-to-right regardless of the order in which they appear.
#
# For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are as follows:
#
# 1 + 2 * 3 + 4 * 5 + 6
#   3   * 3 + 4 * 5 + 6
#       9   + 4 * 5 + 6
#          13   * 5 + 6
#              65   + 6
#                  71
# Parentheses can override this order; for example, here is what happens if parentheses are added to form 1 + (2 * 3) + (4 * (5 + 6)):
#
# 1 + (2 * 3) + (4 * (5 + 6))
# 1 +    6    + (4 * (5 + 6))
#      7      + (4 * (5 + 6))
#      7      + (4 *   11   )
#      7      +     44
#             51
# Here are a few more examples:
#
# 2 * 3 + (4 * 5) becomes 26.
# 5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437.
# 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 12240.
# ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 13632.
# Before you can help with the homework, you need to understand it yourself. Evaluate the expression on each line of the homework; what is the sum of the resulting values?
#
# Your puzzle answer was 69490582260.
#
# --- Part Two ---
# You manage to answer the child's questions and they finish part 1 of their homework, but get stuck when they reach the next section: advanced math.
#
# Now, addition and multiplication have different precedence levels, but they're not the ones you're familiar with. Instead, addition is evaluated before multiplication.
#
# For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are now as follows:
#
# 1 + 2 * 3 + 4 * 5 + 6
#   3   * 3 + 4 * 5 + 6
#   3   *   7   * 5 + 6
#   3   *   7   *  11
#      21       *  11
#          231
# Here are the other examples from above:
#
# 1 + (2 * 3) + (4 * (5 + 6)) still becomes 51.
# 2 * 3 + (4 * 5) becomes 46.
# 5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 1445.
# 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
# ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.
# What do you get if you add up the results of evaluating the homework problems using these new rules?
#
# Your puzzle answer was 362464596624526.
#
# Both parts of this puzzle are complete! They provide two gold stars: **


import re
from pprint import pprint


def get_result_addition_higher_than_multiplication(e):

    e = add_space_around_parentheses(e)

    e_list = [exp.split() for exp in e.split("*")]
    #print("e_list: ", e_list)

    new_e_list = []

    # Perform simple addition operations
    for e_idx in range(len(e_list)):
        sub_addition_exp = " ".join(e_list[e_idx])
        #print("sub_addition_exp: ", sub_addition_exp)
        # No parentheses or start and end of parentheses is included
        if (sub_addition_exp.find("(") < 0 and sub_addition_exp.find(")") < 0) or \
           (sub_addition_exp.count("(") == sub_addition_exp.count(")") and \
           sub_addition_exp.find("(") < sub_addition_exp.find(")")):
            new_e_list.append(str(get_result_of_expression(sub_addition_exp)))
        else:
            new_e_list.append(sub_addition_exp)

    #print("new_e_list: ", new_e_list)

    new_e = " * ".join(exp for exp in new_e_list)
    #print("new_e: ", new_e)
    new_e = add_parentheses_around_addition(new_e)
    #print("new_e: ", new_e)

    return get_result_of_expression(new_e)


def add_parentheses_around_addition(e):
    #print("e: ", e)

    char_idx_list = []
    for c in range(len(e)):
        if e[c] == "+":
            char_idx_list.append(c)

    offset_count_p_added = 0
    added_end_parentheses_idx_list = []

    for c in char_idx_list:

        c_idx = c + offset_count_p_added

        offset_decrease = 0
        for p in added_end_parentheses_idx_list:
            if c_idx < p + offset_count_p_added:
                offset_decrease += 1

        c_idx = c + offset_count_p_added - offset_decrease

        #print("char_idx_list: ", char_idx_list)
        #print("e: ", e)
        #print("c: ", c)
        #print("added_end_parentheses_idx_list: ", added_end_parentheses_idx_list)
        #print("len(added_end_parentheses_idx_list): ", len(added_end_parentheses_idx_list))
        #print("offset_decrease: ", offset_decrease)
        #print("offset_count_p_added: ", offset_count_p_added)
        #print("c_idx: ", c_idx)

        if e[c_idx-2] == ")":

            #print("e[:c_idx-2]: ", e[:c_idx-2])
            # 2 Options:
            # 1. From end ), go left and some next char is (
            # 2. From end ), go left and some next char is another ),
            # which leads to increasing number of ( to be found by 1
            start_p_found = 0
            start_p_to_be_found = 1
            start_p_added = False
            for p_idx in range(c_idx -3, -1, -1):
                if e[p_idx] == ")":
                    start_p_to_be_found += 1
                elif e[p_idx] == "(":
                    start_p_found += 1

                if start_p_found == start_p_to_be_found:
                    #print("start_p_found: ", start_p_found)
                    #print("start_p_to_be_found: ", start_p_to_be_found)
                    #print("c_idx-3: ", c_idx-3)
                    #print("p_idx: ", p_idx)

                    e = e[:p_idx] + "(" + e[p_idx:]
                    offset_count_p_added += 1
                    start_p_added = True

                    #print("e added (: ", e)

                    break

            if not start_p_added:
                #print("e not added (: ", e)
                pass

        else:
            #print("e[:c_idx-2]: ", e[:c_idx-2])
            # Add before number a starting parentheses
            e = e[:c_idx-2] + "(" + e[c_idx-2:]
            offset_count_p_added += 1

        c_idx = c + offset_count_p_added - offset_decrease

        # Is char after + a start parentheses or a number?
        if e[c_idx+2] == "(":
            #print("e[:c_idx+2]: ", e[:c_idx+2])
            # 2 Options:
            # 1. From starting (, go right and some next char is )
            # 2. From starting (, go right and some next char is another (,
            # which leads to increasing number of ) to be found by 1
            end_p_found = 0
            end_p_to_be_found = 1
            for p_idx in range(c_idx + 3, len(e)):
                if e[p_idx] == "(":
                    end_p_to_be_found += 1
                elif e[p_idx] == ")":
                    end_p_found += 1

                if end_p_found == end_p_to_be_found:
                    #print("end_p_found: ", end_p_found)
                    #print("end_p_to_be_found: ", end_p_to_be_found)
                    #print("c_idx: ", c_idx)
                    #print("p_idx: ", p_idx)

                    e = e[:p_idx] + ")" + e[p_idx:]

                    # Edge cases: Some next or all next c_idx < p_idx
                    added_end_parentheses_idx_list.append(p_idx - offset_count_p_added)

                    offset_count_p_added += 1

                    #print("e added ): ", e)

                    break
        else:
            #print("e[:c_idx+2]: ", e[:c_idx+2])
            # Add after number an end parentheses
            e = e[:c_idx+3] + ")" + e[c_idx+3:]
            offset_count_p_added += 1

    #print("e: ", e)

    return e


def get_result_of_expression(e):

    e = add_space_around_parentheses(e)

    # Generate expression list splitted by blanks
    e_list = e.split()

    # Print if parentheses are not single list items
    for e_idx in range(len(e_list)):
        if (e_list[e_idx].startswith("(") or e_list[e_idx].endswith(")")) and len(e_list[e_idx]) > 1:
            print("ERROR: Expected parentheses as separate list item, actual: ", e_list[e_idx])

    regex_number = "^([0-9]|[0-9]*)$"
    regex_start_parentheses = "^(\(*)$"
    sub_exp = ""
    parentheses_exp = ""
    skip_e_idx_until_less_than = -1

    #print("e_list: ", e_list)
    for e_idx in range(len(e_list)):

        if skip_e_idx_until_less_than < e_idx:
            # Check for number and add to tmp_exp
            if re.match(regex_number, e_list[e_idx]):
                sub_exp += e_list[e_idx]

            # Check for operator and add to tmp_exp
            elif e_list[e_idx] == "+" or e_list[e_idx] == "*":
                sub_exp += e_list[e_idx]

            # Check for parentheses
            elif re.match(regex_start_parentheses, e_list[e_idx]):
                # Get everything inside parentheses in new string
                # Remove outer parentheses
                # Recursively call get_result_of_expression
                # Add returned result to sub_exp

                # 2 Options:
                # 1. From starting (, go right and some next char is )
                # 2. From starting (, go right and some next char is another (,
                # which leads to increasing number of ) to be found by 1
                end_p_found = 0
                end_p_to_be_found = 1
                for p_idx in range(e_idx +1, len(e_list)):
                    if e_list[p_idx] == "(":
                        end_p_to_be_found += 1
                    elif e_list[p_idx] == ")":
                        end_p_found += 1
                    if end_p_found == end_p_to_be_found:
                        #print("e_idx: ", e_idx)
                        #print("p_idx: ", p_idx)
                        parentheses_exp = " ".join(e_list[e_idx+1:p_idx])
                        skip_e_idx_until_less_than = p_idx
                        break
                #print("parentheses_exp: ", parentheses_exp)
                sub_exp += str(get_result_of_expression(parentheses_exp))

        #print("sub_exp: ", sub_exp)
        # If sub_exp does not contain a parentheses start "(" and
        # contains only * or contain only + and
        # not ends with + or +, then calculate expression
        if sub_exp.find("(") < 0 and ((sub_exp.find("*") >= 0 and sub_exp.find("+") < 0) or (sub_exp.find("*") < 0 and \
           sub_exp.find("+") >= 0)) and not sub_exp.endswith("*") and not sub_exp.endswith("+"):
            sub_exp = str(eval(sub_exp))
            #print("new calc sub_exp: ", sub_exp)

    r = eval(sub_exp)

    return r


def add_space_around_parentheses(e):
    #print("e: ", e)

    # Add space before and after all parentheses
    char_idx_list = []
    for char_idx in range(len(e)):
      if e[char_idx] == "(" or e[char_idx] == ")":
          char_idx_list.append(char_idx)
    offset = 0
    for char in char_idx_list:
        e = e[:char + offset] + " " + e[char + offset] + " " + e[char + 1 + offset:]
        offset += 2

    #print("e: ", e)

    return e


# Works fine, but hard to read; Easier solution in Python: Own class, with adapted magic methods for add, etc.
if __name__ == '__main__':

    files = ['20201218-example.txt', '20201218-input.txt']

    for file_name in files:
        print("\n****************************\n" + file_name)
        with open(file_name) as f:
            expressions = f.readlines()

        results = []

        for i in range(len(expressions)):

            exp_str = expressions[i].strip()
            exp = {'pos': i, 'exp': exp_str}

            result_part_one = get_result_of_expression(exp_str)

            result_part_two = get_result_addition_higher_than_multiplication(exp_str)

            exp['result_part_one'] = result_part_one
            exp['result_part_two'] = result_part_two

            #print("exp: ", exp)
            results.append(exp)

        #print("results:")
        #pprint(results)

        if file_name.find('example') != -1:
            expected_test_results_part_one = [71, 51, 26, 437, 12240, 13632]
            print("matched expected_test_results_part_one: ", expected_test_results_part_one)

            expected_test_results_part_two = [231, 51, 46, 1445, 669060, 23340]
            print("matched expected_test_results_part_two: ", expected_test_results_part_two)

        print("Part One - sum of all results: ", sum([r['result_part_one'] for r in results]))
        print("Part Two - sum of all results: ", sum([r['result_part_two'] for r in results]))
