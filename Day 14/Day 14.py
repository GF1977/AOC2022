class Map:
    def __init__(self, max_x, max_y, min_x, min_y):
        self.max_x = max_x
        self.max_y = max_y
        self.min_x = min_x
        self.min_y = min_y
        self.map = []
        self.sand_units = 0

    def draw_line(self, a, b):
        x_a = int(a[0])
        y_a = int(a[1])
        x_b = int(b[0])
        y_b = int(b[1])

        if x_a == x_b:
            for y in range(min(y_a, y_b), max(y_a, y_b) + 1):
                self.map[y][x_a] = "#"

        if y_a == y_b:
            for x in range(min(x_a, x_b), max(x_a, x_b) + 1):
                self.map[y_a][x] = "#"

        return self.map

    def draw_the_map(self):
        for y in range(0, self.max_y + 1):
            row = ""
            for x in range(self.min_x - 1, self.max_x + 1):
                row += self.map[y][x]
            print(row)
        print(" ")

    def sand_flow(self):
        res = 0
        while True:
            sand_crd = [0, 500]
            y = sand_crd[0]
            x = sand_crd[1]
            res = self.roll_sand_block(y, x)

            if res:
                break


        return self.sand_units

    def roll_sand_block(self, y,x):
        if self.sand_units % 10 == 0:
            self.draw_the_map()
        #print("X = ", x, "  Y = ", y)
        if x <= self.min_x:
            return True

        repeat = True
        while repeat:

            #check below
            if self.map[y+1][x] == ".":
                self.roll_sand_block(y + 1,x)

            # check left
            if  self.map[y + 1][x - 1] == ".":
                if self.roll_sand_block(y + 1,x - 1):
                    return True

            # check right
            elif self.map[y + 1][x + 1] == ".":
                if self.roll_sand_block(y + 1, x + 1):
                    return True

            else:
                self.map[y][x] = "o"
                self.sand_units+=1
                repeat = False

        return False

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

    the_map = Map(max_x, max_y, min_x, min_y)

    the_map.map = []
    for r in range(0, max_y + 1):
        tmp = []
        the_map.map.append(tmp)
        for c in range(0, max_x + 1):
            the_map.map[r].append(".")

    for line in data:
        crd = line.split(" -> ")
        for i in range(0, len(crd) - 1):
            xy_str_a = crd[i]
            xy_str_b = crd[i + 1]
            the_map.map = the_map.draw_line(xy_str_a.split(","), xy_str_b.split(","))

    the_map.map[0][500] = "+"

    the_map.draw_the_map()

    return the_map


def main():
    file_name = "Day14-Input-d.txt"
    the_map = parse_file(file_name)

    part_one = the_map.sand_flow()

    part_two = 1

    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One:
# Part Two:
