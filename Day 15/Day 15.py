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
    # s_x = crd[0]
    # s_y = crd[1]
    # b_x = crd[2]
    # b_y = crd[3]

    # len_b = 2 * abs(s_x - b_x) + 1
    # len_s = len_b + 2 * abs(s_y - b_y)
    # len_r = len_s - 2 * abs(s_y - r_y)
    # start_s_x = s_x - (len_s - 1) // 2
    # end_s_x = s_x + (len_s - 1) // 2
    # start_r_x = start_s_x + abs(len_s - len_r) // 2
    # end_r_x = end_s_x - abs(len_s - len_b) // 2

    s_x = 0
    s_y = 0
    b_x = abs(crd[2] - crd[0])
    b_y = abs(crd[3] - crd[1])
    r_y = abs(r_y - crd[1])

    end_r_x = b_x + (b_y - r_y)
    start_r_x = -end_r_x

    if end_r_x < start_r_x:
        return None

    return [start_r_x +  crd[0], end_r_x +  crd[0]]


def is_overlapped(A, B):
    # checking if a range A is overlapped with sector B
    # [-3,5] and [0,3] = yes
    # [-3,5] and [3,13] = yes
    # [-3,5] and [7,13] = no

    if A[0] <= B[0] and A[1] >= B[0]:
        return True

    if B[0] <= A[0] and B[1] >= A[0]:
        return True


def get_unique_covered_positions(coverage_line, result=0):
    result = 0

    for i in range(0, len(coverage_line) - 1):
        if is_overlapped(coverage_line[i], coverage_line[i + 1]):
            coverage_line[i + 1][0] = min(coverage_line[i][0], coverage_line[i + 1][0])
            coverage_line[i + 1][1] = max(coverage_line[i][1], coverage_line[i + 1][1])
            coverage_line.remove(coverage_line[i])
            break
        else:
            result = abs(coverage_line[0][0] - coverage_line[0][1])
            coverage_line.remove(coverage_line[i])
            break

    if len(coverage_line) > 1:
        result = get_unique_covered_positions(coverage_line, result)

    return abs(coverage_line[0][0] - coverage_line[0][1])


def get_whole_range(coverage_line):
    start = coverage_line[0][0]
    end =  coverage_line[0][1]

    for a in coverage_line:
        if a[1] > end:
            end = a[1]

    return end - start

def main():
    file_name = "Day15-Input-d.txt"
    data_input = parse_file(file_name)

    coverage_line = []

    line_number = 2000000
    line_number = 10

    for crd in data_input:
        a = get_start_end(crd, line_number)
        # print(crd)
        print(crd, a)
        if a is not None:
            coverage_line.append(a)


    coverage_line.sort()

    part_two = get_whole_range(coverage_line)
    part_one = get_unique_covered_positions(coverage_line) # 4,757,854


    print("----------------------------")
    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One: 5144286
# Part Two:
