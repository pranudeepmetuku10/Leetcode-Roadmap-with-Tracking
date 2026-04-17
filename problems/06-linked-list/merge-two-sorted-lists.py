"""
Problem: Merge Two Sorted Lists
LeetCode #: 21
Difficulty: Easy
URL: https://leetcode.com/problems/merge-two-sorted-lists/

Pattern: Linked List
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Combine both lists, convert to list, sort, rebuild
- Time: O((m+n)log(m+n))  |  Space: O(m+n)

Optimal:
- Use two pointers, one for each list
- Compare values and append the smaller to result
- Move the pointer of the list we took from
- When one list is exhausted, append the rest of the other
- Key Insight: Both lists are already sorted
- Time: O(m+n)  |  Space: O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Both input lists are already sorted. We can merge them in a single pass by
comparing the heads of both lists and taking the smaller value each time.
When one list is exhausted, we append the entire remainder of the other
list. This is O(m+n) time with O(1) extra space."

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ─── Brute Force ───
class BruteForceSolution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Collect all values, sort, rebuild.
        """
        values = []
        
        # Collect from list1
        current = list1
        while current:
            values.append(current.val)
            current = current.next
        
        # Collect from list2
        current = list2
        while current:
            values.append(current.val)
            current = current.next
        
        # Sort and rebuild
        values.sort()
        if not values:
            return None
        
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        
        return head


# ─── Optimal ───
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge by comparing and linking - O(m+n) time.
        """
        # Dummy node to simplify logic
        dummy = ListNode(0)
        current = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Append remainder of whichever list has elements left
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        return dummy.next


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
    
    # Test 1: Both non-empty
    list1 = list_to_linked_list([1, 2, 4])
    list2 = list_to_linked_list([1, 3, 4])
    result = sol.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [1, 1, 2, 3, 4, 4]
    
    # Test 2: One empty
    list1 = list_to_linked_list([])
    list2 = list_to_linked_list([0])
    result = sol.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [0]
    
    # Test 3: Both empty
    result = sol.mergeTwoLists(None, None)
    assert linked_list_to_list(result) == []
    
    # Test 4: Different lengths
    list1 = list_to_linked_list([1, 2])
    list2 = list_to_linked_list([3, 4, 5, 6])
    result = sol.mergeTwoLists(list1, list2)
    assert linked_list_to_list(result) == [1, 2, 3, 4, 5, 6]
    
    print("All tests passed!")
