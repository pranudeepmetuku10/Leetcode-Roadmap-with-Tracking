"""
Problem: Reverse Linked List
LeetCode #: 206
Difficulty: Easy
URL: https://leetcode.com/problems/reverse-linked-list/

Pattern: Linked List
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Store values in a list, reverse the list, reconstruct linked list
- Time: O(n)  |  Space: O(n)

Optimal:
- Iterative: maintain prev, current, next pointers
- Reverse the link direction as we traverse
- Move pointers forward and repeat
- Key Insight: Careful pointer manipulation avoids extra space
- Time: O(n)  |  Space: O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"To reverse a linked list, we need to reverse the direction of all pointers.
We maintain three pointers: prev, current, and next. For each node, we
reverse its link to point to the previous node instead of the next, then
move all pointers forward. This is O(n) time with O(1) space."

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ─── Brute Force ───
class BruteForceSolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Use a list to store values, then rebuild.
        """
        if not head:
            return None
        
        # Collect values
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        
        # Rebuild in reverse
        values.reverse()
        new_head = ListNode(values[0])
        current = new_head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        
        return new_head


# ─── Optimal ───
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iterative reversal with O(1) space.
        """
        prev = None
        current = head
        
        while current:
            # Store next before we change the link
            next_temp = current.next
            # Reverse the link
            current.next = prev
            # Move pointers forward
            prev = current
            current = next_temp
        
        return prev


# ─── Helper function ───
def list_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Normal list
    head1 = list_to_linked_list([1, 2, 3, 4, 5])
    result1 = sol.reverseList(head1)
    assert linked_list_to_list(result1) == [5, 4, 3, 2, 1]
    
    # Test 2: Two elements
    head2 = list_to_linked_list([1, 2])
    result2 = sol.reverseList(head2)
    assert linked_list_to_list(result2) == [2, 1]
    
    # Test 3: Single element
    head3 = list_to_linked_list([1])
    result3 = sol.reverseList(head3)
    assert linked_list_to_list(result3) == [1]
    
    # Test 4: Empty list
    result4 = sol.reverseList(None)
    assert result4 is None
    
    print("All tests passed!")
