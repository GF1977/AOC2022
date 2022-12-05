from typing import List

file = open("Day05-input-p.txt", mode="r")
data: list[str] = file.read().split("\n")


def parse_file(file_to_process):
    index = 0
    stacks = []
    commands = []
    for line in file_to_process:
        if line == "":
            break

        simplified_line = line.replace("    ", "[*] ").replace(" ", "").replace("[", "").replace("]", "")
        stacks.append(simplified_line)

    stacks_adjusted_by_width = []
    for stack in stacks:
        a = len(max(stacks)) - len(stack)
        stacks_adjusted_by_width.append(stack + "*" * a)

    # rotate the array to get each stack in individual list
    tmp = list(zip(*stacks_adjusted_by_width.__reversed__()))
    stacks = []
    for line in tmp:
        line = list(line)
        while line.__contains__("*"):
            line.remove("*")
        stacks.append(line)

    for line in file_to_process:
        if "move" in line:
            quantity = line.split(" from ")[0].split(" ")[1]
            move_from = line.split(" to ")[0][-1:]
            move_to = line.split(" to ")[1][0]
            command = [int(quantity), int(move_from), int(move_to)]
            commands.append(command)
    return stacks, commands


stacks, commands = parse_file(data)
for command in commands:
    # print(stacks)
    move_from = command[1] - 1  # -1 is to adjust the stack number which is 1,2,3.. to arrays' identity 0,1,2,3..
    move_to = command[2] - 1
    for repeats in range(0, command[0]):
        crane_picks = stacks[move_from].pop()
        stacks[move_to].append(crane_picks)

part_one = ""
for stack in stacks:
    part_one = part_one + stack[-1]

stacks, commands = parse_file(data)
for command in commands:
    # print(stacks)
    quantity = command[0]
    move_from = command[1] - 1  # -1 is to adjust the stack number which is 1,2,3.. to arrays' identity 0,1,2,3..
    move_to = command[2] - 1

    mini_stack = []
    for repeats in range(0, command[0]):
        crane_picks = stacks[move_from].pop()
        mini_stack.append(crane_picks)

    mini_stack.reverse()
    for container in mini_stack:
        stacks[move_to].append(container)

part_two = ""
for stack in stacks:
    part_two = part_two + stack[-1]


print("----------------------------")
print("Part One:", part_one)
print("Part Two:", part_two)

# Answers:
# Part one: RFFFWBPNS
# Part one: 833
