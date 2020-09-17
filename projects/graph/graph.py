"""
Simple graph implementation
"""
# from util import Stack, Queue  # These may come in handy
from collections import deque

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices: # vertex_id not in self.vertices
            self.vertices[vertex_id] = set() #set self.verticed[vertex_id] to an empty set

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2) 

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id] if vertex_id in self.vertices else set()

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set()
        queue = deque()
        queue.append(starting_vertex)
        while len(queue) > 0:
            currNode = queue.popleft()
            if currNode not in visited:
                visited.add(currNode)
                print(currNode)
                for neighbor in self.get_neighbors(currNode):
                    queue.append(neighbor)
        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set() # making visited into an empty set
        stack = deque() # making stack into an empty deque
        stack.append(starting_vertex) # append starting_vertex into stack
        while len(stack) > 0: # while the length of stack is greater than zero
            currNode = stack.pop() # make currNode equal to stack.pop()
            if currNode not in visited: # if currNode is not in visited
                visited.add(currNode) # add currNode to visited
                print(currNode) # print the currNode being added
                for neighbor in self.get_neighbors(currNode): # for neighbor in get_neighbors
                    stack.append(neighbor) # add neighbor to stack

    def dft_recursive(self, starting_vertex, seen=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if starting_vertex not in seen: # if starting_vertex not in seen
            print(starting_vertex) # print the starting_vertex
            seen.add(starting_vertex) # add starting_vertex to seen

            for neighbor in self.get_neighbors(starting_vertex): # for neighbor in self.get_neighbors(starting_vertex)
                self.dft_recursive(neighbor, seen) # use recurrsion to call itself 


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = set() # set visited to an empty set
        stack = deque() # set stack to an empty deque
        stack.append([starting_vertex]) # append starting_vertex to stack

        while len(stack) > 0: # if length of stack is greater than zero
            path = stack.pop() # set path equal to stack.pop()
            currNode = path[-1] # set currNode equal to the last item in path
            
            if currNode not in visited: # if currNode is not in visited
                for neighbor in self.get_neighbors(currNode): # for neighbor in self.get_neighbors(currNode)
                    if neighbor == destination_vertex: # if that neighbor is equal to destination_vertex
                        path.append(neighbor) # append that neighbor to path
                        return path # return path

                    visited.add(currNode) # add currNode to visited
                    currPath = path.copy() # set currPath to path.copy()
                    currPath.append(neighbor) # append neighbor to currPath
                    stack.append(currPath) # append that currPath to stack


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = deque()
        stack.append([starting_vertex])
        visited = set()
        while len(stack) > 0:
            currPath = stack.pop()
            currNode = currPath[-1]
            if currNode == destination_vertex:
                return currPath
            if currNode not in visited:
                visited.add(currNode)
                for neighbor in self.get_neighbors(currNode):
                    newPath = list(currPath)
                    newPath.append(neighbor)
                    stack.append(newPath)

    def dfs_recursive(self, starting_vertex, destination_vertex, seen=set(), path=list()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if path == []:
            path = [starting_vertex]
        if starting_vertex not in seen:
            seen.add(starting_vertex)

            if starting_vertex == destination_vertex:
                return path

            for neighbor in self.get_neighbors(starting_vertex):
                result = self.dfs_recursive(neighbor, destination_vertex, seen, path + [neighbor])
                if result:
                    return result

        return None

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

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
