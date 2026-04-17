# Trees

## Pattern Overview

Tree problems involve traversal (DFS/BFS), path finding, and tree manipulation. Understanding node relationships and tree properties is key.

## When to Recognize This Pattern

**Trigger words:**
- "Binary tree"
- "Path from root to..."
- "Lowest common ancestor"
- "Invert/mirror"
- "Level-order traversal"
- "Validate BST"

## Template/Pseudocode

```python
# DFS - Recursive
def dfs(node):
    if not node:
        return base_case
    
    left = dfs(node.left)
    right = dfs(node.right)
    
    return combine(left, right, node.val)

# DFS - Iterative
stack = [root]
while stack:
    node = stack.pop()
    if node:
        process(node)
        stack.append(node.right)
        stack.append(node.left)

# BFS - Level order
from collections import deque
queue = deque([root])
while queue:
    level_size = len(queue)
    for _ in range(level_size):
        node = queue.popleft()
        process(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

## Time & Space Complexity

| Operation | Time | Space |
|-----------|------|-------|
| DFS | O(n) | O(h) height |
| BFS | O(n) | O(w) width |
| Balanced tree | O(n) | O(log n) |

## Common Mistakes to Avoid

1. **Base case forgotten** — Always check `if not node`
2. **Modifying tree in place** — Be careful, sometimes not allowed
3. **Height vs depth** — Know the difference
4. **In-order traversal order** — left, node, right for BST
5. **Stack overflow** — Deep trees may cause recursion depth exceeded

## Problems in This Section

| Problem | Difficulty | LeetCode |
|---------|-----------|----------|
| Invert Binary Tree | Easy | 226 |
| Max Depth Binary Tree | Easy | 104 |
| Same Tree | Easy | 100 |
| Lowest Common Ancestor BST | Medium | 235 |
| Level Order Traversal | Medium | 102 |
| Validate BST | Medium | 98 |
| Kth Smallest BST | Medium | 230 |
| Right Side View | Medium | 199 |
| Serialize/Deserialize | Hard | 297 |

## Key Insights

- **Recursion natural fit** — Trees are recursive structures
- **Traversal order matters** — Pre, in, post order give different info
- **BST property** — Left < node < right (critical for optimization)
- **Balance matters** — O(n) if degenerate, O(log n) if balanced
- **Sentinel nodes** — Dummy node simplifies logic

## Related Patterns

- **Graph BFS/DFS** — Tree is special case of graph
- **Stack & Queue** — Iterative traversal implementations
- **Recursion** — Natural for tree problems
