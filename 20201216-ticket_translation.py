# --- Day 16: Ticket Translation ---
# As you're walking to yet another connecting flight, you realize that one of the legs of your re-routed trip coming up is on a high-speed train. However, the train ticket you were given is in a language you don't understand. You should probably figure out what it says before you get to the train station after the next flight.
#
# Unfortunately, you can't actually read the words on the ticket. You can, however, read the numbers, and so you figure out the fields these tickets must have and the valid ranges for values in those fields.
#
# You collect the rules for ticket fields, the numbers on your ticket, and the numbers on other nearby tickets for the same train service (via the airport security cameras) together into a single document you can reference (your puzzle input).
#
# The rules for ticket fields specify a list of fields that exist somewhere on the ticket and the valid ranges of values for each field. For example, a rule like class: 1-3 or 5-7 means that one of the fields in every ticket is named class and can be any value in the ranges 1-3 or 5-7 (inclusive, such that 3 and 5 are both valid in this field, but 4 is not).
#
# Each ticket is represented by a single line of comma-separated values. The values are the numbers on the ticket in the order they appear; every ticket has the same format. For example, consider this ticket:
#
# .--------------------------------------------------------.
# | ????: 101    ?????: 102   ??????????: 103     ???: 104 |
# |                                                        |
# | ??: 301  ??: 302             ???????: 303      ??????? |
# | ??: 401  ??: 402           ???? ????: 403    ????????? |
# '--------------------------------------------------------'
# Here, ? represents text in a language you don't understand. This ticket might be represented as 101,102,103,104,301,302,303,401,402,403; of course, the actual train tickets you're looking at are much more complicated. In any case, you've extracted just the numbers in such a way that the first number is always the same specific field, the second number is always a different specific field, and so on - you just don't know what each position actually means!
#
# Start by determining which tickets are completely invalid; these are tickets that contain values which aren't valid for any field. Ignore your ticket for now.
#
# For example, suppose you have the following notes:
#
# class: 1-3 or 5-7
# row: 6-11 or 33-44
# seat: 13-40 or 45-50
#
# your ticket:
# 7,1,14
#
# nearby tickets:
# 7,3,47
# 40,4,50
# 55,2,20
# 38,6,12
# It doesn't matter which position corresponds to which field; you can identify invalid nearby tickets by considering only whether tickets contain values that are not valid for any field. In this example, the values on the first nearby ticket are all valid for at least one field. This is not true of the other three nearby tickets: the values 4, 55, and 12 are are not valid for any field. Adding together all of the invalid values produces your ticket scanning error rate: 4 + 55 + 12 = 71.
#
# Consider the validity of the nearby tickets you scanned. What is your ticket scanning error rate?
#
# Your puzzle answer was 21996.
#
# --- Part Two ---
# Now that you've identified which tickets contain invalid values, discard those tickets entirely. Use the remaining valid tickets to determine which field is which.
#
# Using the valid ranges for each field, determine what order the fields appear on the tickets. The order is consistent between all tickets: if seat is the third field, it is the third field on every ticket, including your ticket.
#
# For example, suppose you have the following notes:
#
# class: 0-1 or 4-19
# row: 0-5 or 8-19
# seat: 0-13 or 16-19
#
# your ticket:
# 11,12,13
#
# nearby tickets:
# 3,9,18
# 15,1,5
# 5,14,9
# Based on the nearby tickets in the above example, the first position must be row, the second position must be class, and the third position must be seat; you can conclude that in your ticket, class is 12, row is 11, and seat is 13.
#
# Once you work out which field is which, look for the six fields on your ticket that start with the word departure. What do you get if you multiply those six values together?
#
# Your puzzle answer was 650080463519.
#
# Both parts of this puzzle are complete! They provide two gold stars: **


import copy

# Hard to read code that works but would require a complete refactoring
if __name__ == '__main__':

    files = ['20201216-example_p1.txt', '20201216-input.txt']

    for file_name in files:
        print("\n****************************\n" + file_name)
        with open(file_name) as f:
            lines = f.readlines()

        idx_your_ticket = lines.index("your ticket:\n")
        idx_nearby_tickets = lines.index("nearby tickets:\n")

        rules = []
        nearby_tickets = []
        complete_range = []

        for idx in range(len(lines)):
            if idx < idx_your_ticket -1:
                rule = {'name': lines[idx].split(':')[0].strip()}
                ranges = [ra.strip() for ra in lines[idx].split(':')[1].split('or')]
                rule['r1'] = range(int(ranges[0].strip().split('-')[0]), int(ranges[0].strip().split('-')[1]) + 1)
                rule['r2'] = range(int(ranges[1].strip().split('-')[0]), int(ranges[1].strip().split('-')[1]) + 1)
                rule['r'] = list(rule['r1']) + list(rule['r2'])
                rules.append(rule)
                complete_range += list(rule['r1']) + list(rule['r2'])
            if idx == idx_your_ticket + 1:
                my_ticket = [int(n.strip()) for n in lines[idx].split(',')]
            if idx > idx_nearby_tickets:
                nearby_ticket = [int(n.strip()) for n in lines[idx].split(',')]
                nearby_tickets.append(nearby_ticket)

        print("rules: ", rules)
        print("my_ticket: ", my_ticket)
        print("nearby_tickets: ", nearby_tickets)

        print("\nPart One")

        print("complete_range: ", complete_range)
        no_duplicates = set(complete_range)
        print("no_duplicates: ", no_duplicates)

        not_included_list = []
        valid_tickets = []
        not_valid_tickets = []

        print("Is my_ticket included in rule ranges?")
        if set(my_ticket).issubset(no_duplicates):
            print("Yes")
            print(all([x in no_duplicates for x in my_ticket]))
            valid_tickets.append(my_ticket)
        else:
            not_included_list = [x for x in my_ticket if x not in no_duplicates]

        for nt in nearby_tickets:
            if set(nt).issubset(no_duplicates):
                valid_tickets.append(nt)
            else:
                not_included_list += [x for x in nt if x not in no_duplicates]

        print("not valid tickets: ", [nt for nt in nearby_tickets if nt not in valid_tickets])
        print("valid_tickets: ", valid_tickets)
        print("not_include_list: ", not_included_list)
        print("Sum: ", sum(not_included_list))

        if file_name.find('p1') < 0:
            print("\nPart Two")

            copy_vt = copy.deepcopy(valid_tickets)
            copy_my_ticket = copy.deepcopy(my_ticket)

            for vt in valid_tickets:
                for t_idx in range(len(rules)):
                    matching_rules = []
                    for r_idx in range(len(rules)):
                        if vt[t_idx] in rules[r_idx]['r1'] or vt[t_idx] in rules[r_idx]['r2']:
                            #print("rule {} matches ticket index {}".format(rules[r_idx]['name'], t_idx))
                            #print("Replace vt[t_idx] with r_idx: {} with {}".format(vt[t_idx], rules[r_idx]['name']))
                            matching_rules.append(rules[r_idx]['name'])
                            #matching_rules.append(r_idx)
                    vt[t_idx] = matching_rules

            print("rules: ")#, rules)
            print("\n".join(str(r) for r in rules))

            #print("valid_tickets: ")#, valid_tickets)
            #print("\n".join(str(i) + ' ticket: ' +  str(vt) for i, vt in enumerate(valid_tickets)))

            #print("Transposed valid tickets: ")
            transpose_vt = list(zip(*valid_tickets))
            #print("\n".join(str(i) + ' ticket field: ' +  str(vt) for i, vt in enumerate(transpose_vt)))

            print("Set of transposed valid tickets: ")

            len_complete = len(rules) * len(valid_tickets)
            for tf in range(len(transpose_vt)):
                len_of_vt = 0
                complete_vt_list = []
                for l in transpose_vt[tf]:
                    len_of_vt += len(l)
                    complete_vt_list += l
                if len_of_vt == len_complete:
                    index_field_for_which_each_rule_is_valid = tf
                    set_field_for_which_each_rule_is_valid = set(complete_vt_list)
            print("index_field_for_which_each_rule_is_valid: ", index_field_for_which_each_rule_is_valid)
            print("set_field_for_which_each_rule_is_valid: ", set_field_for_which_each_rule_is_valid)

            results = {}

            for r in set_field_for_which_each_rule_is_valid:

                rule_missing_tf = []
                rule_match_tf = []

                for tf in range(len(transpose_vt)):
                    r_found_counter_per_tf = 0
                    if tf == index_field_for_which_each_rule_is_valid:
                        continue
                    for l in transpose_vt[tf]:
                        if r in l:
                            r_found_counter_per_tf += 1
                    if r_found_counter_per_tf != len(transpose_vt[tf]):
                        #print("transpose_vt[{}] is missing rule {}".format(tf, r))
                        rule_missing_tf.append(tf)
                    else:
                        #print("transpose_vt[{}] is NOT missing rule {}".format(tf, r))
                        rule_match_tf.append(tf)

                if len(rule_match_tf) > 0: #and tf not in skip_tf:
                    results[r] = rule_match_tf

                    #print("rule_match_tf: ", rule_match_tf)

            print("results: ", results)

            values_processed = []
            is_in_progress = True

            while is_in_progress:

                is_in_progress = False

                for r_idx in range(len(rules)):
                    list_val = results.get(rules[r_idx]['name'], [])
                    if len(list_val) == 1 and list_val[0] not in values_processed:
                        value_to_be_removed = list_val[0]
                        values_processed.append(list_val[0])
                        is_in_progress = True
                        for r1_idx in range(len(rules)):
                            if r1_idx == r_idx:
                                continue
                            #print("results.get(rules[r1_idx]['name']: ", results.get(rules[r1_idx]['name']))
                            tmp_list = results.get(rules[r1_idx]['name'], [])
                            if value_to_be_removed in tmp_list:
                                tmp_list.remove(value_to_be_removed)
                                #print("results.get(rules[r1_idx]['name']: ", results.get(rules[r1_idx]['name']))


            print("results: ", results)

            departure_list = []
            for k, v in results.items():
                if k.startswith("departure"):
                    departure_list.append(int(v[0]))

            #print("departure_list: ")
            #print("\n".join(str(d) for d in departure_list))

            product = 1
            for d in departure_list:
                print("Ticket values belonging to departure fields: ", copy_my_ticket[d])
                product *= copy_my_ticket[d]

            print("product: ", product)
