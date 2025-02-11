"""## Question 4 **[PY]**{: .htag } ##

Given a weighted vertex graph $G(V,E)$, a start node
$s$ and a target sum $\\sigma$.

**Write an algorithm, or equivalently a python program
(WAP)** to inspect if there is a path from $s$ such
that adding up all the vertex weights along the path,
equals the target sum.

Note: $\\forall v \\in V\\; \\exists v.w$ that
represents vertex weights.
"""
from . import Graph,Bbt
def q04IsPathSumP(G:Graph,s:int,targetSum:int) :
  """
  Args:
    G: Graph resolves into `G.V` and `G.E`.
    s: The start node.
    targetSum: The target sum.

"""

  pass




class Graph:
    def __init__(self):
        self.V = {}  # Dictionary to store vertex weights
        self.E = {}  # Dictionary to store edges
    
    def add_vertex(self, v, weight):
        """Add vertex v with weight to the graph"""
        self.V[v] = weight
        if v not in self.E:
            self.E[v] = []
    
    def add_edge(self, u, v):
        """Add an edge from u to v"""
        if u in self.E:
            self.E[u].append(v)
        else:
            self.E[u] = [v]

    def get_neighbors(self, v):
        """Return the list of neighbors for vertex v"""
        return self.E.get(v, [])


def q04IsPathSumP(G: Graph, s: int, targetSum: int) -> bool:
    """
    Inspect if there is a path starting from node `s` such that the sum of vertex weights
    along the path equals the target sum `targetSum`.
    
    Args:
    G: A Graph object with vertices (G.V) and edges (G.E).
    s: The start node.
    targetSum: The target sum to check for.
    
    Returns:
    True if such a path exists, False otherwise.
    """

    def dfs(current_node, current_sum, visited):
        # If current sum matches target sum, return True
        if current_sum == targetSum:
            return True
        
        # Mark the current node as visited
        visited.add(current_node)
        
        # Explore all neighbors of the current node
        for neighbor in G.get_neighbors(current_node):
            if neighbor not in visited:
                new_sum = current_sum + G.V.get(neighbor, 0)
                if dfs(neighbor, new_sum, visited):
                    return True
        
        # Unmark current node before backtracking
        visited.remove(current_node)
        return False
    
    # Start DFS from the start node, initializing the sum with the start node's weight
    return dfs(s, G.V.get(s, 0), set())


# Example usage:
G = Graph()

# Add vertices and their weights
G.add_vertex(0, 5)
G.add_vertex(1, 3)
G.add_vertex(2, 4)
G.add_vertex(3, 2)

# Add edges
G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)

start_node = 0
target_sum = 8

# Check if there is a path from start_node that sums to target_sum
result = q04IsPathSumP(G, start_node, target_sum)
print("Path exists with target sum:", result)
