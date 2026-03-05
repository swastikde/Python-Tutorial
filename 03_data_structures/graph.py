# =============================================================
# Module 3: Graph Data Structure
# =============================================================
# A Graph is a set of vertices (nodes) connected by edges.
#
# Representations:
#   - Adjacency List  (efficient for sparse graphs)
#   - Adjacency Matrix (efficient for dense graphs)
#
# Graph types:
#   - Directed / Undirected
#   - Weighted / Unweighted
#
# Algorithms covered:
#   - DFS (Depth-First Search)
#   - BFS (Breadth-First Search)
#   - Topological Sort (DAG)
#   - Shortest path — Dijkstra's algorithm
# =============================================================

from collections import deque
import heapq

# ---------------------------------------------------------
# Graph using Adjacency List
# ---------------------------------------------------------
print("=== Graph — Adjacency List ===")

class Graph:
    """
    Directed/undirected graph using adjacency list.
    For a weighted graph, store (neighbour, weight) tuples.
    """

    def __init__(self, directed=False):
        self.directed = directed
        self._adj = {}      # {node: [(neighbour, weight), ...]}

    def add_vertex(self, v):
        """Add a vertex to the graph."""
        if v not in self._adj:
            self._adj[v] = []

    def add_edge(self, u, v, weight=1):
        """Add an edge from u to v (and v to u if undirected)."""
        self.add_vertex(u)
        self.add_vertex(v)
        self._adj[u].append((v, weight))
        if not self.directed:
            self._adj[v].append((u, weight))

    def neighbours(self, v):
        """Return list of (neighbour, weight) for vertex v."""
        return self._adj.get(v, [])

    def vertices(self):
        return list(self._adj.keys())

    def edges(self):
        """Return all edges as (u, v, weight) tuples."""
        seen = set()
        result = []
        for u, nbrs in self._adj.items():
            for v, w in nbrs:
                edge = (min(u, v), max(u, v), w) if not self.directed else (u, v, w)
                if edge not in seen:
                    seen.add(edge)
                    result.append(edge)
        return result

    def __str__(self):
        lines = []
        for v, nbrs in sorted(self._adj.items()):
            nbr_str = ", ".join(f"{n}(w={w})" for n, w in nbrs)
            lines.append(f"  {v}: [{nbr_str}]")
        return "Graph(\n" + "\n".join(lines) + "\n)"


# Build an undirected weighted graph
g = Graph(directed=False)
edges = [
    ("A", "B", 4), ("A", "C", 2),
    ("B", "C", 5), ("B", "D", 10),
    ("C", "E", 3),
    ("D", "F", 11),
    ("E", "D", 4), ("E", "F", 7),
]
for u, v, w in edges:
    g.add_edge(u, v, w)

print(g)

# ---------------------------------------------------------
# DFS — Depth-First Search
# ---------------------------------------------------------
print("=== DFS (Depth-First Search) ===")

def dfs(graph, start, visited=None):
    """
    Recursive DFS from start node.

    Returns:
        list: Nodes visited in DFS order.
    """
    if visited is None:
        visited = set()
    visited.add(start)
    order = [start]
    for neighbour, _ in graph.neighbours(start):
        if neighbour not in visited:
            order += dfs(graph, neighbour, visited)
    return order


def dfs_iterative(graph, start):
    """Iterative DFS using an explicit stack."""
    visited = set()
    stack = [start]
    order = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbour, _ in reversed(graph.neighbours(node)):
                if neighbour not in visited:
                    stack.append(neighbour)
    return order


print(f"DFS recursive from A:  {dfs(g, 'A')}")
print(f"DFS iterative from A:  {dfs_iterative(g, 'A')}")

# ---------------------------------------------------------
# BFS — Breadth-First Search
# ---------------------------------------------------------
print("\n=== BFS (Breadth-First Search) ===")

def bfs(graph, start):
    """
    BFS from start node.

    Returns:
        list: Nodes visited in BFS order.
    """
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbour, _ in graph.neighbours(node):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return order


print(f"BFS from A: {bfs(g, 'A')}")

# ---------------------------------------------------------
# Topological Sort (Directed Acyclic Graph)
# ---------------------------------------------------------
print("\n=== Topological Sort (DAG) ===")

dag = Graph(directed=True)
deps = [
    ("code",   "test"),
    ("code",   "build"),
    ("test",   "deploy"),
    ("build",  "deploy"),
    ("deploy", "monitor"),
]
for u, v in deps:
    dag.add_edge(u, v)


def topological_sort(graph):
    """
    Kahn's algorithm (BFS-based) topological sort.

    Returns:
        list: Vertices in topological order, or [] if cycle detected.
    """
    in_degree = {v: 0 for v in graph.vertices()}
    for u in graph.vertices():
        for v, _ in graph.neighbours(u):
            in_degree[v] += 1

    queue = deque(v for v, d in in_degree.items() if d == 0)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbour, _ in graph.neighbours(node):
            in_degree[neighbour] -= 1
            if in_degree[neighbour] == 0:
                queue.append(neighbour)

    return order if len(order) == len(graph.vertices()) else []


topo = topological_sort(dag)
print(f"Topological order: {topo}")

# ---------------------------------------------------------
# Dijkstra's Shortest Path
# ---------------------------------------------------------
print("\n=== Dijkstra's Shortest Path ===")

def dijkstra(graph, start):
    """
    Dijkstra's algorithm: find shortest distances from start to all nodes.

    Time:  O((V + E) log V)
    Space: O(V)

    Args:
        graph: Graph with weighted edges.
        start: Source vertex.

    Returns:
        dict: {vertex: shortest_distance_from_start}
    """
    dist = {v: float('inf') for v in graph.vertices()}
    dist[start] = 0
    # Min-heap: (distance, vertex)
    heap = [(0, start)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue    # stale entry
        for v, weight in graph.neighbours(u):
            new_dist = dist[u] + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))

    return dist


distances = dijkstra(g, "A")
print("Shortest distances from A:")
for node, d in sorted(distances.items()):
    print(f"  A → {node}: {d}")
