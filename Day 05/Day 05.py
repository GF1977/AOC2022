def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    stacks = []
    commands = []
    # process first part of the file, get containers into stacks
    for line in data:
        if line == "":
            break
        # adding '*' to fill empty positions, which are _left_ from the last container
        # **A  or *******BCD, but not **A****** or ******XYZ**
        simplified_line = line.replace("    ", "[*] ").replace(" ", "").replace("[", "").replace("]", "")
        stacks.append(simplified_line)

    # here we add '*' to fill the empty positions on the right side, the len of each line will be the same
    stacks_adjusted_by_width = []
    for stack in stacks:
        a = len(max(stacks)) - len(stack)
        stacks_adjusted_by_width.append(stack + "*" * a)

    # rotate the array to get each stack as individual list
    # A B       1 A
    # 1 2       2 B
    tmp = list(zip(*stacks_adjusted_by_width.__reversed__()))
    stacks = []
    for line in tmp:
        line = list(line)
        while line.__contains__("*"):
            line.remove("*")
        stacks.append(line)

    # get commands
    for line in data:
        if "move" in line:
            quantity = line.split(" from ")[0].split(" ")[1]
            move_from = line.split(" to ")[0][-1:]
            move_to = line.split(" to ")[1][0]
            command = [int(quantity), int(move_from), int(move_to)]
            commands.append(command)

    return stacks, commands


def run_crate_mover(input_data, crane_model):
    """
    :param input_data: the data we read from input file
    :param crane_model: two options 9000 for one-by-one move, or 9001 which can moves many containers at once
    :return: answer to the puzzle -  what crate ends up on top of each stack?
    """
    stacks, crane_commands = parse_file(input_data)
    for command in crane_commands:
        quantity = command[0]
        move_from = command[1] - 1  # -1 is to adjust the stack number which is 1,2,3.. to arrays' identity 0,1,2,3..
        move_to = command[2] - 1

        mini_stack = []
        # this is not effective for big quantities, but does work for small ones
        for i in range(0, quantity):
            crane_picks = stacks[move_from].pop()
            mini_stack.append(crane_picks)

        # the whole difference between 9000 and 9001, that the mini stack is inverted in
        # case of 9001
        if crane_model == 9001:
            mini_stack.reverse()

        stacks[move_to] = stacks[move_to] + mini_stack

    answer = ""
    for stack in stacks:
        answer = answer + stack[-1]
    return answer

file_name = "Day05-input-d.txt"
part_one = run_crate_mover(file_name, 9000)
part_two = run_crate_mover(file_name, 9001)

print("----------------------------")
print("Part One:", part_one)
print("Part Two:", part_two)

# Answers:
# Part One: RFFFWBPNS
# Part Two: CQQBBJFCS