# --- Day 19: Monster Messages ---
# You land in an airport surrounded by dense forest. As you walk to your high-speed train, the Elves at the Mythical Information Bureau contact you again. They think their satellite has collected an image of a sea monster! Unfortunately, the connection to the satellite is having problems, and many of the messages sent back from the satellite have been corrupted.
#
# They sent you a list of the rules valid messages should obey and a list of received messages they've collected so far (your puzzle input).
#
# The rules for valid messages (the top part of your puzzle input) are numbered and build upon each other. For example:
#
# 0: 1 2
# 1: "a"
# 2: 1 3 | 3 1
# 3: "b"
# Some rules, like 3: "b", simply match a single character (in this case, b).
#
# The remaining rules list the sub-rules that must be followed; for example, the rule 0: 1 2 means that to match rule 0, the text being checked must match rule 1, and the text after the part that matched rule 1 must then match rule 2.
#
# Some of the rules have multiple lists of sub-rules separated by a pipe (|). This means that at least one list of sub-rules must match. (The ones that match might be different each time the rule is encountered.) For example, the rule 2: 1 3 | 3 1 means that to match rule 2, the text being checked must match rule 1 followed by rule 3 or it must match rule 3 followed by rule 1.
#
# Fortunately, there are no loops in the rules, so the list of possible matches will be finite. Since rule 1 matches a and rule 3 matches b, rule 2 matches either ab or ba. Therefore, rule 0 matches aab or aba.
#
# Here's a more interesting example:
#
# 0: 4 1 5
# 1: 2 3 | 3 2
# 2: 4 4 | 5 5
# 3: 4 5 | 5 4
# 4: "a"
# 5: "b"
# Here, because rule 4 matches a and rule 5 matches b, rule 2 matches two letters that are the same (aa or bb), and rule 3 matches two letters that are different (ab or ba).
#
# Since rule 1 matches rules 2 and 3 once each in either order, it must match two pairs of letters, one pair with matching letters and one pair with different letters. This leaves eight possibilities: aaab, aaba, bbab, bbba, abaa, abbb, baaa, or babb.
#
# Rule 0, therefore, matches a (rule 4), then any of the eight options from rule 1, then b (rule 5): aaaabb, aaabab, abbabb, abbbab, aabaab, aabbbb, abaaab, or ababbb.
#
# The received messages (the bottom part of your puzzle input) need to be checked against the rules so you can determine which are valid and which are corrupted. Including the rules and the messages together, this might look like:
#
# 0: 4 1 5
# 1: 2 3 | 3 2
# 2: 4 4 | 5 5
# 3: 4 5 | 5 4
# 4: "a"
# 5: "b"
#
# ababbb
# bababa
# abbbab
# aaabbb
# aaaabbb
# Your goal is to determine the number of messages that completely match rule 0. In the above example, ababbb and abbbab match, but bababa, aaabbb, and aaaabbb do not, producing the answer 2. The whole message must match all of rule 0; there can't be extra unmatched characters in the message. (For example, aaaabbb might appear to match rule 0 above, but it has an extra unmatched b on the end.)
#
# How many messages completely match rule 0?
#
# Your puzzle answer was 171.
#
# --- Part Two ---
# As you look over the list of messages, you realize your matching rules aren't quite right. To fix them, completely replace rules 8: 42 and 11: 42 31 with the following:
#
# 8: 42 | 42 8
# 11: 42 31 | 42 11 31
# This small change has a big impact: now, the rules do contain loops, and the list of messages they could hypothetically match is infinite. You'll need to determine how these changes affect which messages are valid.
#
# Fortunately, many of the rules are unaffected by this change; it might help to start by looking at which rules always match the same set of values and how those rules (especially rules 42 and 31) are used by the new versions of rules 8 and 11.
#
# (Remember, you only need to handle the rules you have; building a solution that could handle any hypothetical combination of rules would be significantly more difficult.)
#
# For example:
#
# 42: 9 14 | 10 1
# 9: 14 27 | 1 26
# 10: 23 14 | 28 1
# 1: "a"
# 11: 42 31
# 5: 1 14 | 15 1
# 19: 14 1 | 14 14
# 12: 24 14 | 19 1
# 16: 15 1 | 14 14
# 31: 14 17 | 1 13
# 6: 14 14 | 1 14
# 2: 1 24 | 14 4
# 0: 8 11
# 13: 14 3 | 1 12
# 15: 1 | 14
# 17: 14 2 | 1 7
# 23: 25 1 | 22 14
# 28: 16 1
# 4: 1 1
# 20: 14 14 | 1 15
# 3: 5 14 | 16 1
# 27: 1 6 | 14 18
# 14: "b"
# 21: 14 1 | 1 14
# 25: 1 1 | 1 14
# 22: 14 14
# 8: 42
# 26: 14 22 | 1 20
# 18: 15 15
# 7: 14 5 | 1 21
# 24: 14 1
#
# abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
# bbabbbbaabaabba
# babbbbaabbbbbabbbbbbaabaaabaaa
# aaabbbbbbaaaabaababaabababbabaaabbababababaaa
# bbbbbbbaaaabbbbaaabbabaaa
# bbbababbbbaaaaaaaabbababaaababaabab
# ababaaaaaabaaab
# ababaaaaabbbaba
# baabbaaaabbaaaababbaababb
# abbbbabbbbaaaababbbbbbaaaababb
# aaaaabbaabaaaaababaa
# aaaabbaaaabbaaa
# aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
# babaaabbbaaabaababbaabababaaab
# aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
# Without updating rules 8 and 11, these rules only match three messages: bbabbbbaabaabba, ababaaaaaabaaab, and ababaaaaabbbaba.
#
# However, after updating rules 8 and 11, a total of 12 messages match:
#
# bbabbbbaabaabba
# babbbbaabbbbbabbbbbbaabaaabaaa
# aaabbbbbbaaaabaababaabababbabaaabbababababaaa
# bbbbbbbaaaabbbbaaabbabaaa
# bbbababbbbaaaaaaaabbababaaababaabab
# ababaaaaaabaaab
# ababaaaaabbbaba
# baabbaaaabbaaaababbaababb
# abbbbabbbbaaaababbbbbbaaaababb
# aaaaabbaabaaaaababaa
# aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
# aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
# After updating rules 8 and 11, how many messages completely match rule 0?
#
# Your puzzle answer was 369.
#
# Both parts of this puzzle are complete! They provide two gold stars: **


import copy
import re
from pprint import pprint


def generated_regex(r, is_p2 = False):

    global rules
    global rules_p2
    global rec_count
    global count_r8
    global count_r11
    global regex
    global reoccurring_r

    if is_p2:
        #print("is_p2: ", is_p2)
        rules = rules_p2
        #print("r: ", r)
        reoccurring_r.append(r)
        if r == 8:
            count_r8 += 1
        if r == 11:
            count_r11 += 1
    else:
        count_r8 = 0
        count_r11 = 0

        #print("count_r8: ", count_r8)
        #print("count_r11: ", count_r11)

    rec_count += 1
    #print("Recursion: ", rec_count)

    r_dict = rules.get(r)

    #print("r_dict: ", r_dict)

    # Ignore or_index key
    or_index = r_dict.get('or_index')
    #print("or_index: ", or_index)
    if or_index != -1:
        regex += "("
    for ref_idx in range(len(r_dict) - 1):
        ref = r_dict.get(ref_idx)
        #print("ref: ", ref)
        #print("ref_idx: ", ref_idx)
        if ref == 'a' or ref == 'b':
            regex += ref
        elif ref_idx == or_index and or_index != -1:
            regex += "|"
            generated_regex(ref, is_p2)
        else:
            if count_r8 < 5:
                generated_regex(ref, is_p2)
            elif count_r11 < 5 and ref != 8:
                generated_regex(ref, is_p2)
            elif ref != 8 and ref != 11:
                generated_regex(ref, is_p2)

        # Was last item
        if ref_idx == len(r_dict) - 2 and or_index != -1:
            regex += ")"

        #print("regex: ", regex)


if __name__ == '__main__':

    files = ['20201219-example_p1.txt', '20201219-example_p2.txt', '20201219-input.txt']

    for file_name in files:
        print("\n****************************\n" + file_name)
        with open(file_name) as f:
            lines = f.readlines()

        rules = {}
        messages = []
        is_rules = True

        # Read rules and messages
        for i in range(len(lines)):

            if lines[i].strip() == "":
                is_rules = False
                continue

            if is_rules:
                rule = {}
                rule_int = int(lines[i].split(":")[0].strip())
                values_str = lines[i].split(":")[1].strip()
                if values_str.find("|") == -1:
                    values = values_str.split()
                    rule['or_index'] = -1
                else:
                    left_or_values = values_str.split("|")[0].split()
                    right_or_values = values_str.split("|")[1].split()
                    values = left_or_values + right_or_values
                    rule['or_index'] = len(left_or_values)
                for v_idx in range(len(values)):
                    try:
                        rule[v_idx] = int(values[v_idx].replace("\"", ""))
                    except ValueError as e:
                        rule[v_idx] = values[v_idx].replace("\"", "")
                rules[rule_int] = rule
            # Is message and not a rule
            else:
                messages.append(lines[i].strip())

        #print("rules:")
        #pprint(rules)
        #print("messages: ")
        #pprint(messages)

        if file_name.find('p2') < 0:

            print("Part One")
            rec_count = 0
            rule_to_be_applied = 0
            regex = "^"
            generated_regex(rule_to_be_applied)
            regex += "$"
            print("regex")
            pprint(regex)

            count_valid_m = 0
            for m in messages:
                search = re.fullmatch(regex, m)
                #print("search: ", search)
                if search:
                    count_valid_m += 1

            print("count_valid_m: ", count_valid_m)

        if file_name.find('p1') < 0:
            print("\nPart Two")

            rules_p2 = copy.deepcopy(rules)

            print("rules_p2.get(8): ", rules_p2.get(8))
            print("rules_p2.get(11): ", rules_p2.get(11))

            print("Now adapt rule 8 and 11..")
            # 8: 42 | 42 8
            rules_p2[8] = {0: 42, 1: 42, 2: 8, 'or_index': 1}
            # 11: 42 31 | 42 11 31
            rules_p2[11] = {0: 42, 1: 31, 2: 42, 3: 11, 4: 31, 'or_index': 2}
            print("rules_p2.get(8): ", rules_p2.get(8))
            print("rules_p2.get(11): ", rules_p2.get(11))

            rec_count = 0
            count_r8 = 0
            count_r11 = 0
            rule_to_be_applied = 0
            reoccurring_r = []
            regex = "^"
            generated_regex(rule_to_be_applied, True)
            regex += "$"
            #print("regex")
            pprint(regex)

            count_valid_m = 0
            for m in messages:
                search = re.fullmatch(regex, m)
                #print("search: ", search)
                if search:
                    count_valid_m += 1

            print("count_valid_m: ", count_valid_m)
            print("reoccuring_r: ", reoccurring_r)
