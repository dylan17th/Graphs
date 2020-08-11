from util import Stack

def get_neighbors(number, ancestors):
    numbers = []
    for pair in ancestors:
        if pair[1] == number:
            numbers.append(pair[0])
    return numbers


def earliest_ancestor(ancestors, starting_node):
    my_stack = Stack()
    visited = {}
    my_stack.push([starting_node])

    while my_stack.size() > 0:
        visited_node = my_stack.pop()
        new_path = visited_node[-1]
        if new_path not in visited:
            visited[new_path] = visited_node
                
            for node in get_neighbors(new_path, ancestors):
                path = visited_node + [node]
                if "highest" in visited: 
                    if len(path) > len(visited["highest"]) or path[-1] < visited["highest"][-1]:
                            visited["highest"] = path
                if "highest" not in visited:
                    visited["highest"] = path
                my_stack.push(path)
    if "highest" in visited:
        return visited["highest"][-1]
    else:
        return -1


if __name__ == "__main__":
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors,2))
    #expected output is 10