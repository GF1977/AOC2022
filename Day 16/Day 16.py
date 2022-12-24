def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    for line in data:
        tmp = line.split("; ")
        valve = tmp[0].split(" ")[1]
        flow_rate = tmp[0].split("=")[1]
        tmp_lead_to = tmp[1].split(" ")
        lead_to = []
        for i in range(4, len(tmp_lead_to)):
            lead_to.append(tmp_lead_to[i])


    return data


def main():
    file_name = "Day16-Input-d.txt"
    data_input = parse_file(file_name)
    part_one = 0
    part_two = 1

    print("----------------------------")
    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One:
# Part Two: