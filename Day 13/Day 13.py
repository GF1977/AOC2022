# The whole idea is to convert the signal to "INT" and compare them


def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    list_of_pairs = []
    pair = []
    for line in data:
        if line == "":
            list_of_pairs.append(pair)
            pair = []
            continue
        pair.append(line)

    list_of_pairs.append(pair)
    return list_of_pairs


def get_value_between(line):
    res = ""
    capturing = False
    for symbol in line:
        if symbol == "[":
            capturing = True
            res = ""
        if capturing:
            res += symbol
        if symbol == "]":
            break
    return res


def calculate_value(value):
    value = value[1:-1]
    if len(value) == 0:
        return "0"

    data = value.split(",")
    res = ""

    for item in data:
        res = res + item

    return res


def compare_pairs(l_p, r_p):
    res = True
    str_l_p = str(l_p)
    str_r_p = str(r_p)
    zero_padding = '0' * abs(len(str_r_p) - len(str_l_p))
    if len(str_l_p) < len(str_r_p):
        str_l_p += zero_padding
    else:
        str_r_p += zero_padding

    if int(str_l_p) <= int(str_r_p):
        return True, str_l_p, str_r_p
    else:
        return False, str_l_p, str_r_p


def main():
    file_name = "Day13-Input-p.txt"
    pairs = parse_file(file_name)

    pair_index = 1
    part_one = 0
    str_l_p, str_r_p = "", ""

    for pair in pairs:
        count = 0
        while "[" in pair[0] or "[" in pair[1]:
            left_pair = get_value_between(pair[0])

            right_pair = get_value_between(pair[1])

            l_p = calculate_value(left_pair)
            if l_p == 0:
                l_p = pair[0]

            r_p = calculate_value(right_pair)
            if r_p == 0:
                r_p = pair[1]

            if left_pair != "":
                pair[0] = pair[0].replace(left_pair, str(l_p))

            if right_pair != "":
                pair[1] = pair[1].replace(right_pair, str(r_p))

            count += 1
            if pair[0] == "0":
                pair[0] = "1" + "1" * count

            if pair[1] == "0":
                pair[1] = "1" + "1" * count


        #print(pair[0])
        #print(pair[1])
        res, str_l_p, str_r_p = compare_pairs(pair[0], pair[1])
        #print(res)

        if res:
            part_one += pair_index
            print("Pair : ", pair_index)
            print(str_l_p)
            print(str_r_p)
            print(" ")

        pair_index += 1
        #print(" ")


    part_two = 1


    print("----------------------------")
    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One:
# Part Two: