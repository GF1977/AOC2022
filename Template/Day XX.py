def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    return 0


file_name = "DayXX-input-p.txt"
part_one = 0
part_two = 1

print("----------------------------")
print("Part One:", part_one)
print("Part Two:", part_two)

# Answers:
# Part One: RFFFWBPNS
# Part Two: CQQBBJFCS
