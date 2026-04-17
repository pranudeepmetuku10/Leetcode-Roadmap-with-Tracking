"""
Problem: Linked List Cycle
LeetCode #: 141
Difficulty: Easy
URL: https://leetcode.com/problems/linked-list-cycle/

Pattern: Linked List
Companies: Google, Amazon, Microsoft, Apple

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Use a set to track visited nodes
- If we visit a node twice, there's a cycle
- Time: O(n)  |  Space: O(n)

Optimal:
- Floyd's Cycle Detection (Tortoise and Hare)
- Use two pointers: slow (1 step) and fast (2 steps)
- If they meet, there's a cycle
- Key Insight: In a cycle, fast pointer must catch slow pointer
- Time: O(n)  |  Space: O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"To detect a cycle with O(1) space, we use Floyd's algorithm: two pointers,
one slow (moves 1 step) and one fast (moves 2 steps). If there's a cycle,
the fast pointer will eventually catch up to the slow pointer. If the fast
pointer reaches the end, there's no cycle. This is the optimal solution."

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ─── Brute Force ───
class BruteForceSolution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Use a set to track visited nodes - O(n) space.
        """
        visited = set()
        current = head
        
        while current:
            if id(current) in visited:
                return True
            visited.add(id(current))
            current = current.next
        
        return False


# ─── Optimal ───
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Floyd's cycle detection - O(1) space.
        """
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        while slow != fast:
            # If fast reaches the end, no cycle
            if not fast or not fast.next:
                return False
            
            slow = slow.next
            fast = fast.next.next
        
        return True


# ─── Helper function ───
def list_to_linked_list_with_cycle(arr, cycle_pos):
    """Create a linked list with an optional cycle."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    cycle_node = None
    
    for i, val in enumerate(arr[1:], 1):
        current.next = ListNode(val)
        current = current.next
        if i == cycle_pos:
            cycle_node = current
    
    # Create cycle if specified
    if cycle_pos >= 0 and cycle_node:
        current.next = cycle_node
    
    return head


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Cycle exists
    head1 = list_to_linked_list_with_cycle([3, 2, 0, -4], 1)
    assert sol.hasCycle(head1) == True
    
    # Test 2: No cycle
    head2 = list_to_linked_list_with_cycle([1, 2], -1)
    assert sol.hasCycle(head2) == False
    
    # Test 3: Single node, no cycle
    head3 = ListNode(1)
    assert sol.hasCycle(head3) == False
    
    # Test 4: Single node with cycle
    head4 = ListNode(1)
    head4.next = head4
    assert sol.hasCycle(head4) == True
    
    print("All tests passed!")
