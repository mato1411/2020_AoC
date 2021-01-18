# --- Day 10: Adapter Array ---
# Patched into the aircraft's data port, you discover weather forecasts of a massive tropical storm. Before you can figure out whether it will impact your vacation plans, however, your device suddenly turns off!
#
# Its battery is dead.
#
# You'll need to plug it in. There's only one problem: the charging outlet near your seat produces the wrong number of jolts. Always prepared, you make a list of all of the joltage adapters in your bag.
#
# Each of your joltage adapters is rated for a specific output joltage (your puzzle input). Any given adapter can take an input 1, 2, or 3 jolts lower than its rating and still produce its rated output joltage.
#
# In addition, your device has a built-in joltage adapter rated for 3 jolts higher than the highest-rated adapter in your bag. (If your adapter list were 3, 9, and 6, your device's built-in adapter would be rated for 12 jolts.)
#
# Treat the charging outlet near your seat as having an effective joltage rating of 0.
#
# Since you have some time to kill, you might as well test all of your adapters. Wouldn't want to get to your resort and realize you can't even charge your device!
#
# If you use every adapter in your bag at once, what is the distribution of joltage differences between the charging outlet, the adapters, and your device?
#
# For example, suppose that in your bag, you have adapters with the following joltage ratings:
#
# 16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4
# With these adapters, your device's built-in joltage adapter would be rated for 19 + 3 = 22 jolts, 3 higher than the highest-rated adapter.
#
# Because adapters can only connect to a source 1-3 jolts lower than its rating, in order to use every adapter, you'd need to choose them like this:
#
# The charging outlet has an effective rating of 0 jolts, so the only adapters that could connect to it directly would need to have a joltage rating of 1, 2, or 3 jolts. Of these, only one you have is an adapter rated 1 jolt (difference of 1).
# From your 1-jolt rated adapter, the only choice is your 4-jolt rated adapter (difference of 3).
# From the 4-jolt rated adapter, the adapters rated 5, 6, or 7 are valid choices. However, in order to not skip any adapters, you have to pick the adapter rated 5 jolts (difference of 1).
# Similarly, the next choices would need to be the adapter rated 6 and then the adapter rated 7 (with difference of 1 and 1).
# The only adapter that works with the 7-jolt rated adapter is the one rated 10 jolts (difference of 3).
# From 10, the choices are 11 or 12; choose 11 (difference of 1) and then 12 (difference of 1).
# After 12, only valid adapter has a rating of 15 (difference of 3), then 16 (difference of 1), then 19 (difference of 3).
# Finally, your device's built-in adapter is always 3 higher than the highest adapter, so its rating is 22 jolts (always a difference of 3).
# In this example, when using every adapter, there are 7 differences of 1 jolt and 5 differences of 3 jolts.
#
# Here is a larger example:
#
# 28
# 33
# 18
# 42
# 31
# 14
# 46
# 20
# 48
# 47
# 24
# 23
# 49
# 45
# 19
# 38
# 39
# 11
# 1
# 32
# 25
# 35
# 8
# 17
# 7
# 9
# 4
# 2
# 34
# 10
# 3
# In this larger example, in a chain that uses all of the adapters, there are 22 differences of 1 jolt and 10 differences of 3 jolts.
#
# Find a chain that uses all of your adapters to connect the charging outlet to your device's built-in adapter and count the joltage differences between the charging outlet, the adapters, and your device. What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?
#
# Your puzzle answer was 1917.
#
# --- Part Two ---
# To completely determine whether you have enough adapters, you'll need to figure out how many different ways they can be arranged. Every arrangement needs to connect the charging outlet to your device. The previous rules about when adapters can successfully connect still apply.
#
# The first example above (the one that starts with 16, 10, 15) supports the following arrangements:
#
# (0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
# (0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
# (0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
# (0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4, 7, 10, 12, 15, 16, 19, (22)
# (The charging outlet and your device's built-in adapter are shown in parentheses.) Given the adapters from the first example, the total number of arrangements that connect the charging outlet to your device is 8.
#
# The second example above (the one that starts with 28, 33, 18) has many arrangements. Here are a few:
#
# (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
# 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, (52)
#
# (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
# 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 49, (52)
#
# (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
# 32, 33, 34, 35, 38, 39, 42, 45, 46, 48, 49, (52)
#
# (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
# 32, 33, 34, 35, 38, 39, 42, 45, 46, 49, (52)
#
# (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
# 32, 33, 34, 35, 38, 39, 42, 45, 47, 48, 49, (52)
#
# (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
# 46, 48, 49, (52)
#
# (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
# 46, 49, (52)
#
# (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
# 47, 48, 49, (52)
#
# (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
# 47, 49, (52)
#
# (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
# 48, 49, (52)
# In total, this set of adapters can connect the charging outlet to your device in 19208 distinct arrangements.
#
# You glance back down at your bag and try to remember why you brought so many adapters; there must be more than a trillion valid ways to arrange them! Surely, there must be an efficient way to count the arrangements.
#
# What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?
#
# Your puzzle answer was 113387824750592.
#
# Both parts of this puzzle are complete! They provide two gold stars: **


def get_next_adapter(previous_adapter, diff_end):

    global jolt_adapters_list
    for diff in range(1, diff_end):
        #print("previous_adapter: ", previous_adapter)
        #print("previous_adapter + diff: ", previous_adapter + diff)
        for jolt_adapter in jolt_adapters_list:
            #print("jolt_adapter: ", jolt_adapter)
            if jolt_adapter == previous_adapter + diff:
                    #print("match!!!")
                    return jolt_adapter, diff
    return 0, 0


def get_distinct_ways(current_adapter, adapter_list):
    global distinct_ways
    global end_adapter

    #print("current_adapter: ", current_adapter)
    #print("end_adapter: ", end_adapter)

    if current_adapter == end_adapter:
        distinct_ways += 1
        #print("distinct_ways: ", distinct_ways)
        return

    next_adapters = get_possible_next_adapters(current_adapter, diff_end, adapter_list)
    #print("next_adapters: ", next_adapters)
    for adapter in next_adapters:
        #print("distinct_ways:" ,distinct_ways)
        get_distinct_ways(adapter, adapter_list)


def get_possible_next_adapters(current_adapter, diff_end, adapter_list):
    #global jolt_adapters_list
    next_jolt_adapters = []

    for jolt_adapter in adapter_list:
        #print("jolt_adapter: ", jolt_adapter)
        for diff in range(1, diff_end):
            #print("current_adapter: ", current_adapter)
            #print("current_adapter + diff: ", current_adapter + diff)
            if jolt_adapter == current_adapter + diff:
                #print("match for diff: ", diff)
                next_jolt_adapters.append(jolt_adapter)
        # There are just maximum diff_end -1 differences per adapter allowed
        if len(next_jolt_adapters) == diff_end - 1:
            break

    return next_jolt_adapters


if __name__ == '__main__':

    files = ['20201210-example.txt', '20201210-input.txt']

    for file_name in files:
        print("\n****************************\n" + file_name)
        with open(file_name) as f:
            jolt_adapters = f.readlines()

        len_jolt_adapters = len(jolt_adapters)
        #print("len_jolt_adapters :", len_jolt_adapters)

        jolt_adapters_count = 0

        jolt_adapters_list = []

        while jolt_adapters_count < len_jolt_adapters:
            #print("jolt_adapters[jolt_adapters_count]: ", jolt_adapters[jolt_adapters_count].strip())
            number = int(jolt_adapters[jolt_adapters_count].strip())
            jolt_adapters_list.append(number)
            jolt_adapters_count += 1

        #print("jolt_adapters: ", jolt_adapters)
        #print("jolt_adapters_list: ", jolt_adapters_list)

        print("\npart 1")

        jolt_adapter_seq = []
        jolt_adapter_dict = {}
        counter = 0
        previous_adapter = 0
        # The maximum number of voltage difference that adapter can have +1,
        # because each value adapter+n is checked while n is a value in range(voltage_adapter, end_of_range_diff)
        end_of_range_diff = 4

        while counter < len_jolt_adapters:
            #print("counter: ", counter)
            next_adapter, diff = get_next_adapter(previous_adapter, end_of_range_diff)
            if next_adapter:
                jolt_adapter_dict['seq'] = counter
                jolt_adapter_dict['jolt'] = next_adapter
                jolt_adapter_dict['diff'] = diff
                jolt_adapter_seq.append(jolt_adapter_dict)
                #print("jolt_adapter_dict: ", jolt_adapter_dict)
                previous_adapter = next_adapter
                counter += 1
                jolt_adapter_dict = {}
            else:
                break

        #print("len_jolt_adapters: ", len_jolt_adapters)
        #print("len(jolt_adapter_seq): ", len(jolt_adapter_seq))
        #print("jolt_adapter_seq: ", jolt_adapter_seq)
        #print("jolt_adapter_seq:\n", "\n".join(str(j) for j in jolt_adapter_seq))

        sum_diff = 0
        count_diff_1 = 0
        count_diff_3 = 0

        for jolt_adapter in jolt_adapter_seq:
            if jolt_adapter.get('diff') == 1:
                count_diff_1 += 1
            if jolt_adapter.get('diff') == 3:
                count_diff_3 += 1
            sum_diff += jolt_adapter.get('diff')

        print("sum_diff: ", sum_diff)
        print("my adapter rating: ", sum_diff + 3)
        print("count_diff_1: ", count_diff_1)
        print("count_diff_3 + 1 (for my adapter): ", count_diff_3 + 1)
        print("count_diff_1 * (count_diff_3+1): ", count_diff_1 * (count_diff_3+1))

        print("\npart 2")

        #print("jolt_adapters_list: ", jolt_adapters_list)
        jolt_adapters_list = sorted(jolt_adapters_list)
        #print("sorted jolt_adapters_list: ", jolt_adapters_list)

        print("Let's split the sorted list when diff between current and next item is 3")

        split = False
        wrapper_list = []
        split_list = []

        for j in range(len(jolt_adapters_list)):
            # For each item, besides last item
            if j < len(jolt_adapters_list) -1:
                if jolt_adapters_list[j] + 3 == jolt_adapters_list[j+1]:
                    split = True
                if split:
                    split_list.append(jolt_adapters_list[j])
                    wrapper_list.append(split_list)
                    split_list = []
                    split = False
                else:
                    split_list.append(jolt_adapters_list[j])
            # Handle last item
            else:
                split_list.append(jolt_adapters_list[j])
                wrapper_list.append(split_list)

        #print("wrapper_list: ", wrapper_list)

        # Old: Working with test data but takes too long with input file / real data
        # start_adapter = 0
        #     end_adapter = 49
        #     diff_end = 4
        #     distinct_ways = 0
        #
        #     get_distinct_ways(start_adapter, jolt_adapters_list)
        #     print("distinct_ways: ", distinct_ways)

        distinct_way_list = []

        for i in wrapper_list:
            if i[0] - 3 < 0:
                start_adapter = 0
            else:
                start_adapter = i[0] - 3

            end_adapter = i[-1]
            diff_end = 4
            distinct_ways = 0

            get_distinct_ways(start_adapter, i)

            distinct_way_list.append(distinct_ways)
            #print("distinct_way_list: ", distinct_way_list)

            product = 1

            for i in distinct_way_list:
                product *= i

            print(product)
