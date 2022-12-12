class Tree:
    def __init__(self, parent, value, xy):
        self.parent = parent
        self.value = value
        self.xy = xy


def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    the_map = []
    xy_s = [0, 0]
    xy_e = [0, 0]
    x, y = 0, 0
    for line in data:
        row = []
        x = 0
        for letter in line:
            value = ord(letter) - 96  # a = 1; z = 26
            if letter == "S":
                value = 0
                xy_s = [x, y]
            if letter == "E":
                value = 27  # the task is solved when we step into 27 only
                xy_e = [x, y]
            row.append(value)
            x += 1
        the_map.append(row)
        y += 1

    return the_map, xy_s, xy_e


def get_neighbours(path, the_map):
    res = []
    deltas = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    for sector in path:
        x = sector[0]
        y = sector[1]
        value = the_map[x][y]
        if value < 99:
            for d in deltas:
                n_x = x + d[0]
                n_y = y + d[1]
                if 0 <= n_x <= len(the_map) - 1 and 0 <= n_y <= len(the_map[0]) - 1:
                    if (value + 1) == the_map[n_x][n_y] or value >= the_map[n_x][n_y]:
                        res.append([n_x, n_y])
            the_map[x][y] = 99  # we checked this sector, let's exclude it from the list
    return res


def main():
    file_name = "Day12-input-p.txt"
    the_map, xy_s, xy_e = parse_file(file_name)

    the_path = [[xy_s[1], xy_s[0]]]
    counter = 0
    part_one = 0
    while len(the_path) > 0 and part_one == 0:
        the_new_path = get_neighbours(the_path, the_map)
        the_path = the_new_path
        for destination in the_path:
            if the_map[destination[0]][destination[1]] == 27:
                part_one = counter + 1
        counter += 1

    part_two = 1

    print("----------------------------")
    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One:
# Part Two:
