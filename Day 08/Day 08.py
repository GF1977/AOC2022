def parse_file(file_to_process):
    file = open(file_to_process, mode="r")
    data: list[str] = file.read().split("\n")

    return data



def get_tree_details(row, col, tree_map):
    tree_size = tree_map[row][col]
    is_visible = 4  # let's assume a tree is visible from all 4 sides

    up_scenic_score = 0
    for r in range(row - 1, -1, -1):  # this weird  -1 -1 because we are moving from center to periphery
        up_scenic_score += 1
        if tree_size <= tree_map[r][col]:
            is_visible -= 1
            break

    down_scenic_score = 0
    for r in range(row + 1, len(tree_map)):
        down_scenic_score += 1
        if tree_size <= tree_map[r][col]:
            is_visible -= 1
            break

    left_scenic_score = 0
    for c in range(col - 1, -1, -1):
        left_scenic_score += 1
        if tree_size <= tree_map[row][c]:
            is_visible -= 1
            break

    right_scenic_score = 0
    for c in range(col + 1, len(tree_map[0])):
        right_scenic_score += 1
        if tree_size <= tree_map[row][c]:
            is_visible -= 1
            break

    return up_scenic_score * down_scenic_score * right_scenic_score * left_scenic_score, is_visible


def analyze_the_map(tree_map):
    count_trees_visible = 0
    best_scenic_score = 0

    for r in range(0, len(tree_map)):
        for c in range(0, len(tree_map[0])):
            scenic_score, is_visible = get_tree_details(r, c, tree_map)
            if is_visible:
                count_trees_visible += 1
            if scenic_score > best_scenic_score:
                best_scenic_score = scenic_score

    return count_trees_visible, best_scenic_score


def main():
    file_name = "Day08-input-p.txt"
    tree_map = parse_file(file_name)
    count_trees_visible, best_scenic_score = analyze_the_map(tree_map)
    print("----------------------------")
    print("Part One:", count_trees_visible)
    print("Part Two:", best_scenic_score)


if __name__ == "__main__":
    main()

# Answers:
# Part One: 1851
# Part Two: 574080