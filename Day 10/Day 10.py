def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    return data

class CPU:
    def __init__(self):
        self.X = 1
        self.counter = 1
        self.signal_str = 0
        self.signal_str_summary = 0

    def execute(self, command):
        if command == "noop":
            self.counter += 1
            self.counter_check()

        else:
            cmd, arg = command.split(" ")
            self.counter += 1
            self.counter_check()

            self.X += int(arg)
            self.counter += 1
            self.counter_check()



    def counter_check(self):
        if (self.counter + 20) % 40 == 0:
            print("Counter: ", self.counter, "     X: ", self.X)
            self.signal_str = self.X * self.counter
            self.signal_str_summary += self.signal_str


def main():
    file_name = "Day10-input-p.txt"
    data_input = parse_file(file_name)


    cpu = CPU()
    for command in data_input:
        cpu.execute(command)




    part_one = cpu.signal_str_summary
    part_two = 1

    print("----------------------------")
    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One:
# Part Two: