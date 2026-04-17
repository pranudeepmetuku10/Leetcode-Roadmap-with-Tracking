"""
Problem: Reorder List
LeetCode #: 143
Difficulty: Medium
URL: https://leetcode.com/problems/reorder-list/

Pattern: Linked List
Companies: Google, Amazon, Microsoft, Meta, Apple

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Convert list to array, reorder array, rebuild linked list
- Time: O(n)  |  Space: O(n)

Optimal:
- Find middle of list using slow/fast pointers
- Reverse the second half
- Merge the two halves in alternating fashion
- Key Insight: Combine multiple pointer techniques
- Time: O(n)  |  Space: O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"We need to reorder the list to L0->Ln->L1->L(n-1)->... We break this into
steps: first, find the middle using slow/fast pointers. Then, reverse the
second half. Finally, merge the two halves in alternating fashion. This
requires careful pointer manipulation but O(n) time with O(1) space."

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ─── Brute Force ───
class BruteForceSolution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Convert to array, reorder, rebuild.
        """
        # Collect values
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        
        # Reorder
        reordered = []
        left, right = 0, len(values) - 1
        while left <= right:
            reordered.append(values[left])
            if left != right:
                reordered.append(values[right])
            left += 1
            right -= 1
        
        # Rebuild the list
        current = head
        for val in reordered:
            current.val = val
            current = current.next


# ─── Optimal ───
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Find middle, reverse second half, merge - O(n) time, O(1) space.
        """
        if not head or not head.next:
            return
        
        # Find the middle using slow/fast pointers
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half
        second_head = slow.next
        slow.next = None
        
        prev = None
        current = second_head
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        # Merge the two halves
        first = head
        second = prev
        while second:  # second will be shorter or equal
            first_next = first.next
            second_next = second.next
            
            first.next = second
            second.next = first_next
            
            first = first_next
            second = second_next


# ─── Helper functions ───
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
    
    # Test 1: 5 elements
    head1 = list_to_linked_list([1, 2, 3, 4, 5])
    sol.reorderList(head1)
    assert linked_list_to_list(head1) == [1, 5, 2, 4, 3]
    
    # Test 2: 4 elements
    head2 = list_to_linked_list([1, 2, 3, 4])
    sol.reorderList(head2)
    assert linked_list_to_list(head2) == [1, 4, 2, 3]
    
    # Test 3: 2 elements
    head3 = list_to_linked_list([1, 2])
    sol.reorderList(head3)
    assert linked_list_to_list(head3) == [1, 2]
    
    # Test 4: 1 element
    head4 = list_to_linked_list([1])
    sol.reorderList(head4)
    assert linked_list_to_list(head4) == [1]
    
    print("All tests passed!")
