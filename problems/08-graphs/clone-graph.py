"""
Problem: Clone Graph
LeetCode #: 133
Difficulty: Medium
URL: https://leetcode.com/problems/clone-graph/

Pattern: Graphs, DFS
Companies: Google, Amazon, Microsoft, Apple

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Recursively clone with visited check
- Time: O(n + e)  |  Space: O(n)

Optimal:
- DFS with HashMap to track cloned nodes
- Clone node, add to map, then clone all neighbors
- Key Insight: Map prevents infinite loops in cycles
- Time: O(n + e)  |  Space: O(n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"To clone a graph, we do DFS but maintain a HashMap to map original nodes
to cloned nodes. This prevents infinite loops. For each node, we create a
clone (if not already created), add it to the map, then recursively clone
all neighbors."

"""
from typing import Optional
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# ─── Brute Force ───
class BruteForceSolution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        """
        DFS clone with visited set.
        """
        if not node:
            return None
        
        visited = {}
        
        def dfs(original):
            if original in visited:
                return visited[original]
            
            clone = Node(original.val)
            visited[original] = clone
            
            for neighbor in original.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)


# ─── Optimal ───
class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        """
        DFS with HashMap - O(n+e) time.
        """
        if not node:
            return None
        
        # Map original node to clone
        clone_map = {}
        
        def dfs(original):
            # If already cloned, return the clone
            if original in clone_map:
                return clone_map[original]
            
            # Create clone
            clone = Node(original.val)
            clone_map[original] = clone
            
            # Clone neighbors
            for neighbor in original.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)


# ─── Helper functions ───
def graph_to_dict(node):
    """Convert graph to dict for comparison."""
    if not node:
        return {}
    visited = set()
    result = {}
    queue = deque([node])
    visited.add(id(node))
    
    while queue:
        n = queue.popleft()
        result[n.val] = sorted([neighbor.val for neighbor in n.neighbors])
        for neighbor in n.neighbors:
            if id(neighbor) not in visited:
                visited.add(id(neighbor))
                queue.append(neighbor)
    
    return result


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Simple 3-node graph
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.neighbors = [node2, node3]
    node2.neighbors = [node1]
    node3.neighbors = [node1]
    
    cloned = sol.cloneGraph(node1)
    assert cloned.val == 1
    assert cloned != node1
    assert len(cloned.neighbors) == 2
    
    # Test 2: Single node, self-loop
    single = Node(1)
    single.neighbors = [single]
    cloned_single = sol.cloneGraph(single)
    assert cloned_single.val == 1
    assert cloned_single.neighbors[0] == cloned_single
    
    # Test 3: Empty graph
    assert sol.cloneGraph(None) is None
    
    # Test 4: Single node, no neighbors
    node = Node(1)
    cloned_node = sol.cloneGraph(node)
    assert cloned_node.val == 1
    assert len(cloned_node.neighbors) == 0
    
    print("All tests passed!")
