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


# GPT


def simplify_list(lst):
    """
    Takes a list of lists of integers and returns a list of integers formed by
    concatenating the integers in each list in the order they appear.
    """
    if not lst:
        return []
    elif isinstance(lst, int):
        return [lst]
    elif all(isinstance(elem, int) for elem in lst):
        return [''.join(map(str, lst))]
    else:
        return [elem for sublist in lst for elem in simplify_list(sublist)]


def compare_sublists(L, R):
    """
    Compares the number of sublists in L and R. Returns True if L has fewer or
    equal number of sublists than R, and False otherwise.
    """
    if count_sublists(L) <= count_sublists(R):
        return True
    else:
        return False


def count_sublists(lst):
    """
    Counts the number of sublists in lst, including empty sublists.
    """
    count = 0
    for elem in lst:
        if isinstance(elem, list):
            count += 1
            count += count_sublists(elem)
    return count


def pad_strings(L, R):
    diff = len(L) - len(R)
    if diff > 0:
        R += '0' * diff
    elif diff < 0:
        L += '0' * abs(diff)
    return L, R


def compare_strings(listL, listR):
    # Pad L and R with leading zeroes to equal length
    L, R = pad_strings(str(listL), str(listR))
    list_len = len(L)
    # Compare the characters in L and R
    for i in range(list_len):
        if ord(L[i]) > ord(R[i]):
            return "False"
        if ord(L[i]) < ord(R[i]):
            return "True"

    if ord(L[list_len - 1]) == ord(R[list_len - 1]):
        return "?"


def compare_lists(L, R):
    """
    Recursively compares two lists L and R element-wise, including nested sublists.
    Returns True if the lists are equal, and False otherwise.
    """
    if compare_sublists(L, R) == False:
        return False

    for i in range(len(L)):
        if isinstance(L[i], list) and isinstance(R[i], list):
            if not compare_lists(L[i], R[i]):
                return False
        else:
            res = compare_strings(L[i], R[i])
            if res == "False":
                return False
            if res == "True":
                return True

    return True


def main():
    print("Hello - Day 13")
    file_name = "Day13-Input-d.txt"
    pairs = parse_file(file_name)

    L = [1]

    compare_strings('1234', '1234')

    for p in pairs:
        list_l = eval(p[0])
        list_r = eval(p[1])
        simple_list_left = simplify_list(list_l)
        simple_list_right = simplify_list(list_r)
        print(list_l, " - ", simple_list_left)
        print(list_r, " - ", simple_list_right)

        res = compare_lists(simple_list_left, simple_list_right)
        print(res)
        print()


def main_old():
    file_name = "Day13-Input-d.txt"
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

        # print(pair[0])
        # print(pair[1])
        res, str_l_p, str_r_p = compare_pairs(pair[0], pair[1])
        # print(res)

        if res:
            part_one += pair_index
            print("Pair : ", pair_index)
            print(str_l_p)
            print(str_r_p)
            print(" ")

        pair_index += 1
        # print(" ")

    part_two = 1

    print("----------------------------")
    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One:
# Part Two:
