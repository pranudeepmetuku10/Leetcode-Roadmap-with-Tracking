"""
Problem: Binary Tree Level Order Traversal
LeetCode #: 102
Difficulty: Medium
URL: https://leetcode.com/problems/binary-tree-level-order-traversal/

Pattern: Trees, BFS
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- DFS to find depth of each node, group by depth
- Time: O(n log n)  |  Space: O(n)

Optimal:
- BFS with queue, process nodes level by level
- Add nodes to result grouped by level
- Key Insight: Queue naturally processes level order
- Time: O(n)  |  Space: O(n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Level order traversal is a BFS task. We use a queue and process nodes
level by level. For each level, we enqueue all children and record all
nodes at that level before moving to the next. This naturally gives us
the level-by-level structure."

"""
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ─── Brute Force ───
class BruteForceSolution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        DFS to find depths, group by depth.
        """
        if not root:
            return []
        
        result = {}
        
        def dfs(node, depth):
            if not node:
                return
            if depth not in result:
                result[depth] = []
            result[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return [result[i] for i in sorted(result.keys())]


# ─── Optimal ───
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        BFS with queue - O(n) time.
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            level_values = []
            
            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level_values)
        
        return result


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Balanced tree
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
    assert sol.levelOrder(root1) == [[3], [9, 20], [15, 7]]
    
    # Test 2: Single node
    root2 = TreeNode(1)
    assert sol.levelOrder(root2) == [[1]]
    
    # Test 3: Empty tree
    assert sol.levelOrder(None) == []
    
    # Test 4: Right-skewed tree
    root4 = TreeNode(1)
    root4.right = TreeNode(2)
    root4.right.right = TreeNode(3)
    assert sol.levelOrder(root4) == [[1], [2], [3]]
    
    print("All tests passed!")
