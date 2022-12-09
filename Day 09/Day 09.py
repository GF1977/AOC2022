class Rope:
    def __init__(self):
        self.head_x, self.head_y, self.tail_x, self.tail_y = 0, 0, 0, 0
        self.prev_pos_head_x, self.prev_pos_head_y = 0, 0
        self.where_tail_was = {}

    def tail_near_head(self):
        return abs(self.head_x - self.tail_x) <= 1 and abs(self.head_y - self.tail_y) <= 1

    def memorize_tail_position(self):
        position = self.tail_x * 100000 + self.tail_y
        self.where_tail_was[position] = 0

    def move_head(self, step_x, step_y):
        self.prev_pos_head_x = self.head_x
        self.prev_pos_head_y = self.head_y
        self.head_x += step_x
        self.head_y += step_y

    def move_tail(self):
        self.tail_x = self.prev_pos_head_x
        self.tail_y = self.prev_pos_head_y

    def get_visited_positions(self):
        return len(self.where_tail_was)


def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    return data


def emulate_rope_motion(command, rope):
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
        rope.move_head(step_x, step_y)
        if not rope.tail_near_head():
            rope.move_tail()
        rope.memorize_tail_position()
    return rope


def main():
    file_name = "Day09-input-p.txt"
    data_input = parse_file(file_name)
    part_two = 1

    rope = Rope()

    for command in data_input:
        rope = emulate_rope_motion(command.split(" "), rope)

    part_one = rope.get_visited_positions()

    print("----------------------------")
    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One: 6384
# Part Two: