from anytree import Node, RenderTree


def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    return data


class File(object):
    def __init__(self, file_type, size, name):
        self.file_type = file_type
        self.name = name
        if file_type == "f":
            self.size = size
        if file_type == "d":
            self.size = 0


def tree_test():
    udo = Node("Udo")
    marc = Node("Marc", parent=udo)
    lian = Node("Lian", parent=marc)
    dan = Node("Dan", parent=udo)
    jet = Node("Jet", parent=dan)
    jan = Node("Jan", parent=dan)
    joe = Node("Joe", parent=dan)
    abc = Node("ABC", parent=lian)

    a = Node('/Udo/Dan/Joe')
    print(a)

    for pre, fill, node in RenderTree(udo):
        print("%s%s ID:%s" % (pre, node.name, id(node)))


def main():

    #tree_test()
    #return 0

    file_name = "Day07-input-d.txt"
    data_input = parse_file(file_name)

    root_file = File("d", 0, "/")
    nodes = {}
    root = Node("root")
    current_dir = root

    for line in data_input:
        if current_dir is None:
            print("stop")
            return 0

        if line[0] == "$":
            command = line.split(" ")
            if command[1] == "cd":
                if command[2] == "/":
                    current_dir = root
                else:
                    if command[2] == "..":
                        current_dir = current_dir.parent
                    else:
                        new_dir = command[2]
                        for node in current_dir.children:
                            if node.name == new_dir:
                                current_dir = node
                                break


        else:
            result = line.split(" ")
            new_file = line
            #
            if result[0] == "dir":
                new_file = result[1]
            #if new_file not in nodes[current_dir_id].children:
            new_node = Node(new_file, parent=current_dir)

    for pre, fill, node in RenderTree(root):
        # print("%s%s ID:%s" % (pre, node.name,id(node)))
        result = node.name.split(" ")

        if len(result) == 1:
            element = result[0] + "(dir)"
        else:
            element = result[1] + " (file, size = " + result[0] + ")"

        print("%s%s" % (pre, element))

    # tree_test()

    part_one = 0
    part_two = 1

    print("----------------------------")
    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One:
# Part Two:
