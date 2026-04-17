"""
Problem: Kth Smallest Element in a BST
LeetCode #: 230
Difficulty: Medium
URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Pattern: Trees, BST, DFS
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Convert BST to sorted list (in-order traversal), return k-th element
- Time: O(n)  |  Space: O(n)

Optimal:
- In-order DFS gives sorted order in a BST
- Count nodes visited, return when count equals k
- Key Insight: BST in-order traversal yields sorted sequence
- Time: O(n) worst, O(k) if k is small  |  Space: O(h)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"In a BST, in-order traversal gives us elements in sorted order. We can
traverse in-order and keep a counter. When the counter reaches k, we've
found the kth smallest element. This is more efficient than building a
full sorted list if k is small relative to n."

"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ─── Brute Force ───
class BruteForceSolution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Build sorted list, return k-th element.
        """
        values = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return values[k - 1]


# ─── Optimal ───
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        In-order DFS with counter - O(n) worst, O(k) average.
        """
        self.count = 0
        self.result = None
        
        def inorder(node):
            if not node or self.result is not None:
                return
            
            # Visit left subtree
            inorder(node.left)
            
            # Visit current node
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            
            # Visit right subtree
            inorder(node.right)
        
        inorder(root)
        return self.result


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: k in middle
    root1 = TreeNode(3)
    root1.left = TreeNode(1, None, TreeNode(2))
    root1.right = TreeNode(4)
    assert sol.kthSmallest(root1, 1) == 1
    assert sol.kthSmallest(root1, 2) == 2
    assert sol.kthSmallest(root1, 3) == 3
    assert sol.kthSmallest(root1, 4) == 4
    
    # Test 2: k = 1 (smallest)
    root2 = TreeNode(3, TreeNode(1), TreeNode(4))
    assert sol.kthSmallest(root2, 1) == 1
    
    # Test 3: Single node
    root3 = TreeNode(1)
    assert sol.kthSmallest(root3, 1) == 1
    
    # Test 4: Skewed tree
    root4 = TreeNode(1)
    root4.right = TreeNode(2)
    root4.right.right = TreeNode(3)
    assert sol.kthSmallest(root4, 2) == 2
    
    print("All tests passed!")
