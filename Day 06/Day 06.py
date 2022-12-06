def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    return data


def is_message_unique(msg):
    my_dict = {}
    for symbol in msg:
        if symbol not in my_dict:
            my_dict[symbol] = 0

    return len(my_dict) == len(msg)


def get_marker(msg, shift):
    index = shift
    for i in range(0, len(msg)):
        sub_message = msg[i:i + shift]
        res = is_message_unique(sub_message)
        if res:
            break
        else:
            index = index + 1

    return index


file_name = "Day06-input-p.txt"
buffer = parse_file(file_name)
for message in buffer:
    part_one = get_marker(message, 4)
    part_two = get_marker(message, 14)


print("----------------------------")
print("Part One:", part_one)
print("Part Two:", part_two)

# Answers:
# Part One: RFFFWBPNS
# Part Two: CQQBBJFCS