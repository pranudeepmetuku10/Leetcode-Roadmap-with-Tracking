"""
Problem: Serialize and Deserialize Binary Tree
LeetCode #: 297
Difficulty: Hard
URL: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Pattern: Trees, BFS/DFS
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Serialize using level order, deserialize by rebuilding level by level
- Time: O(n) both ways  |  Space: O(n)

Optimal:
- Pre-order DFS serialization with null markers
- Deserialize by rebuilding tree from pre-order sequence
- Key Insight: Pre-order with nulls uniquely encodes tree structure
- Time: O(n) both ways  |  Space: O(n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"To serialize/deserialize a tree, we need to encode the structure completely.
Using pre-order DFS with null markers works well: we visit node, then left
subtree, then right subtree, using a marker for nulls. To deserialize, we
reverse the process: build the tree from this pre-order sequence."

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
    def serialize(self, root: Optional[TreeNode]) -> str:
        """BFS serialization."""
        if not root:
            return ""
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("N")
        return ",".join(result)
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """BFS deserialization."""
        if not data:
            return None
        nodes = data.split(",")
        if nodes[0] == "N":
            return None
        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        i = 1
        while queue and i < len(nodes):
            node = queue.popleft()
            if i < len(nodes) and nodes[i] != "N":
                node.left = TreeNode(int(nodes[i]))
                queue.append(node.left)
            i += 1
            if i < len(nodes) and nodes[i] != "N":
                node.right = TreeNode(int(nodes[i]))
                queue.append(node.right)
            i += 1
        return root


# ─── Optimal ───
class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Pre-order DFS serialization with nulls."""
        result = []
        
        def dfs(node):
            if not node:
                result.append("N")
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(result)
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Rebuild tree from pre-order sequence."""
        nodes = data.split(",")
        self.idx = 0
        
        def dfs():
            if self.idx >= len(nodes):
                return None
            if nodes[self.idx] == "N":
                self.idx += 1
                return None
            node = TreeNode(int(nodes[self.idx]))
            self.idx += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()


# ─── Test Cases ───
if __name__ == "__main__":
    codec = Codec()
    
    # Test 1: Balanced tree
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    serialized1 = codec.serialize(root1)
    deserialized1 = codec.deserialize(serialized1)
    assert deserialized1.val == 1
    assert deserialized1.left.val == 2
    assert deserialized1.right.val == 3
    
    # Test 2: Skewed tree
    root2 = TreeNode(1)
    root2.left = TreeNode(2, None, TreeNode(3))
    serialized2 = codec.serialize(root2)
    deserialized2 = codec.deserialize(serialized2)
    assert deserialized2.val == 1
    assert deserialized2.left.val == 2
    assert deserialized2.left.right.val == 3
    
    # Test 3: Empty tree
    serialized3 = codec.serialize(None)
    deserialized3 = codec.deserialize(serialized3)
    assert deserialized3 is None
    
    # Test 4: Single node
    root4 = TreeNode(1)
    serialized4 = codec.serialize(root4)
    deserialized4 = codec.deserialize(serialized4)
    assert deserialized4.val == 1
    
    print("All tests passed!")
