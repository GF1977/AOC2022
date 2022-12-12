class Sector:
    def __init__(self, sector_id, value, neighbours):
        self.id = sector_id
        self.value = value
        self.neighbours = neighbours


def get_neighbours_ids(sector_id, x, y):
    candidates = [sector_id - 1, sector_id + 1, sector_id - x, sector_id + x]

    if sector_id % x == 1:  #left edge
        candidates = [sector_id + 1, sector_id - x, sector_id + x]

    if sector_id % x == 0:  #right edge
        candidates = [sector_id - 1, sector_id - x, sector_id + x]



    res = list(filter(lambda l: l > 0 and l <= x*y, candidates))
    return res


def parse_file2(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    y = len(data)
    x = len(data[0])

    start_id = 0
    res = {}
    sector_id = 1
    for line in data:
        for letter in line:
            value = ord(letter) - 96  # a = 1; z = 26
            if letter == "S":
                value = 0
                start_id = sector_id
            if letter == "E":
                value = 27  # the task is solved when we step into 27 only

            neighbours = get_neighbours_ids(sector_id, x, y)
            sector = Sector(sector_id, value, neighbours)
            res[sector_id] = sector
            sector_id += 1
    return res, start_id


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


def get_shortest_path(the_path, the_map):
    counter = 0
    part_one = 0
    while len(the_path) > 0 and part_one == 0:
        the_new_path = get_neighbours(the_path, the_map)
        the_path = the_new_path
        for destination in the_path:
            if the_map[destination[0]][destination[1]] == 27:
                return counter + 1
        counter += 1
    return -1

def get_shortest_path2(the_path, the_map):
    counter = 0
    part_one = 0
    while len(the_path) > 0 and part_one == 0:
        the_new_path = get_neighbours(the_path, the_map)
        the_path = the_new_path
        for destination in the_path:
            if the_map[destination[0]][destination[1]] == 27:
                return counter + 1
        counter += 1
    return -1

def get_my_path2(map2, candidates, count):
    res = []
    for sector_id in candidates:
        sector = map2[sector_id]
        for maybe_go_here_id in sector.neighbours:
            if map2[maybe_go_here_id].value < 99:
                if sector.value >= map2[maybe_go_here_id].value or sector.value == map2[maybe_go_here_id].value - 1:
                    if maybe_go_here_id not in res:
                        res.append(maybe_go_here_id)
                    if map2[maybe_go_here_id].value == 27:
                        return [], count
        sector.value = 99


    return res, count + 1


def main():
    file_name = "Day12-input-d.txt"
    the_map, xy_s, xy_e = parse_file(file_name)

    map2, start_point_id = parse_file2(file_name)
    res = [start_point_id]
    count = 1
    while len(res) > 0:
        res, count = get_my_path2(map2, res, count)


    the_path = [[xy_s[1], xy_s[0]]]

    part_one = get_shortest_path(the_path, the_map)

    the_map, xy_s, xy_e = parse_file(file_name)
    the_path = []
    for x in range(0, len(the_map) - 1):
        for y in range(0, len(the_map[0]) - 1):
            if the_map[x][y] == 1:
                the_path.append([x, y])

    part_two = get_shortest_path(the_path, the_map)

    print("----------------------------")
    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One:
# Part Two:
