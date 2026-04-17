# Binary Search

## Pattern Overview

Binary Search is used to efficiently search in sorted data by repeatedly dividing the search space in half. It's fundamental for optimization problems.

## When to Recognize This Pattern

**Trigger words:**
- "Sorted array"
- "Find/Search a value"
- "Minimize/maximize" (with sorted property)
- "Left-most/right-most"
- "Condition-based search"

## Template/Pseudocode

```python
# Classic binary search
left, right = 0, len(arr) - 1

while left <= right:
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

return -1  # Not found

# Optimization problem binary search
def can_achieve(value):
    # Check if we can achieve target with this value
    return True/False

left, right = 0, max_value
while left < right:
    mid = (left + right) // 2
    if can_achieve(mid):
        right = mid  # Try to find smaller
    else:
        left = mid + 1
```

## Time & Space Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Basic binary search | O(log n) | O(1) |
| With modified array | O(log n) | O(1) |

## Common Mistakes to Avoid

1. **Infinite loops** — Use `left < right` vs `left <= right` correctly
2. **Integer overflow** — Use `mid = left + (right - left) // 2` not `(left + right) // 2`
3. **Off-by-one errors** — In boundary conditions
4. **Forgetting sorted assumption** — Binary search ONLY works on sorted data
5. **Wrong search condition** — Know if finding exact match, left-most, or right-most

## Problems in This Section

| Problem | Difficulty | LeetCode |
|---------|-----------|----------|
| Binary Search | Easy | 704 |
| Search 2D Matrix | Medium | 74 |
| Koko Eating Bananas | Medium | 875 |
| Find Min in Rotated Array | Medium | 153 |
| Search Rotated Sorted Array | Medium | 33 |

## Key Insights

- **Always halve search space** — Guaranteed O(log n)
- **Optimization problems** — Use binary search on answer value
- **Rotated arrays** — Identify which half is sorted, search that
- **Left-most vs right-most** — Different boundary conditions  
- **Integer overflow** — Even in Python, good habit

## Related Patterns

- **Two Pointers** — Linear but simpler logic
- **HashMap** — For unsorted data  
- **Greedy** — Often combined with binary search
