def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    stacks = [[]]
    commands = []

    # converting rows to columns
    for line in data:
        if line == "":
            break
        simplified_line = line.replace("    ", "[*] ").replace(" ", "").replace("[", "").replace("]", "")
        index = 0
        for symbol in simplified_line:
            if len(stacks) <= index:
                stacks.append([])
            if symbol != "*":
                stacks[index].insert(0, symbol)
            index = index + 1

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


file_name = "Day05-input-p.txt"
part_one = run_crate_mover(file_name, 9000)
part_two = run_crate_mover(file_name, 9001)

print("----------------------------")
print("Part One:", part_one)
print("Part Two:", part_two)

# Answers:
# Part One: RFFFWBPNS
# Part Two: CQQBBJFCS
