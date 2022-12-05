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

    stakcs_adjusted_by_width = []
    for stack in stacks:
        a = len(max(stacks)) - len(stack)
        stakcs_adjusted_by_width.append(stack + "*"*a)

    # rotate the array to get each stack in individual list
    tmp = list(zip(*stakcs_adjusted_by_width.__reversed__()))
    stacks = []
    for line in tmp:
        line = list(line)
        #if "*" in line:
        while line.__contains__("*"):
            line.remove("*")
        stacks.append(line)

    for line in file_to_process:
        if "move" in line:
            quantity = line.split(" from ")[0].split(" ")[1]
            move_from = line.split(" to ")[0][-1:]
            move_to = line.split(" to ")[1][0]
            command = [int(quantity), int(move_from), int(move_to)]
            #print(command)
            commands.append(command)

    return stacks, commands


stacks, commands = parse_file(data)
for command in commands:
    #print(stacks)
    move_from = command[1] - 1
    move_to = command[2] - 1
    for repeats in range(0,command[0]):
        crane_picks = stacks[move_from].pop()
        stacks[move_to].append(crane_picks)

part_one = ""
for stack in stacks:
    part_one = part_one + stack[-1]

print("----------------------------")
print("Part One:", part_one)
print("Part Two:", 1)

# Answers:
# Part one: 494
# Part one: 833
