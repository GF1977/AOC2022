def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    monkeys = []
    block_len = 7

    for block_index in range(0, len(data), block_len):
        block_to_parse = data[block_index: block_index + block_len]
        block_index += block_len

        starting_items = block_to_parse[1].split(": ")[1].split(",")
        operation = block_to_parse[2].split("old ")[1]
        test = block_to_parse[3].split("by ")[1]
        if_true_to = block_to_parse[4].split("monkey ")[1]
        if_false_to = block_to_parse[5].split("monkey ")[1]

        monkeys.append(Monkey(starting_items, operation, int(test), int(if_true_to), int(if_false_to)))
    return monkeys


class Monkey:
    def __init__(self, starting_items, operation, test, if_true_to_a, if_false_to_b):
        self.items = starting_items
        self.operation = operation  # new worry level = old worry level operation(+ or *) value
        self.test = test  # divisible by test
        self.throw_to_A = if_true_to_a  # throw to monkey A
        self.throw_to_B = if_false_to_b  # throw to monkey B
        self.items_inspected = 0

    def inspect_and_throw(self, number_of_rounds, simplifying_coefficient):
        throwing_items = []  # [throw to, worry level]   Example:   [1, 123]  w.l. 123 throw to monkey #1

        relief_coefficient = 1
        if number_of_rounds == 21:
            relief_coefficient = 3

        self.items_inspected += len(self.items) # This one collects the number of inspected items by single monkey
        for item_str in self.items:
            item = int(item_str)
            worry_level = self.adjust_worry_level(item, relief_coefficient)
            if relief_coefficient == 1:
                worry_level = worry_level % simplifying_coefficient

            # throw
            if worry_level % self.test:
                throw_to = self.throw_to_B
            else:
                throw_to = self.throw_to_A

            throwing_items.append([throw_to, worry_level])

        self.items = []  # removing all items as monkeys throw away everything
        return throwing_items

    def adjust_worry_level(self, worry_level, relief_coefficient):
        operation, value_str = self.operation.split(" ")
        if value_str == "old":
            value = worry_level
        else:
            value = int(value_str)

        if operation == "+":
            worry_level = worry_level + value
        if operation == "*":
            worry_level = worry_level * value

        worry_level = worry_level // relief_coefficient

        return worry_level


def get_level_monkey_business(monkeys):
    times_inspected = []
    for m in monkeys:
        times_inspected.append(m.items_inspected)

    times_inspected.sort(reverse=True)
    return times_inspected[0] * times_inspected[1]


def solve_puzzle(number_of_rounds, monkeys):
    simplifying_coefficient = 1
    for m in monkeys:
        simplifying_coefficient *= m.test

    for game_round in range(1, number_of_rounds):
        for monkey in monkeys:
            #  leveraging "number_of_rounds" as identification of puzzle part; Example: 21 - part one; 10001 - part two
            throwing_items = monkey.inspect_and_throw(number_of_rounds, simplifying_coefficient)
            # catching items
            for item in throwing_items:
                throw_to = item[0]
                worry_level = item[1]
                monkeys[throw_to].items.append(worry_level)

    return get_level_monkey_business(monkeys)


def main():
    file_name = "Day11-input-p.txt"
    monkeys = parse_file(file_name)
    part_one = solve_puzzle(number_of_rounds=21, monkeys=monkeys)

    monkeys = parse_file(file_name)
    part_two = solve_puzzle(number_of_rounds=10001, monkeys=monkeys)

    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One: 120056
# Part Two: 21816744824
