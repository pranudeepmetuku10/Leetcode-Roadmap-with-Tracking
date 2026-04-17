"""
Problem: Maximum Depth of Binary Tree
LeetCode #: 104
Difficulty: Easy
URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Pattern: Trees, DFS
Companies: Google, Amazon, Microsoft, Apple

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Level order traversal, count levels
- Time: O(n)  |  Space: O(n)

Optimal:
- Recursive DFS: depth of node is 1 + max(left depth, right depth)
- Base case: null node has depth 0
- Key Insight: Height of tree is max depth from root
- Time: O(n)  |  Space: O(h)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"The maximum depth is the longest path from root to a leaf. We can find
this recursively: for each node, the depth is 1 plus the maximum of the
depths of its left and right subtrees. Base case is a null node which
has depth 0. Very straightforward O(n) solution."

"""
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ─── Brute Force ───
class BruteForceSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        BFS, count levels.
        """
        if not root:
            return 0
        
        max_depth = 0
        queue = deque([(root, 1)])
        
        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        
        return max_depth


# ─── Optimal ───
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Recursive DFS - O(n) time, O(h) space.
        """
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return 1 + max(left_depth, right_depth)


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Balanced tree
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
    assert sol.maxDepth(root1) == 3
    
    # Test 2: Single node
    root2 = TreeNode(1)
    assert sol.maxDepth(root2) == 1
    
    # Test 3: Empty tree
    assert sol.maxDepth(None) == 0
    
    # Test 4: Skewed tree
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.left.left = TreeNode(3)
    assert sol.maxDepth(root4) == 3
    
    print("All tests passed!")
