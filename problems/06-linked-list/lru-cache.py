"""
Problem: LRU Cache
LeetCode #: 146
Difficulty: Medium
URL: https://leetcode.com/problems/lru-cache/

Pattern: Linked List, Map
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Use a list to track order and a dict for values
- When evicting, search for least recently used - O(capacity)
- Time: O(capacity) for get/put  |  Space: O(capacity)

Optimal:
- Use a HashMap + Doubly Linked List
- HashMap maps key to node for O(1) access
- Doubly Linked List maintains LRU order
- Move accessed node to front, evict from back
- Key Insight: Combine two data structures for optimal performance
- Time: O(1) for get/put  |  Space: O(capacity)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"An LRU Cache needs fast access and fast eviction. We combine a HashMap for
O(1) lookup and a doubly linked list for ordering. The most recently used
node is at the front, least recently used at the back. On access, we move
the node to front. When full, we evict from the back."

"""


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


# ─── Brute Force ───
class BruteForceLRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = []  # Track access order
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move to end (most recent)
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) == self.capacity:
            # Evict least recently used
            lru_key = self.order.pop(0)
            del self.cache[lru_key]
        
        self.cache[key] = value
        self.order.append(key)


# ─── Optimal ───
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        
        # Dummy nodes to simplify insertion/deletion
        self.head = Node(0, 0)  # Most recently used
        self.tail = Node(0, 0)  # Least recently used
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove_node(self, node: Node) -> None:
        """Remove node from linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_to_head(self, node: Node) -> None:
        """Add node right after head (most recently used)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def get(self, key: int) -> int:
        """Get value and mark as recently used - O(1)."""
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove_node(node)
        self._add_to_head(node)
        return node.val
    
    def put(self, key: int, value: int) -> None:
        """Put key-value and mark as recently used - O(1)."""
        if key in self.cache:
            # Update existing key
            node = self.cache[key]
            node.val = value
            self._remove_node(node)
            self._add_to_head(node)
        else:
            # Add new key
            if len(self.cache) == self.capacity:
                # Evict least recently used (right before tail)
                lru_node = self.tail.prev
                self._remove_node(lru_node)
                del self.cache[lru_node.key]
            
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)


# ─── Test Cases ───
if __name__ == "__main__":
    # Test 1: Basic operations
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)  # Evicts key 2
    assert cache.get(2) == -1
    
    # Test 2: Update existing
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(1, 2)
    assert cache.get(1) == 2
    
    # Test 3: Capacity of 1
    cache = LRUCache(1)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == -1
    assert cache.get(2) == 2
    
    # Test 4: Multiple operations
    cache = LRUCache(3)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    assert cache.get(1) == 1
    cache.put(4, 4)  # Evicts key 2
    assert cache.get(2) == -1
    
    print("All tests passed!")
