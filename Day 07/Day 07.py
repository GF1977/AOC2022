from anytree import Node, RenderTree, PreOrderIter


def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    return data


class File(object):
    def __init__(self, file_type, file_size, file_name):
        self.file_type = file_type
        self.file_name = file_name
        if file_type == "f":
            self.file_size = file_size
        if file_type == "d":
            self.file_size = 0

def show_tree(_root):
    for pre, fill, node in RenderTree(_root):
        if node.name == "/":
            element = "/"
        else:
            element = node.name.file_name + " (Type:" + node.name.file_type + "  Size:" + str(node.name.file_size) + ")"
        print("%s%s" % (pre, element))

def walk_the_tree(node: Node):
    size = 0
    for child in node.children:
        if child.name.file_type == "f":
            size = size + int(child.name.file_size)
        else:
            size = size + walk_the_tree(child)

    dir_name = node.name.file_name
    node.name.file_size = size

    print("Directory = {:<12} Size = {:<40}".format(dir_name, size))


    return size


def main():

    #tree_test()
    #return 0

    file_name = "Day07-input-p.txt"
    data_input = parse_file(file_name)

    root = Node(File("d",0,"/"))
    current_dir = root

    for line in data_input:
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
                            if node.name.file_name == new_dir and node.name.file_type == "d":
                                current_dir = node
                                break

        else:
            result = line.split(" ")
            new_f = File(file_type="", file_size= 0, file_name = "")
            new_file = line
            if result[0] == "dir":
                new_file = result[1]
                new_f.file_type = "d"
                new_f.file_size = 0
                new_f.file_name = result[1]
            else:
                new_f.file_type = "f"
                new_f.file_size = result[0]
                new_f.file_name = result[1]


            Node(new_f, parent=current_dir)

    walk_the_tree(root)
    show_tree(root)

    part_one = 0
    for child in PreOrderIter(root):
        a = 9
        if child.name.file_type == "d" and child.name.file_size < 100000:
            part_one += child.name.file_size


    #part_one = 0
    part_two = 1

    print("----------------------------")
    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One:
# Part Two:
