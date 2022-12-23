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
    b_x = abs(crd[2] - crd[0])
    b_y = abs(crd[3] - crd[1])
    r_y = abs(r_y - crd[1])

    end_r_x = b_x + (b_y - r_y)
    start_r_x = -end_r_x

    if end_r_x < start_r_x:
        return None

    return [start_r_x + crd[0], end_r_x + crd[0]]


def is_overlapped(a, b):
    # checking if a range A is overlapped with range B
    # [-3,5] and [0,3] = yes
    # [-3,5] and [3,13] = yes
    # [-3,5] and [7,13] = no

    if abs(a[0] - b[1]) == 1 or abs(a[1] - b[0]) == 1:
        return True

    if a[0] <= b[0] <= a[1] or b[0] <= a[0] <= b[1]:
        return True


def get_unique_covered_positions(coverage_line):
    result = []
    while len(coverage_line) > 1:
        if is_overlapped(coverage_line[0], coverage_line[1]):
            coverage_line[1][0] = min(coverage_line[0][0], coverage_line[1][0])
            coverage_line[1][1] = max(coverage_line[0][1], coverage_line[1][1])
        else:
            result.append(coverage_line[0])

        coverage_line.remove(coverage_line[0])

    result.append(coverage_line[0])
    return result


def get_whole_range(coverage_line):
    start = coverage_line[0][0]
    end = coverage_line[0][1]

    for a in coverage_line:
        if a[1] > end:
            end = a[1]

    return end - start


def get_coverage_line(data_input, line_number):
    coverage_line = []
    for crd in data_input:
        a = get_start_end(crd, line_number)
        if a is not None:
            coverage_line.append(a)

    coverage_line.sort()
    return coverage_line


def get_safe_positions(the_line):
    res = 0
    for segment in the_line:
        res += abs(segment[0] - segment[1])

    return res


def main():
    file_name = "Day15-Input-p.txt"
    data_input = parse_file(file_name)

    line_number = 2000000
    #line_number = 10

    coverage_line = get_coverage_line(data_input, line_number)

    res = get_unique_covered_positions(coverage_line)
    part_one = get_safe_positions(res)
    part_two = 0

    for line_number in range(3000000, 4000000):

        coverage_line = get_coverage_line(data_input, line_number)
        A = get_whole_range(coverage_line)
        res = get_unique_covered_positions(coverage_line)
        B = get_safe_positions(res)
        if A != B:
            part_two = (res[0][1] + 1) * 4000000 + line_number
            break

    print("----------------------------")
    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One: 5144286
# Part Two: 10229191267339
