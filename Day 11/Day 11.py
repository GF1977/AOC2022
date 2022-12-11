def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    monkeys = []

    monkey_n = 0
    block_to_parse = []
    block_index = 0

    for line in data:
        if "Monkey" in line:
            block_to_parse = data[block_index: block_index + 7]
            block_index +=7

            monkey_n = block_to_parse[0].split(" ")[1][0]
            starting_items = block_to_parse[1].split(": ")[1].split(",")
            operation = block_to_parse[2].split("= ")[1]
            test = block_to_parse[3].split("by ")[1]
            if_true_to = block_to_parse[4].split("monkey ")[1]
            if_false_to = block_to_parse[5].split("monkey ")[1]

            monkeys.append(Monkey(monkey_n,starting_items, operation, test, if_true_to, if_false_to))
            block_to_parse = []




    return monkeys

class Monkey:
    def __init__(self, number, starting_items, operation, test, if_true_to_A, if_false_to_B):
        self.number = int(number)
        self.starting_items = starting_items
        self.operation = operation          # new worry level = old w.l. & operation
        self.test = int(test)                    # divisible by test
        self.throw_to_A = int(if_true_to_A)      # throw to monkey A
        self.throw_to_B = int(if_false_to_B)     # throw to monkey B
        self.items_inspected = 0
        self.simplifying_coefficient = 1

    def inspect_and_throw(self, part_to_solve):
        throwing_items = [] # throw to, worry level      [1, 123]  w.l. 123 throw to monkey #1

        relief_coefficient = 1
        if part_to_solve == 1:
            relief_coefficient = 3

        self.items_inspected += len(self.starting_items)
        for item_str in self.starting_items:
            item = int(item_str)
            #print("Monkey inspects an item with a worry level of ", item)



            worry_level = self.adjust_worry_level(item, relief_coefficient)
            ops = self.operation.split(" ")
            #print("Worry level is ", ops[0]," by ", ops[1],  " to  ", worry_level)
            throw_to = self.throw_to_A
            if worry_level % self.test:
                throw_to = self.throw_to_B

            #throw


            throwing_items.append([throw_to, worry_level])
            #print("Item with worry level  ",worry_level, "thrown to monkey ", throw_to)


        self.starting_items = []

        return throwing_items


    def adjust_worry_level(self, level, relief_coefficient):
        old, operation, value_str = self.operation.split(" ")
        if value_str == "old":
            value = level
        else:
            value = int(value_str)

        new_level = 0
        if operation == "+":
            new_level = level + value
        if operation == "*":
            new_level = level * value

        new_level = new_level // relief_coefficient

        if relief_coefficient == 1:
            new_level = new_level % self.simplifying_coefficient

        return new_level

# def print_monkeys(monkeys: Monkey):
#     for monkey in monkeys:
#         items = "Monkey " + str(monkey.number) + ": "
#         for item in monkey.starting_items:
#             items += str(item) + " "
#         print(items)

def inspected_items_status(monkeys: Monkey):
    i = 0
    times_inspected = []
    for m in monkeys:
        times_inspected.append(m.items_inspected)
        print("Monkey ", i, " inspected items ", m.items_inspected, " times.")
        i += 1

    times_inspected.sort(reverse=True)
    level_monkey_business = times_inspected[0] * times_inspected[1]
    return level_monkey_business

def main():
    file_name = "Day11-input-p.txt"

    part_one = 0
    part_two = 1

    monkeys = parse_file(file_name)

    simpl_coeff = 1
    for m in monkeys:
        simpl_coeff *= m.test

    for m in monkeys:
        m.simplifying_coefficient = simpl_coeff

    for round in range(1,10001):
        for monkey in monkeys:
            throwing_items = monkey.inspect_and_throw(part_to_solve=2)
            for item in throwing_items:
                throw_to = item[0]
                worry_level = item[1]
                monkeys[throw_to].starting_items.append(worry_level)


    part_one = inspected_items_status(monkeys)



    print("----------------------------")
    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One:
# Part Two:
