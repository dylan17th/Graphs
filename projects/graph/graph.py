from util import Stack, Queue  # These may come in handy

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else: 
            return("that index does not exist")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        my_queue = Queue()
        my_queue.enqueue(starting_vertex)

        visited = set()

        while my_queue.size() > 0:
            visited_node = my_queue.dequeue()

            if visited_node not in visited:
                visited.add(visited_node)
                print(visited_node)
                
                for node in self.get_neighbors(visited_node):
                    my_queue.enqueue(node)

    def dft(self, starting_vertex):
        my_stack = Stack()
        visited = set()

        my_stack.push(starting_vertex)

        while my_stack.size() > 0:
            visited_node = my_stack.pop()

            if visited_node not in visited:
                visited.add(visited_node)
                print(visited_node)
                
                for node in self.get_neighbors(visited_node):
                    my_stack.push(node)

    def dft_recursive(self, starting_vertex, visited=None ):
        if visited is None:
            visited = set() 
        print(starting_vertex)
        visited.add(starting_vertex)
        for index in self.get_neighbors(starting_vertex):
            if index not in visited:
                self.dft_recursive(index, visited)

    def bfs(self, starting_vertex, destination_vertex):

        my_queue = Queue()
        my_queue.enqueue([starting_vertex])
        
        visited = set()

        while my_queue.size() > 0:

            node = my_queue.dequeue()
            new_path = node[-1]
            if new_path not in visited:

                if new_path is destination_vertex:
                    return node
                else: 
                    visited.add(new_path)
                    for next_node in self.get_neighbors(new_path):
                        next_in_queue = node 
                        path = next_in_queue + [next_node]
                        my_queue.enqueue(path)

        return None

    def dfs(self, starting_vertex, destination_vertex):
       
        my_stack = Stack()
        my_stack.push([starting_vertex])
        
        visited = set()

        while my_stack.size() > 0:

            node = my_stack.pop()
            new_path = node[-1]
            if new_path not in visited:

                if new_path is destination_vertex:
                    return node
                else: 
                    visited.add(new_path)
                    for next_node in self.get_neighbors(new_path):
                        next_in_queue = node 
                        path = next_in_queue + [next_node]
                        my_stack.push(path)

        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = {}, path= []):    
        if starting_vertex not in visited:
            visited[starting_vertex] = path + [starting_vertex] 
            for next_node in self.get_neighbors(starting_vertex):
                path = visited[starting_vertex]
                self.dfs_recursive(next_node, destination_vertex, visited, path)
            if destination_vertex in visited:
                return visited[destination_vertex]



if __name__ == '__main__':

    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)


    # '''
    # Should print:
    #     {1: {2}, 2: 4} {3,, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    # '''
    print(graph.vertices)

    # '''
    # Valid BFT paths:
    #     1, 2, 3, 4, 5, 6, 7
    #     1, 2, 3, 4, 5, 7, 6
    #     1, 2, 3, 4, 6, 7, 5
    #     1, 2, 3, 4, 6, 5, 7
    #     1, 2, 3, 4, 7, 6, 5
    #     1, 2, 3, 4, 7, 5, 6
    #     1, 2, 4, 3, 5, 6, 7
    #     1, 2, 4, 3, 5, 7, 6
    #     1, 2, 4, 3, 6, 7, 5
    #     1, 2, 4, 3, 6, 5, 7
    #     1, 2, 4, 3, 7, 6, 5
    #     1, 2, 4, 3, 7, 5, 6
    # '''
    # graph.bft(1)

    # '''
    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    # print(graph.dft(1))
    graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    # print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6), "this is the result of the dfs method")
