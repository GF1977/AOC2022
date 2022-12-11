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
        self.crt = []
        for i in range(1, 241):
            self.crt += "."

    def execute(self, command):
        if command == "noop":
            self.tick()

        else:
            cmd, arg = command.split(" ")

            pass
            self.tick()

            self.X += int(arg)
            self.tick()

    def draw_sprite(self):
        # counter position is within the 3pixel sprite (-1, 0 , 1)
        if self.X - 1 <= self.counter <= self.X + 1:
            self.crt[self.counter] = "#"

    def show_screen(self):
        pass
        crt_line = ""
        for a in self.crt:
            crt_line+= str(a)
        print(crt_line[ 0:40])
        print(crt_line[40:80])
        print(crt_line[80:120])
        print(crt_line[120:160])
        print(crt_line[160:200])
        print(crt_line[200:240])



    def tick(self):
        self.draw_sprite()
        self.counter += 1
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

    cpu.show_screen()




    part_one = cpu.signal_str_summary
    part_two = 1

    print(" ")
    print("----------------------------")
    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One: 15020
# Part Two: