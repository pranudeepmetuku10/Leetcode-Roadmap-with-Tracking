"""
Problem: Invert Binary Tree
LeetCode #: 226
Difficulty: Easy
URL: https://leetcode.com/problems/invert-binary-tree/

Pattern: Trees, DFS
Companies: Google, Amazon, Microsoft, Apple

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Queue-based level order traversal, swap children at each node
- Time: O(n)  |  Space: O(n)

Optimal:
- Recursive DFS: swap left and right children, then recurse
- Base case: null nodes return null
- Key Insight: Simple recursion elegantly inverts tree
- Time: O(n)  |  Space: O(h) where h is height

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"To invert a tree, we need to swap left and right children at each node.
We can do this recursively: for each node, swap its children, then
recursively invert the left and right subtrees. The base case is when
we hit a null node. Very clean O(n) solution."

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        BFS with queue, swap at each node.
        """
        if not root:
            return None
        
        queue = deque([root])
        while queue:
            node = queue.popleft()
            # Swap children
            node.left, node.right = node.right, node.left
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root


# ─── Optimal ───
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Recursive inversion - O(n) time.
        """
        if not root:
            return None
        
        # Swap children
        root.left, root.right = root.right, root.left
        
        # Recurse
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root


# ─── Helper functions ───
def tree_to_list(root):
    """Level order traversal for testing."""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    return result


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Balanced tree
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)
    result1 = sol.invertTree(root1)
    assert result1.val == 2
    assert result1.left.val == 3
    assert result1.right.val == 1
    
    # Test 2: Single node
    root2 = TreeNode(1)
    result2 = sol.invertTree(root2)
    assert result2.val == 1
    
    # Test 3: Empty tree
    result3 = sol.invertTree(None)
    assert result3 is None
    
    # Test 4: Unbalanced tree
    root4 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    result4 = sol.invertTree(root4)
    assert result4.left.val == 7
    assert result4.right.val == 2
    
    print("All tests passed!")
