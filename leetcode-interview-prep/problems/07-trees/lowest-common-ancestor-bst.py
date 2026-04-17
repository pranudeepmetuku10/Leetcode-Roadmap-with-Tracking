"""
Problem: Lowest Common Ancestor of a Binary Search Tree
LeetCode #: 235
Difficulty: Medium
URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Pattern: Trees, BST
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Find paths to both nodes using DFS, find common ancestor
- Time: O(n)  |  Space: O(h)

Optimal:
- Use BST property: if both values are less than root, go left
- If both greater, go right; otherwise root is LCA
- Key Insight: BST property eliminates need for search
- Time: O(log n) average, O(n) worst  |  Space: O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"In a BST, we can use the ordering property. If both p and q are less than
the current node, their LCA must be in the left subtree. If both are
greater, it's in the right subtree. Otherwise, the current node is the LCA
because p and q are on different sides or at this node."

"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ─── Brute Force ───
class BruteForceSolution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Find paths, compare - O(n) time.
        """
        def find_path(node, target, path):
            if not node:
                return None
            path.append(node)
            if node.val == target.val:
                return path[:]
            if node.left:
                result = find_path(node.left, target, path)
                if result:
                    return result
            if node.right:
                result = find_path(node.right, target, path)
                if result:
                    return result
            path.pop()
            return None
        
        path_p = find_path(root, p, [])
        path_q = find_path(root, q, [])
        
        lca = None
        for i in range(min(len(path_p), len(path_q))):
            if path_p[i].val == path_q[i].val:
                lca = path_p[i]
        return lca


# ─── Optimal ───
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Use BST property - O(log n) average time.
        """
        current = root
        
        while current:
            if p.val < current.val and q.val < current.val:
                # Both less than current, go left
                current = current.left
            elif p.val > current.val and q.val > current.val:
                # Both greater than current, go right
                current = current.right
            else:
                # Nodes are on different sides or one is current
                return current


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Basic case
    root = TreeNode(6)
    root.left = TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5)))
    root.right = TreeNode(8, TreeNode(7), TreeNode(9))
    p = root.left  # node 2
    q = root.left.right  # node 4
    assert sol.lowestCommonAncestor(root, p, q).val == 2
    
    # Test 2: LCA is root
    p = root.left  # node 2
    q = root.right  # node 8
    assert sol.lowestCommonAncestor(root, p, q).val == 6
    
    # Test 3: One node is ancestor of other
    p = root.left  # node 2
    q = root.left.right.left  # node 3
    assert sol.lowestCommonAncestor(root, p, q).val == 2
    
    # Test 4: LCA is on right side
    p = root.right.left  # node 7
    q = root.right  # node 8
    assert sol.lowestCommonAncestor(root, p, q).val == 8
    
    print("All tests passed!")
