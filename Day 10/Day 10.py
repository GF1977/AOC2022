def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    return data


class CPU:
    def __init__(self):
        self.X = 1
        self.counter = 0
        self.signal_str_summary = 0
        self.crt = []

    def execute(self, command):
        if command == "noop":
            self.tick()
        else:
            cmd, arg = command.split(" ")
            self.tick()
            self.tick()
            self.X += int(arg)

    def draw_sprite(self):
        self.crt.append(".")
        # counter position is within the 3pixel sprite (-1, 0 , 1)
        if self.X - 1 <= self.counter % 40 <= self.X + 1:
            self.crt[self.counter] = "░"

    def show_screen(self):
        crt_line = ""
        for a in self.crt:
            crt_line += str(a)
        for n in range(0, 6):
            print(crt_line[40 * n:40 * n + 40])

    def tick(self):
        self.draw_sprite()
        self.counter += 1
        if (self.counter + 20) % 40 == 0:
            self.signal_str_summary += self.X * self.counter


def main():
    file_name = "Day10-input-p.txt"
    data_input = parse_file(file_name)

    cpu = CPU()
    for command in data_input:
        cpu.execute(command)

    print("Part One:", cpu.signal_str_summary)
    cpu.show_screen()


if __name__ == "__main__":
    main()

# Answers:
# Part One: 15020
# Part Two: EFUGLPAP
