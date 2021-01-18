# --- Day 14: Docking Data ---
# As your ferry approaches the sea port, the captain asks for your help again. The computer system that runs this port isn't compatible with the docking program on the ferry, so the docking parameters aren't being correctly initialized in the docking program's memory.
#
# After a brief inspection, you discover that the sea port's computer system uses a strange bitmask system in its initialization program. Although you don't have the correct decoder chip handy, you can emulate it in software!
#
# The initialization program (your puzzle input) can either update the bitmask or write a value to memory. Values and memory addresses are both 36-bit unsigned integers. For example, ignoring bitmasks for a moment, a line like mem[8] = 11 would write the value 11 to memory address 8.
#
# The bitmask is always given as a string of 36 bits, written with the most significant bit (representing 2^35) on the left and the least significant bit (2^0, that is, the 1s bit) on the right. The current bitmask is applied to values immediately before they are written to memory: a 0 or 1 overwrites the corresponding bit in the value, while an X leaves the bit in the value unchanged.
#
# For example, consider the following program:
#
# mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# mem[8] = 11
# mem[7] = 101
# mem[8] = 0
# This program starts by specifying a bitmask (mask = ....). The mask it specifies will overwrite two bits in every written value: the 2s bit is overwritten with 0, and the 64s bit is overwritten with 1.
#
# The program then attempts to write the value 11 to memory address 8. By expanding everything out to individual bits, the mask is applied as follows:
#
# value:  000000000000000000000000000000001011  (decimal 11)
# mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# result: 000000000000000000000000000001001001  (decimal 73)
# So, because of the mask, the value 73 is written to memory address 8 instead. Then, the program tries to write 101 to address 7:
#
# value:  000000000000000000000000000001100101  (decimal 101)
# mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# result: 000000000000000000000000000001100101  (decimal 101)
# This time, the mask has no effect, as the bits it overwrote were already the values the mask tried to set. Finally, the program tries to write 0 to address 8:
#
# value:  000000000000000000000000000000000000  (decimal 0)
# mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# result: 000000000000000000000000000001000000  (decimal 64)
# 64 is written to address 8 instead, overwriting the value that was there previously.
#
# To initialize your ferry's docking program, you need the sum of all values left in memory after the initialization program completes. (The entire 36-bit address space begins initialized to the value 0 at every address.) In the above example, only two values in memory are not zero - 101 (at address 7) and 64 (at address 8) - producing a sum of 165.
#
# Execute the initialization program. What is the sum of all values left in memory after it completes? (Do not truncate the sum to 36 bits.)
#
# Your puzzle answer was 7611244640053.
#
# --- Part Two ---
# For some reason, the sea port's computer system still can't communicate with your ferry's docking program. It must be using version 2 of the decoder chip!
#
# A version 2 decoder chip doesn't modify the values being written at all. Instead, it acts as a memory address decoder. Immediately before a value is written to memory, each bit in the bitmask modifies the corresponding bit of the destination memory address in the following way:
#
# If the bitmask bit is 0, the corresponding memory address bit is unchanged.
# If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
# If the bitmask bit is X, the corresponding memory address bit is floating.
# A floating bit is not connected to anything and instead fluctuates unpredictably. In practice, this means the floating bits will take on all possible values, potentially causing many memory addresses to be written all at once!
#
# For example, consider the following program:
#
# mask = 000000000000000000000000000000X1001X
# mem[42] = 100
# mask = 00000000000000000000000000000000X0XX
# mem[26] = 1
# When this program goes to write to memory address 42, it first applies the bitmask:
#
# address: 000000000000000000000000000000101010  (decimal 42)
# mask:    000000000000000000000000000000X1001X
# result:  000000000000000000000000000000X1101X
# After applying the mask, four bits are overwritten, three of which are different, and two of which are floating. Floating bits take on every possible combination of values; with two floating bits, four actual memory addresses are written:
#
# 000000000000000000000000000000011010  (decimal 26)
# 000000000000000000000000000000011011  (decimal 27)
# 000000000000000000000000000000111010  (decimal 58)
# 000000000000000000000000000000111011  (decimal 59)
# Next, the program is about to write to memory address 26 with a different bitmask:
#
# address: 000000000000000000000000000000011010  (decimal 26)
# mask:    00000000000000000000000000000000X0XX
# result:  00000000000000000000000000000001X0XX
# This results in an address with three floating bits, causing writes to eight memory addresses:
#
# 000000000000000000000000000000010000  (decimal 16)
# 000000000000000000000000000000010001  (decimal 17)
# 000000000000000000000000000000010010  (decimal 18)
# 000000000000000000000000000000010011  (decimal 19)
# 000000000000000000000000000000011000  (decimal 24)
# 000000000000000000000000000000011001  (decimal 25)
# 000000000000000000000000000000011010  (decimal 26)
# 000000000000000000000000000000011011  (decimal 27)
# The entire 36-bit address space still begins initialized to the value 0 at every address, and you still need the sum of all values left in memory at the end of the program. In this example, the sum is 208.
#
# Execute the initialization program using an emulator for a version 2 decoder chip. What is the sum of all values left in memory after it completes?
#
# Your puzzle answer was 3705162613854.
#
# Both parts of this puzzle are complete! They provide two gold stars: **


import itertools
import re


def generate_result_set(bin_string):
    x_count = bin_string.count('X')
    expected_len_results = pow(2, x_count)
    results = set()
    index = 0
    index_list = []

    while True:
        index = bin_string.find('X', index)
        if index == -1:
            break
        index_list.append(index)
        index += 1

    #print("index_list: ", index_list)

    if x_count != len(index_list):
        print("ERROR: Not all expected 'X' occurrences ({}) are in index_list ({})".format(x_count, len(index_list)))

    all_comb = list(map(list, itertools.product([0, 1], repeat=x_count)))
    #print("all_comb: ", all_comb)
    #print("len(all_comb): ", len(all_comb))

    for comb in all_comb:
        result = bin_string
        iteration = 0
        for i in index_list:
            result = result[:i] + str(comb[iteration]) + result[i + 1:]
            iteration += 1
        #print("result: ", result)
        results.add(result)

    if expected_len_results != len(results):
       print("ERROR: Expected results ({}) does not match number of items in set ({})".format(expected_len_results, len(results)))

    return results


if __name__ == '__main__':

    files = ['20201214-example_p1.txt', '20201214-example_p2.txt', '20201214-input.txt']

    for file_name in files:
        print("\n****************************\n" + file_name)
        with open(file_name) as f:
            lines = f.readlines()

        len_lines = len(lines)
        #print("len_lines: ", len_lines)

        mem_regex = '(^mem\[)([0-9]*)(\].*\=)(.*$)'

        programs = []

        for idx in range(len_lines):

            dict_mask = {}

            if lines[idx].startswith('mask'):
                mask = lines[idx].split('=')[1].strip()
                #print('mask: ', mask)

            elif lines[idx].startswith('mem'):
                match = re.match(mem_regex, lines[idx])
                #print("match: ", match)
                if match:
                    mem_pos = match[2]
                    #print("mem_pos: ", int(mem_pos))
                    value_dec = int(match[4])
                    #print("value_dec: ", value_dec)
                    value_bin = bin(value_dec)
                    #print("value_bin: ", value_bin)
                    value_bin_str = f'{value_dec:036b}'
                    #print("value_bin_str: ", value_bin_str)
                    dict_mask['mem_pos'] = mem_pos
                    dict_mask['value_dec'] = value_dec
                    dict_mask['value_bin'] = value_bin
                    dict_mask['value_bin_str'] = value_bin_str
                    dict_mask['mask'] = mask
                    programs.append(dict_mask)

        #print("programs: ")
        #print("\n".join(str(j) for j in programs))

        if file_name.find('p2') < 0:
            print("\nPart One")

            part_one = []

            for p in programs:
                m = p.get('mask')
                v = p.get('value_bin_str')
                m_pos = p.get('mem_pos')
                b_pos = 0
                rbs = ''
                for b in m:
                    if b == 'X':
                        rbs += v[b_pos]
                    elif b == '1':
                        rbs += '1'
                    elif b == '0':
                        rbs += '0'
                    b_pos += 1
                rd = int(rbs, 2)

                part_one.append(p)

                if len(part_one) > 0:
                    overwrite_p_idx_list = [p_idx for p_idx in range(len(part_one)) if part_one[p_idx].get('mem_pos') == m_pos]
                    if len(overwrite_p_idx_list) > 1:
                        overwrite_p_idx = overwrite_p_idx_list[0]
                        part_one.pop() # Removes last list item
                        index = overwrite_p_idx
                        #print(overwrite_p_idx)
                    else:
                        index = -1

                #print(index)

                part_one[index]['result_bin_str'] = rbs
                part_one[index]['result_dec'] = rd

            #print("part_one: ")
            #print("\n".join(str(j) for j in part_one))

            print("Sum: ", sum(p.get('result_dec') for p in part_one))

        if file_name.find('p1') < 0:
            print("\nPart Two")

            part_two = {}

            for p in programs:
                m = p.get('mask')
                m_pos = p.get('mem_pos')
                v_d = p.get('value_dec')

                process_p = True
                if len(part_two) > 0:
                    if m_pos in part_two.keys():
                        v = next((k for k, v in part_two if k == m_pos), None)
                        process_p = False

                if process_p:
                    v = f'{int(m_pos):036b}'

                #print("v: ", v)
                b_pos = 0
                rbs = ''
                for b in m:
                    if b == 'X':
                        rbs += 'X'
                    elif b == '1':
                        rbs += '1'
                    elif b == '0':
                        rbs += v[b_pos]
                    b_pos += 1

                #print("rbs: ", rbs)
                rbs_comb = generate_result_set(rbs)
                #print("rbs_comb: ")
                #print("\n".join(j for j in rbs_comb))

                for rbs_i in rbs_comb:
                    rd_i = int(rbs_i, 2)
                    #print("rd_i: ", rd_i)
                    part_two[rd_i] = v_d

            #print("part_two: ", part_two)
            #print("part_two: ")
            #print("\n".join(str(j) for j in part_two.items()))

            print("Sum: ", sum(part_two.values()))
