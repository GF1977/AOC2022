class Sector:
    def __init__(self, sector_id, value, neighbours):
        self.id = sector_id
        self.value = value
        self.neighbours = neighbours
        self.visited = False


def get_neighbours_ids(sector_id, x, y):
    candidates = [sector_id - 1, sector_id + 1, sector_id - x, sector_id + x]

    if sector_id % x == 1:  # left edge
        candidates = [sector_id + 1, sector_id - x, sector_id + x]

    if sector_id % x == 0:  # right edge
        candidates = [sector_id - 1, sector_id - x, sector_id + x]

    res = list(filter(lambda l: 0 < l <= x * y, candidates))
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


def get_my_path2(map2, candidates, count):
    res = []
    for sector_id in candidates:
        sector = map2[sector_id]
        if not sector.visited:
            for maybe_go_here_id in sector.neighbours:
                if sector.value >= map2[maybe_go_here_id].value or sector.value == map2[maybe_go_here_id].value - 1:
                    if maybe_go_here_id not in res:
                        res.append(maybe_go_here_id)
                    if map2[maybe_go_here_id].value == 27:
                        return [], count
            sector.visited = True

    return res, count + 1


def main():
    file_name = "Day12-input-p.txt"

    map2, start_point_id = parse_file2(file_name)
    res = [start_point_id]
    part_one = 1
    while len(res) > 0:
        res, part_one = get_my_path2(map2, res, part_one)

    map2, start_point_id = parse_file2(file_name)
    res = list(filter(lambda l: map2[l].value <= 1, map2))

    part_two = 1
    while len(res) > 0:
        res, part_two = get_my_path2(map2, res, part_two)

    print("----------------------------")
    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One: 383
# Part Two: 377