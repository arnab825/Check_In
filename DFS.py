# =========================
# Depth-First Search (DFS) Implementation
# Using Adjacency List Representation of Graph
# =========================

# Class to represent a Graph
class Graph:
    def __init__(self, vertices):
        """
        Initialize a graph with given number of vertices.
        :param vertices: Total number of vertices in the graph
        """
        self.vertices = vertices
        # Using a dictionary to store adjacency list
        self.adj_list = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        """
        Add an edge from vertex u to vertex v.
        For an undirected graph, also add from v to u.
        :param u: Start vertex
        :param v: End vertex
        """
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # Comment this line for directed graph

    def dfs_util(self, v, visited):
        """
        Utility function for DFS traversal from a given vertex
        :param v: Current vertex
        :param visited: List to keep track of visited vertices
        """
        # Mark the current node as visited
        visited[v] = True
        print(v, end=' ')  # Print the current vertex

        # Recur for all adjacent vertices
        for neighbour in self.adj_list[v]:
            if not visited[neighbour]:
                self.dfs_util(neighbour, visited)

    def dfs(self, start_vertex):
        """
        Perform DFS traversal starting from a given vertex
        :param start_vertex: Starting point for DFS
        """
        # Initially, no vertex is visited
        visited = [False] * self.vertices
        # Start DFS from the start_vertex
        self.dfs_util(start_vertex, visited)


# =========================
# Example Usage
# =========================

# Create a graph with 5 vertices (0 to 4)
g = Graph(5)

# Add edges to the graph
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 4)

# Perform DFS starting from vertex 0
print("DFS traversal starting from vertex 0:")
g.dfs(0)
