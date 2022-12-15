class Map:
    def __init__(self, max_x, max_y, min_x, min_y):
        self.max_x = max_x
        self.max_y = max_y
        self.min_x = min_x
        self.min_y = min_y
        self.map = []
        self.sand_units = 0
        self.part_one = 0

    # placing the rocks as line from a to b
    def put_rocks_on_map(self, a, b):
        x_a, y_a = int(a[0]), int(a[1])
        x_b, y_b = int(b[0]), int(b[1])

        for y in range(min(y_a, y_b), max(y_a, y_b) + 1):
            for x in range(min(x_a, x_b), max(x_a, x_b) + 1):
                self.map[y][x] = "#"
        return self.map

    def sand_flow(self):
        while True:
            sand_crd_xy = [0, 500]
            # checking is there free space for sand right at the source "+"
            if self.map[0][500] != ".":
                break  # nope
            self.fall_sand_block(sand_crd_xy[0], sand_crd_xy[1])  # yes
        return self.part_one, self.sand_units

    def fall_sand_block(self, y, x):
        while True:
            # checking if sand starts falling into the void (first part of the puzzle)
            if x <= self.min_x and self.part_one == 0:
                self.part_one = self.sand_units

            # check below
            if self.map[y + 1][x] == ".":
                y = y + 1
                continue

            # check left
            if self.map[y + 1][x - 1] == ".":
                y = y + 1
                x = x - 1
                continue

            # check right
            if self.map[y + 1][x + 1] == ".":
                y = y + 1
                x = x + 1
                continue

            break

        self.map[y][x] = "o"
        self.sand_units += 1
        return False


def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    min_x = 99999
    min_y = 99999
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

    the_map = Map(max_x, max_y, min_x, min_y)

    the_map.map = []
    for r in range(0, max_y + 3):
        tmp = []
        the_map.map.append(tmp)
        # floor
        if r == max_y + 2:
            for c in range(0, max_x + 500):
                the_map.map[r].append("#")
        else:
            for c in range(0, max_x + 500):
                the_map.map[r].append(".")

    for line in data:
        crd = line.split(" -> ")
        for i in range(0, len(crd) - 1):
            xy_str_a = crd[i]
            xy_str_b = crd[i + 1]
            the_map.map = the_map.put_rocks_on_map(xy_str_a.split(","), xy_str_b.split(","))

    return the_map


def main():
    file_name = "Day14-Input-p.txt"
    the_map = parse_file(file_name)

    part_one, part_two = the_map.sand_flow()

    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One: 1298
# Part Two: 25585
