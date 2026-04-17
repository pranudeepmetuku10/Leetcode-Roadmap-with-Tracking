"""
Problem: Binary Tree Right Side View
LeetCode #: 199
Difficulty: Medium
URL: https://leetcode.com/problems/binary-tree-right-side-view/

Pattern: Trees, BFS
Companies: Google, Amazon, Microsoft, Apple

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Level order traversal, take rightmost node of each level
- Time: O(n)  |  Space: O(n)

Optimal:
- Right-first DFS: visit right child before left
- Track maximum depth seen so far
- Add node value when encountering a new depth level
- Key Insight: Right-first DFS visits right side nodes first at each level
- Time: O(n)  |  Space: O(h)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Right side view shows the rightmost node at each depth level. We can use
BFS and take the last node from each level. Or we can use DFS, visiting
right children before left children, and tracking the maximum depth seen.
When we see a new depth, we record that node."

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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        BFS level order, take rightmost of each level.
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            rightmost = None
            
            for _ in range(level_size):
                node = queue.popleft()
                rightmost = node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(rightmost)
        
        return result


# ─── Optimal ───
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Right-first DFS with depth tracking - O(n) time.
        """
        result = []
        max_depth = -1
        
        def dfs(node, depth):
            nonlocal max_depth
            if not node:
                return
            
            # When we reach a new depth level, record this node
            if depth > max_depth:
                result.append(node.val)
                max_depth = depth
            
            # Visit right first, then left
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return result


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Balanced tree
    root1 = TreeNode(1)
    root1.left = TreeNode(2, None, TreeNode(5))
    root1.right = TreeNode(3, None, TreeNode(4))
    assert sol.rightSideView(root1) == [1, 3, 4]
    
    # Test 2: Left-skewed tree
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.left.left = TreeNode(3)
    assert sol.rightSideView(root2) == [1, 2, 3]
    
    # Test 3: Single node
    root3 = TreeNode(1)
    assert sol.rightSideView(root3) == [1]
    
    # Test 4: Empty tree
    assert sol.rightSideView(None) == []
    
    print("All tests passed!")
