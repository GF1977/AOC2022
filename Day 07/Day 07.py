from anytree import Node, RenderTree, PreOrderIter


def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")
    return data


class File(object):
    def __init__(self, file_type, file_size, file_name):
        self.file_type = file_type
        self.file_name = file_name
        self.file_size = file_size


def show_tree(_root):
    for pre, fill, node in RenderTree(_root):
        element = node.name.file_name + " (Type:" + node.name.file_type + "  Size:" + str(node.name.file_size) + ")"
        print("%s%s" % (pre, element))


def update_dir_sizes(node: Node):
    size = 0
    for child in node.children:
        if child.name.file_type == "f":
            size = size + int(child.name.file_size)
        else:
            size = size + update_dir_sizes(child)
    node.name.file_size = size
    return size


def main():
    file_name = "Day07-input-p.txt"
    data_input = parse_file(file_name)

    root = Node(File("d", 0, "/"))
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

        else:  # everything here is the output of "ls" command
            file_info = line.split(" ")
            if file_info[0] == "dir":
                new_f = File(file_type="d", file_name=file_info[1], file_size=0)
            else:
                new_f = File(file_type="f", file_name=file_info[1], file_size=file_info[0])

            Node(new_f, parent=current_dir)

    update_dir_sizes(root)

    disk_space_available = 70000000
    need_unused_space = 30000000
    free_space = disk_space_available - root.name.file_size
    space_to_release = need_unused_space - free_space

    part_one = 0
    part_two = root.name.file_size

    for child in PreOrderIter(root):
        dir_size = child.name.file_size
        if child.name.file_type == "d":
            if dir_size < 100000:
                part_one += dir_size
            if space_to_release <= dir_size < part_two:
                part_two = dir_size

    print("----------------------------")
    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One: 1297159
# Part Two: 3866390