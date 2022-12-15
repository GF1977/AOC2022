def draw_line(the_map, a, b):
    x_a = int(a[0])
    y_a = int(a[1])
    x_b = int(b[0])
    y_b = int(b[1])

    if x_a == x_b:
        for y in range(min(y_a, y_b), max(y_a, y_b) + 1):
            the_map[y][x_a] = "#"

    if y_a == y_b:
        for x in range(min(x_a, x_b), max(x_a, x_b) + 1):
            the_map[y_a][x] = "#"

    return the_map


def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    min_x = 999
    min_y = 999
    max_x = 0
    max_y = 0

    for line in data:
        rocks = line.split(" -> ")
        for crd in rocks:
            xy_str = crd.split(",")
            x = int(xy_str[0])
            y = int(xy_str[1])

            if x > max_x:
                max_x = x
            if x < min_x:
                min_x = x

            if y > max_y:
                max_y = y
            if y < min_y:
                min_y = y

    the_map = []
    for r in range(0, max_y + 1):
        tmp = []
        the_map.append(tmp)
        for c in range(0, max_x + 1):
            the_map[r].append(".")

    for line in data:
        crd = line.split(" -> ")
        for i in range(0, len(crd) - 1):
            xy_str_a = crd[i]
            xy_str_b = crd[i + 1]
            the_map = draw_line(the_map, xy_str_a.split(","), xy_str_b.split(","))

    the_map[0][500] = "+"

    for y in range(0, max_y + 1):
        row = ""
        for x in range(min_x - 1, max_x + 1):
            row += the_map[y][x]
        print(row)

    return the_map


def main():
    file_name = "Day14-Input-d.txt"
    data_input = parse_file(file_name)
    part_one = 0
    part_two = 1


    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One:
# Part Two:
