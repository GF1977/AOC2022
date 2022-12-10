from typing import List


class Rope:
    def __init__(self):
        self.head_x, self.head_y, self.tail_x, self.tail_y = 0, 0, 0, 0
        self.prev_pos_head_x, self.prev_pos_head_y = 0, 0
        self.where_tail_was = {}

    def tail_near_head(self):
        return abs(self.head_x - self.tail_x) <= 1 and abs(self.head_y - self.tail_y) <= 1

    def memorize_tail_position(self):
        position = str(self.tail_x) + ":" + str(self.tail_y)
        self.where_tail_was[position] = 0

    def move_head(self, step_x, step_y):
        self.prev_pos_head_x = self.head_x
        self.prev_pos_head_y = self.head_y
        self.head_x += step_x
        self.head_y += step_y

    def move_tail(self):
        # s_x = self.prev_pos_head_x - self.tail_x
        # s_y = self.prev_pos_head_y - self.tail_y
        #
        # self.tail_x = self.prev_pos_head_x
        # self.tail_y = self.prev_pos_head_y

        if self.head_x > self.tail_x:
            s_x = 1
        else:
            s_x = -1

        if self.head_x == self.tail_x:
            s_x = 0


        if self.head_y > self.tail_y:
            s_y = 1
        else:
            s_y = -1

        if self.head_y == self.tail_y:
            s_y = 0

        self.tail_x += s_x
        self.tail_y += s_y
        #return s_x, s_y

    def get_visited_positions(self):
        return len(self.where_tail_was)


def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    return data


def emulate_rope_motion(command, ropes):
    direction = command[0]
    distance = int(command[1])
    step_x, step_y = 0, 0

    if direction == "R":
        step_x = +1
    if direction == "L":
        step_x = -1
    if direction == "U":
        step_y = +1
    if direction == "D":
        step_y = -1

    for step in range(0, distance):
        main_head = ropes[0]
        main_head.move_head(step_x, step_y)
        if not main_head.tail_near_head():
            main_head.move_tail()
        main_head.memorize_tail_position()

        for i in range(1, len(ropes)):
            ropes[i].head_x = ropes[i - 1].tail_x
            ropes[i].head_y = ropes[i - 1].tail_y

            if not ropes[i].tail_near_head():
                ropes[i].move_tail()
            ropes[i].memorize_tail_position()
    return ropes


def show_me(wts):
    grid_size = 28

    res = []
    for x in range(0, grid_size - 6):
        line = []
        for y in range(0, grid_size):
            line.append(".")
        res.append(line)

    for a in wts:
        x, y = a.split(":")
        res[15 - int(y)][15 - int(x)] = "#"

    for l in res:
        s = ""
        for a in l:
            s = a + s
        print(s)


def main():
    file_name = "Day09-input-p.txt"
    data_input = parse_file(file_name)
    part_two = 1

    ropes = []

    for i in range(0, 9):
        ropes.append(Rope())

    for command in data_input:
        ropes = emulate_rope_motion(command.split(" "), ropes)

    part_one = ropes[0].get_visited_positions()
    part_two = ropes[8].get_visited_positions()

    print("----------------------------")
    print("Part One:", part_one)
    print("Part Two:", part_two)

    #show_me(ropes[0].where_tail_was)


if __name__ == "__main__":
    main()

# Answers:
# Part One: 6384
# Part Two:
