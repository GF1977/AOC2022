import itertools


class Sector:
    id_iter = itertools.count()

    def __init__(self, value, neighbours):
        self.id = Sector.id_iter.__next__() + 1
        self.value = value
        self.neighbours = neighbours
        self.visited = False


def get_neighbours_ids(sector_id, x, y):
    candidates = [sector_id - 1, sector_id + 1, sector_id - x, sector_id + x]

    if sector_id % x == 1:  # left edge
        candidates.remove(sector_id - 1)

    if sector_id % x == 0:  # right edge
        candidates.remove(sector_id + 1)

    res = list(filter(lambda l: 0 < l <= x * y, candidates))  # removing the candidates which are out of the map
    return res


def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    the_map = {}

    for line in data:
        for letter in line:
            value = ord(letter) - 96  # a = 1; z = 26
            if letter == "S":
                value = 0
            if letter == "E":
                value = 27  # the task is solved when we step into 27 only

            sector = Sector(value, [])
            sector.neighbours = get_neighbours_ids(sector.id, x=len(data[0]), y=len(data))
            the_map[sector.id] = sector

    return the_map


def get_my_path(the_map, candidates_id, count=0):
    count = count + 1
    res = []
    for sector_id in candidates_id:
        sector = the_map[sector_id]
        if not sector.visited:
            for destination_id in sector.neighbours:
                if sector.value >= the_map[destination_id].value or sector.value == the_map[destination_id].value - 1:
                    if the_map[destination_id].value == 27:
                        return count
                    if destination_id not in res:
                        res.append(destination_id)
            sector.visited = True

    return get_my_path(the_map, res, count)


def main():
    file_name = "Day12-input-p.txt"
    the_map = parse_file(file_name)

    res = list(filter(lambda l: the_map[l].value == 0, the_map))  # adding 'E' as starting points
    part_one = get_my_path(the_map, res)

    for sector_id in the_map:
        the_map[sector_id].visited = False

    res = list(filter(lambda l: the_map[l].value <= 1, the_map))  # adding 'E' and all 'a' as starting points
    part_two = get_my_path(the_map, res)

    print("----------------------------")
    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One: 383
# Part Two: 377
