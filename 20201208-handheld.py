# --- Day 8: Handheld Halting ---
# Your flight to the major airline hub reaches cruising altitude without incident. While you consider checking the in-flight menu for one of those drinks that come with a little umbrella, you are interrupted by the kid sitting next to you.
#
# Their handheld game console won't turn on! They ask if you can take a look.
#
# You narrow the problem down to a strange infinite loop in the boot code (your puzzle input) of the device. You should be able to fix it, but first you need to be able to run the code in isolation.
#
# The boot code is represented as a text file with one instruction per line of text. Each instruction consists of an operation (acc, jmp, or nop) and an argument (a signed number like +4 or -20).
#
# acc increases or decreases a single global value called the accumulator by the value given in the argument. For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction, the instruction immediately below it is executed next.
# jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue to the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.
# nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.
# For example, consider the following program:
#
# nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6
# These instructions are visited in this order:
#
# nop +0  | 1
# acc +1  | 2, 8(!)
# jmp +4  | 3
# acc +3  | 6
# jmp -3  | 7
# acc -99 |
# acc +1  | 4
# jmp -4  | 5
# acc +6  |
# First, the nop +0 does nothing. Then, the accumulator is increased from 0 to 1 (acc +1) and jmp +4 sets the next instruction to the other acc +1 near the bottom. After it increases the accumulator from 1 to 2, jmp -4 executes, setting the next instruction to the only acc +3. It sets the accumulator to 5, and jmp -3 causes the program to continue back at the first acc +1.
#
# This is an infinite loop: with this sequence of jumps, the program will run forever. The moment the program tries to run any instruction a second time, you know it will never terminate.
#
# Immediately before the program would run an instruction a second time, the value in the accumulator is 5.
#
# Run your copy of the boot code. Immediately before any instruction is executed a second time, what value is in the accumulator?
#
# Your puzzle answer was 1941.
#
# --- Part Two ---
# After some careful analysis, you believe that exactly one instruction is corrupted.
#
# Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp. (No acc instructions were harmed in the corruption of this boot code.)
#
# The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in the file. By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.
#
# For example, consider the same program from above:
#
# nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6
# If you change the first instruction from nop +0 to jmp +0, it would create a single-instruction infinite loop, never leaving that instruction. If you change almost any of the jmp instructions, the program will still eventually find another jmp instruction and loop forever.
#
# However, if you change the second-to-last instruction (from jmp -4 to nop -4), the program terminates! The instructions are visited in this order:
#
# nop +0  | 1
# acc +1  | 2
# jmp +4  | 3
# acc +3  |
# jmp -3  |
# acc -99 |
# acc +1  | 4
# nop -4  | 5
# acc +6  | 6
# After the last instruction (acc +6), the program terminates by attempting to run the instruction below the last instruction in the file. With this change, after the program terminates, the accumulator contains the value 8 (acc +1, acc +1, acc +6).
#
# Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator after the program terminates?
#
# Your puzzle answer was 2096.
#
# Both parts of this puzzle are complete! They provide two gold stars: **


import copy


def process_instructions(pos):
    global accumulator
    global count
    global last_pos

    end = False

    if pos == len(instruction_list) -1:
        #print('List end reached')
        end = True

    count += 1

    if instruction_list[pos].get('visited', 0) == 0:
        instruction_list[pos]['visited'] = count
        last_pos = pos
    else:
        instruction_list[pos]['visited'] = count
        #print('Instruction visited the second time! ..return')
        return

    if instruction_list[pos]['op'] == 'jmp':
        new_pos = pos + instruction_list[pos]['sn']

    if instruction_list[pos]['op'] == 'acc':
        accumulator += instruction_list[pos]['sn']
        new_pos = pos + 1

    if instruction_list[pos]['op'] == 'nop':
        new_pos = pos + 1

    if not end:
        process_instructions(new_pos)


if __name__ == '__main__':

    files = ['20201208-example.txt', '20201208-input.txt']

    for file_name in files:
        print("\n****************************\n" + file_name)
        with open(file_name) as f:
            instructions = f.readlines()

        len_instructions = len(instructions)

        instruction_count = 0
        instruction_list = []

        while instruction_count < len_instructions:
            instruction_dict = {}
            #print("instructions[instruction_count]: ", instructions[instruction_count].strip())
            instruction = instructions[instruction_count].strip()
            #print("instruction: ", instruction)
            instruction_dict['pos'] = instruction_count
            instruction_dict['op'] = instruction.split()[0].strip()
            instruction_dict['sn'] = int(instruction.split()[1].strip())
            # [ { pos: 0, op: acc, sn: +1}, ... ]
            #print('instruction_dict: ', instruction_dict)
            instruction_list.append(instruction_dict)
            instruction_count += 1
        #print('instruction_list: ', instruction_list)

        # part one
        last_pos = 0
        accumulator = 0
        count = 0
        process_instructions(0)

        print("\npart one")
        #print("last_pos: ", last_pos)
        #print("instruction_list[last_pos]: ", instruction_list[last_pos])
        print("accumulator: ", accumulator)
        #print("count: ", count)

        #part two
        print("\npart two")

        #print("Create deepcopy of instruction_list")
        part_two_instruction_list = copy.deepcopy(instruction_list)

        for index in range(len(part_two_instruction_list)):

            if part_two_instruction_list[index].get('visited', 0) != 0 and part_two_instruction_list[index].get('op') == 'jmp':

                #print("Delete visited entries in original instruction_list")
                for i in instruction_list:
                    i.pop('visited', 'No key found, ignore')
                #print("Change instruction_list[index] op: jmp => nop")
                #print("Before: ", instruction_list[index])
                instruction_list[index]['op'] = 'nop'
                #print("After: ", instruction_list[index])
                last_pos = 0
                accumulator = 0
                count = 0
                process_instructions(0)
                if last_pos == len_instructions -1:
                    #print('Bug fixed')
                    break
                else:
                    #print('No match, revert change of instruction_list[index] op: nop => jmp')
                    #print("Before: ", instruction_list[index])
                    instruction_list[index]['op'] = 'jmp'
                    #print("After: ", instruction_list[index])

        #print("last_pos: ", last_pos)
        #print("instruction_list[last_pos]: ", instruction_list[last_pos])
        print("accumulator: ", accumulator)
        #print("count: ", count)
