# Linked List

## Pattern Overview

Linked List problems involve manipulating nodes and pointers. Common themes are reversing, merging, cycle detection, and rearrangement.

## When to Recognize This Pattern

**Trigger words:**
- "Reverse linked list"
- "Merge two lists"
- "Detect cycle"
- "Reorder/rearrange"
- "Middle element"
- "Kth node"

## Template/Pseudocode

```python
# ListNode definition
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Pattern 1: Two pointers (slow/fast)
slow, fast = head, head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
# slow is now at middle

# Pattern 2: Reverse linked list
prev, curr = None, head
while curr:
    next_temp = curr.next
    curr.next = prev
    prev = curr
    curr = next_temp
return prev
```

## Time & Space Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Traversal | O(n) | O(1) |
| Reversal | O(n) | O(1) |
| With recursion | O(n) | O(n) |

## Common Mistakes to Avoid

1. **Losing references** — Save next pointer before modifying
2. **Infinite loops** — Make sure curr moves forward
3. **Null pointer exceptions** — Check `if node` before accessing `node.next`
4. **Off-by-one in cycles** — Count carefully or use runner technique
5. **Memory leaks** — Clean up unused references in languages that require it

## Problems in This Section

| Problem | Difficulty | LeetCode |
|---------|-----------|----------|
| Reverse Linked List | Easy | 206 |
| Merge Two Sorted Lists | Easy | 21 |
| Linked List Cycle | Easy | 141 |
| Reorder List | Medium | 143 |
| LRU Cache | Medium | 146 |

## Key Insights

- **Draw it out** — Linked lists are hard to visualize; put it on paper
- **Slow & fast pointers** — Find middle, detect cycles
- **Reverse carefully** — Track three pointers: prev, curr, next
- **Sentinel nodes** — Dummy node at head simplifies edge cases
- **Two-pass approach** — First pass to find details, second to execute

## Related Patterns

- **Stack** — For reverse or paired processing
- **Hash Table** — For cycle detection or caching
- **Recursion** — Elegant for reversal but uses O(n) space
