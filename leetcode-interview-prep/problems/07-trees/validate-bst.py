"""
Problem: Validate Binary Search Tree
LeetCode #: 98
Difficulty: Medium
URL: https://leetcode.com/problems/validate-binary-search-tree/

Pattern: Trees, BST, DFS
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- For each node, verify all values in left subtree < node < right subtree
- Time: O(n²)  |  Space: O(h)

Optimal:
- DFS with min/max bounds for each subtree
- Left subtree: values must be < parent
- Right subtree: values must be > parent
- Key Insight: Track valid range as we traverse
- Time: O(n)  |  Space: O(h)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"To validate a BST, we need to ensure that every node respects the BST
property with respect to its entire ancestors, not just its parent. We
use DFS with bounds: as we go left, update the upper bound; as we go
right, update the lower bound. Check if node value is within bounds."

"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ─── Brute Force ───
class BruteForceSolution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Check all values in subtrees - O(n²) time.
        """
        def get_min_max(node):
            if not node:
                return float('inf'), float('-inf')
            
            left_min, left_max = get_min_max(node.left)
            right_min, right_max = get_min_max(node.right)
            
            min_val = min(node.val, left_min, right_min)
            max_val = max(node.val, left_max, right_max)
            return min_val, max_val
        
        def is_valid(node):
            if not node:
                return True
            
            left_min, left_max = get_min_max(node.left)
            right_min, right_max = get_min_max(node.right)
            
            if node.left and left_max >= node.val:
                return False
            if node.right and right_min <= node.val:
                return False
            
            return is_valid(node.left) and is_valid(node.right)
        
        return is_valid(root)


# ─── Optimal ───
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        DFS with min/max bounds - O(n) time.
        """
        def validate(node, min_val, max_val):
            if not node:
                return True
            
            # Check if node is within bounds
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Left subtree: values must be < node.val
            # Right subtree: values must be > node.val
            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))
        
        return validate(root, float('-inf'), float('inf'))


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Valid BST
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)
    assert sol.isValidBST(root1) == True
    
    # Test 2: Invalid BST
    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4, TreeNode(3), TreeNode(6))
    assert sol.isValidBST(root2) == False
    
    # Test 3: Single node
    root3 = TreeNode(1)
    assert sol.isValidBST(root3) == True
    
    # Test 4: Violation in subtree
    root4 = TreeNode(10)
    root4.left = TreeNode(5)
    root4.right = TreeNode(15, TreeNode(6), TreeNode(20))
    assert sol.isValidBST(root4) == False
    
    print("All tests passed!")
