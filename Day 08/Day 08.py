def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    return data


def is_tree_visible(row, col, tree_map):
    tree_size = tree_map[row][col]

    left = tree_map[row][:col]
    right = tree_map[row][col + 1:]

    up = []
    for r in range(0, row):
        up.append(tree_map[r][col])

    down = []
    for r in range(row + 1, len(tree_map)):
        down.append(tree_map[r][col])

    return max(left) < tree_size or max(right)  < tree_size or max(down) < tree_size or max(up)  < tree_size

def count_visible_trees(tree_map):
    width = len(tree_map[0])
    height = len(tree_map)

    count = 2 * width + 2 * height - 4  # perimeter

    is_tree_visible(1, 3, tree_map)

    for r in range(1, height - 1):
        for c in range(1, width - 1):
            if is_tree_visible(r, c, tree_map):
                count += 1
    return count


def main():
    file_name = "Day08-input-p.txt"
    tree_map = parse_file(file_name)

    part_one = count_visible_trees(tree_map)
    part_two = 1

    print("----------------------------")
    print("Part One:", part_one)
    print("Part Two:", part_two)


if __name__ == "__main__":
    main()

# Answers:
# Part One: 1851
# Part Two:
