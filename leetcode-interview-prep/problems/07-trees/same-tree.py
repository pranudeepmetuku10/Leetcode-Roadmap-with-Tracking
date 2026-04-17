"""
Problem: Same Tree
LeetCode #: 100
Difficulty: Easy
URL: https://leetcode.com/problems/same-tree/

Pattern: Trees, DFS
Companies: Google, Amazon, Microsoft, Apple

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Convert both trees to lists, compare lists
- Time: O(n + m)  |  Space: O(n + m)

Optimal:
- Recursive comparison: check if nodes match, recurse on children
- Base cases: both null (true), one null (false), values differ (false)
- Key Insight: Simple structural comparison
- Time: O(n)  |  Space: O(h)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"To check if two trees are identical, we compare recursively. For each
node: if both are null, they match. If one is null or values differ,
they don't match. Otherwise, check if left and right subtrees match.
Base cases handle all edge cases elegantly."

"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ─── Brute Force ───
class BruteForceSolution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Convert to lists and compare.
        """
        def tree_to_list(root):
            if not root:
                return [None]
            return [root.val] + tree_to_list(root.left) + tree_to_list(root.right)
        
        return tree_to_list(p) == tree_to_list(q)


# ─── Optimal ───
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Recursive structural comparison - O(n) time.
        """
        # Both null
        if not p and not q:
            return True
        
        # One null or values differ
        if not p or not q or p.val != q.val:
            return False
        
        # Recurse on children
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Same trees
    p1 = TreeNode(1, TreeNode(2), TreeNode(3))
    q1 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert sol.isSameTree(p1, q1) == True
    
    # Test 2: Different structures
    p2 = TreeNode(1, TreeNode(2), None)
    q2 = TreeNode(1, None, TreeNode(2))
    assert sol.isSameTree(p2, q2) == False
    
    # Test 3: Different values
    p3 = TreeNode(1, TreeNode(2), TreeNode(1))
    q3 = TreeNode(1, TreeNode(1), TreeNode(2))
    assert sol.isSameTree(p3, q3) == False
    
    # Test 4: Both empty
    assert sol.isSameTree(None, None) == True
    
    print("All tests passed!")
