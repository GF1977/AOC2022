where_tail_was = {}



def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    return data


def is_t_and_h_in_touch(h_x, h_y, t_x, t_y):
    if abs(h_x - t_x) <= 1 and abs(h_y - t_y) <= 1:
        return True
    else:
        return False




def move_head(command, h_x, h_y, t_x, t_y, prev_step_x, prev_step_y):

    command = command.split(" ")
    direction = command[0]
    distance = int(command[1])
    tail_position = str(t_x)+":"+str(t_y)
    #where_tail_was[tail_position] = 0

    step_x = 0
    step_y = 0

    if direction == "R":
        step_x = 1
    if direction == "L":
        step_x = -1
    if direction == "U":
        step_y = 1
    if direction == "D":
        step_y = -1

    #print("Command: ", command)
    for step in range(0, distance):
        h_x += step_x
        h_y += step_y

        in_touch = is_t_and_h_in_touch(h_x, h_y, t_x, t_y)
        if not in_touch:
            t_x += step_x
            t_y += step_y

            if h_y != t_y and h_x != t_x:
                t_x += prev_step_x
                t_y += prev_step_y

            tail_position = str(t_x) + ":" + str(t_y)


        #print("[h_x ; h_y] = ", h_x, ";", h_y)
        #print("[t_x ; t_y] = ", t_x, ";", t_y)
        #print("-------------------------------")

        if tail_position not in where_tail_was.keys():
            where_tail_was[tail_position] = 0
        else:
            where_tail_was[tail_position] += 1

    prev_step_x = step_x
    prev_step_y = step_y

    return h_x, h_y, t_x, t_y, tail_position, prev_step_x, prev_step_y

def main():
    file_name = "Day09-input-d.txt"
    data_input = parse_file(file_name)
    part_one = 0
    part_two = 1


    h_x = 00000000
    h_y = 00000000
    t_x = 00000000
    t_y = 00000000

    prev_step_x = 0
    prev_step_y = 0

    tail_position = ""
    for command in data_input:
        h_x, h_y, t_x, t_y, tail_position, prev_step_x, prev_step_y = move_head(command, h_x, h_y, t_x, t_y, prev_step_x, prev_step_y)





    part_one = len(where_tail_was)

    print("----------------------------")
    print("Part One:", part_one)
    print("Part Two:", part_two)


    # res = []
    # for x in range(0,12):
    #     line = []
    #     for y in range(0, 12):
    #         line.append(".")
    #     res.append(line)
    #
    # for a in where_tail_was:
    #     x,y = a.split(":")
    #     #print (XY[0], XY[1])
    #     res[11 - int(y)][int(x)] = "#"
    #
    #
    # for l in res:
    #     s = ""
    #     for a in l:
    #         s+=a
    #     print(s)


if __name__ == "__main__":
    main()

# Answers:
# Part One:
# Part Two: