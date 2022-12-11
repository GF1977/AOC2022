def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    return data

class Monkey:
    def __init__(self, starting_items, operation, test, if_true_to_A, if_false_to_B):
        self.starting_items = starting_items
        self.operation = operation          # new worry level = old w.l. & operation
        self.test = test                    # divisible by test
        self.throw_to_A = if_true_to_A      # throw to monkey A
        self.throw_to_B = if_false_to_B     # throw to monkey B

    def inspect_and_throw(self):
        throwing_items = [] # throw to, worry level      [1, 123]  w.l. 123 throw to monkey #1
        for item in range(0, 2):
            worry_level = self.adjust_worry_level(self.starting_items[item])
            throw_to = self.throw_to_B
            if worry_level % self.test:
                throw_to = self.throw_to_A

            #throw
            del self.starting_items[item]
            throwing_items.append([worry_level, throw_to])

        return throwing_items

    def throw_item(self, item, worry_level, throw_to):
        del self.starting_items[item]
        return worry_level, throw_to

    def adjust_worry_level(self, level):
        operation, value = self.operation.split(" ")
        if value == "old":
            value = level

        new_level = 0
        if operation == "+":
            new_level = level + value
        if operation == "*":
            new_level = level * value

        new_level = new_level // 3

        return new_level




def main():
    file_name = "Day11-input-d.txt"
    data_input = parse_file(file_name)
    part_one = 0
    part_two = 1

    monkeys = [Monkey([79, 98], "* 19", 23, 2, 3),
               Monkey([54, 65, 75, 74], "+ 6", 19, 2, 0),
               Monkey([79, 60, 97], "* old", 13, 1, 3),
               Monkey([74], "+ 3", 17, 0, 1)]

    for round in (0,3):
        for monkey in monkeys:
            throwing_items = monkey.inspect_and_throw()


    print("----------------------------")
    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One:
# Part Two:
