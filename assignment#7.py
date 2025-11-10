class DFSTopologicalSort:
    def __init__(self, graph: list[list[int]]):
        """
        Initialize the class with the graph.

        """
        self.graph = graph
        self.N = len(graph)  # Number of vertices
        self.enter = [0] * self.N  # Entry times
        self.exit = [0] * self.N  # Exit times
        self.marked = [False] * self.N  # Visited markers
        self.time = 0  # Global time counter for DFS
        self.NO_EDGE = graph[0][0]  # Value indicating no edge in adjacency matrix

    def _dfs(self, v: int):
        """
        Recursive DFS helper that updates entry and exit times.

        """
        self.enter[v] = self.time  # Record entry time
        self.time += 1
        self.marked[v] = True  # Mark vertex as visited

        # Visit all neighbors of v
        for w in range(self.N):
            if self.graph[v][w] != self.NO_EDGE and not self.marked[w]:
                self._dfs(w)  # Recursive call for unvisited neighbors

        self.exit[v] = self.time  # Record exit time
        self.time += 1

    def compute_topological_order(self) -> list[int]:
        """
        Compute the topological order of the DAG using DFS stack timings.

        """
        # Run DFS from every unvisited vertex
        for v in range(self.N):
            if not self.marked[v]:
                self._dfs(v)

        # Sort vertices by descending exit time to get topological order
        topo_order = sorted(range(self.N), key=lambda x: self.exit[x], reverse=True)
        return topo_order

    def get_stack_times(self) -> tuple[list[int], list[int]]:
        """
        Return the entry and exit times of all vertices.

        """
        return self.enter, self.exit


# TESTING PURPOSES
G1 = [
    [0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
]

G2 = [
    [0, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 1, 2, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
]

# Analyze G1
print("===== Graph G1 =====")
dfs_sort1 = DFSTopologicalSort(G1)
order1 = dfs_sort1.compute_topological_order()
enter1, exit1 = dfs_sort1.get_stack_times()

print("Topological Order:", order1)
print("\nVertex | Enter | Exit | Duration (Exit - Enter)")
print("---------------------------------------------")
for v in range(len(G1)):
    print(
        f"   {v:>2}   |  {enter1[v]:>4}  |  {exit1[v]:>4}  |     {exit1[v] - enter1[v]:>4}"
    )

# Analyze G2
print("\n===== Graph G2 =====")
dfs_sort2 = DFSTopologicalSort(G2)
order2 = dfs_sort2.compute_topological_order()
enter2, exit2 = dfs_sort2.get_stack_times()

print("Topological Order:", order2)
print("\nVertex | Enter | Exit | Duration (Exit - Enter)")
print("---------------------------------------------")
for v in range(len(G2)):
    print(
        f"   {v:>2}   |  {enter2[v]:>4}  |  {exit2[v]:>4}  |     {exit2[v] - enter2[v]:>4}"
    )
