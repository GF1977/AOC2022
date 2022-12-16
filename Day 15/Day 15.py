def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    coordinates = []
    for line in data:
        tmp = line.split(": ")
        s_x = int(tmp[0].split(", ")[0].split("=")[1])
        s_y = int(tmp[0].split(", ")[1].split("=")[1])
        b_x = int(tmp[1].split(", ")[0].split("=")[1])
        b_y = int(tmp[1].split(", ")[1].split("=")[1])
        coordinates.append([s_x, s_y, b_x, b_y])

    return coordinates


def get_start_end(crd, r_y):
    s_x = crd[0]
    s_y = crd[1]
    b_x = crd[2]
    b_y = crd[3]

    len_b = 2 * abs(s_x - b_x)  + 1
    len_s = len_b + 2 * abs(s_y - b_y)
    len_r = len_s - 2 * (s_y - r_y)
    start_s_x = s_x - (len_s - 1)//2
    end_s_x = s_x + (len_s - 1) //2
    start_r_x = start_s_x + (len_s - len_r)//2
    end_r_x = end_s_x - (len_s - len_b)//2

    return [start_r_x, end_r_x]


def main():
    file_name = "Day15-Input-d.txt"
    data_input = parse_file(file_name)

    for crd in data_input:
        a = get_start_end(crd, 10)
        #print(crd)
        print(a)
        print(" ")

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