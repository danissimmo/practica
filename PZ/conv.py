import sys


class Node:
    def __init__(self, node, level):
        self.node = node
        self.level = level


def print_child_nodes(input_file, output_file, parent_node, current_node, level):
    node_level = level
    node_string = ""
    prev_node = current_node

    for line in input_file:
        node_string = line
        node_level = node_string.count("\t")

        node = node_string[node_level:].strip()

        while node != "" and node_level > level:
            output_file.write(f"{node};{prev_node};1\n")

            next_level = node_level + 1

            node_class = print_child_nodes(input_file, output_file, prev_node, node, next_level)

            node = node_class.node
            node_level = node_class.level

        if node_level == level:
            output_file.write(f"{node};{parent_node};1\n")

        if node_level < level:
            level = node_level
            return Node(node, level)

        prev_node = node

    return Node("", level)


def parse_mindmap(input_file, output_file):
    node_string = input_file.readline().strip()
    level = 1
    parent_nodes = [node_string]

    output_file.write("Source; Target; distance\n")
    print_child_nodes(input_file, output_file, node_string, "", level)


if __name__ == "__main__":
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]

    try:
        input_file = open(input_file_name, "r")
        output_file = open(output_file_name, "w")

        parse_mindmap(input_file, output_file)

    except FileNotFoundError:
        print("Can't open file for reading or writing")
        sys.exit(1)
