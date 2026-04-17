# Graphs

## Pattern Overview

Graph problems involve finding paths, connectivity, topological ordering, and cycles. Key techniques are DFS, BFS, and Union-Find.

## When to Recognize This Pattern

**Trigger words:**
- "Connected components"
- "Path from X to Y"
- "Course prerequisites"
- "Social network"
- "Island/Region"
- "Topological order"

## Template/Pseudocode

```python
# DFS - Recursive
visited = set()
def dfs(node):
    if node in visited:
        return
    visited.add(node)
    for neighbor in graph[node]:
        dfs(neighbor)

# BFS - Queue based
from collections import deque
visited = {start}
queue = deque([start])
while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

# Topological Sort (Kahn's algorithm)
in_degree = {node: 0 for node in graph}
for node in graph:
    for neighbor in graph[node]:
        in_degree[neighbor] += 1

queue = deque([node for node in in_degree if in_degree[node] == 0])
result = []
while queue:
    node = queue.popleft()
    result.append(node)
    for neighbor in graph[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)
```

## Time & Space Complexity

| Operation | Time | Space |
|-----------|------|-------|
| DFS | O(V + E) | O(V) |
| BFS | O(V + E) | O(V) |
| Topological | O(V + E) | O(V) |

## Common Mistakes to Avoid

1. **Forgetting visited set** — Causes infinite loops in cycles
2. **Directed vs undirected** — Different adjacency list structure
3. **Building graph incorrectly** — Double edges for undirected
4. **Not handling disconnected components** — May need multiple DFS calls
5. **Stack overflow** — Use BFS or iterative for large graphs

## Problems in This Section

| Problem | Difficulty | LeetCode |
|---------|-----------|----------|
| Number of Islands | Medium | 200 |
| Clone Graph | Medium | 133 |
| Pacific Atlantic Water Flow | Medium | 417 |
| Course Schedule | Medium | 207 |
| Course Schedule II | Medium | 210 |
| Rotting Oranges | Medium | 994 |

## Key Insights

- **Adjacency list vs matrix** — List for sparse, matrix for dense
- **Connected components** — DFS/BFS identifies clusters
- **Cycle detection** — In directed graphs, use coloring
- **Shortest path** — BFS for unweighted, Dijkstra for weighted
- **Topological sort** — Only for DAGs (directed acyclic graphs)

## Related Patterns

- **Union-Find** — Alternative for connected components
- **Tree/DFS** — Tree is special case of DAG
- **Dijkstra/Bellman-Ford** — For weighted graph shortest path
