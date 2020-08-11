from util import Stack
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertexs(self, ancestors):
        for pair in ancestors:
            if pair[0] not in self.vertices:
                self.vertices[pair[0]] = set()
            if pair[1] not in self.vertices:
                self.vertices[pair[1]] = set()

    def add_edge(self, ancestors):
        for pair in ancestors:
            if pair[0] in self.vertices and pair[1] in self.vertices:
                self.vertices[pair[1]].add(pair[0])
            else: 
                return("that index does not exist")

    def get_neighbors(self, key):
        return self.vertices[key]


def earliest_ancestor(ancestors, starting_node):
    my_graph = Graph()
    my_graph.add_vertexs(ancestors)
    my_graph.add_edge(ancestors)

    if my_graph.vertices[starting_node] == set():
        return -1

    my_stack = Stack()
    visited = set()
    my_stack.push([starting_node])
    highest = []

    while my_stack.size() > 0:
        visited_node = my_stack.pop()
        new_path = visited_node[-1]

        if new_path not in visited:
            visited.add(new_path)   
            for node in my_graph.get_neighbors(new_path):
                path = visited_node + [node] 
                if len(path) > len(highest) or path[-1] < highest[-1]:
                    highest = path
                my_stack.push(path)
                
    return highest[-1]


if __name__ == "__main__":
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors,9))
    #expected output is 10