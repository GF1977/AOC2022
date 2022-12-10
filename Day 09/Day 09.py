import math


def get_step(a, b):
    if a == b:
        return 0
    else:
        return math.copysign(1, (a - b))


class Rope:
    def __init__(self):
        self.head_x, self.head_y, self.tail_x, self.tail_y = 0, 0, 0, 0
        self.where_tail_was = {}

    def move_head(self, step_x, step_y):
        self.head_x += step_x
        self.head_y += step_y

    def move_tail(self):
        # move only the head and tail are disconnected
        if not (abs(self.head_x - self.tail_x) <= 1 and abs(self.head_y - self.tail_y) <= 1):
            self.tail_x += get_step(self.head_x, self.tail_x)
            self.tail_y += get_step(self.head_y, self.tail_y)
            # memorize position
            position = str(self.tail_x) + ":" + str(self.tail_y)
            self.where_tail_was[position] = 0

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
        first_knot = ropes[0]
        first_knot.move_head(step_x, step_y)
        first_knot.move_tail()

        # this does work for 2nd part only, when number of knots > 1
        for i in range(1, len(ropes)):
            ropes[i].head_x = ropes[i - 1].tail_x
            ropes[i].head_y = ropes[i - 1].tail_y
            ropes[i].move_tail()

    return ropes


def main():
    file_name = "Day09-input-p.txt"
    data_input = parse_file(file_name)

    ropes = []
    for i in range(0, 9):
        ropes.append(Rope())

    for command in data_input:
        ropes = emulate_rope_motion(command.split(" "), ropes)

    print("----------------------------")
    print("Part One:", ropes[0].get_visited_positions())
    print("Part Two:", ropes[8].get_visited_positions())


if __name__ == "__main__":
    main()

# Answers:
# Part One: 6384
# Part Two: 2734