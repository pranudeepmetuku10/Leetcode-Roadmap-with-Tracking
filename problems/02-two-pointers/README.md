# Two Pointers

## Pattern Overview

The Two Pointers pattern uses two indices moving through data, typically used for sorted arrays. This pattern is extremely efficient for finding pairs, validating structures, and partitioning data.

## When to Recognize This Pattern

**Trigger words:**
- "Sorted array"
- "Pair of elements"
- "Palindrome"
- "Partition"
- "Remove/Skip elements"

## Template/Pseudocode

```python
# Pattern 1: Two pointers from both ends
left, right = 0, len(arr) - 1
while left < right:
    if condition_met(arr[left], arr[right]):
        return [arr[left], arr[right]]
    elif arr[left] + arr[right] < target:
        left += 1
    else:
        right -= 1

# Pattern 2: Slow and fast pointers
slow, fast = 0, 0
while fast < len(arr):
    if condition(arr[fast]):
        slow += 1
        arr[slow] = arr[fast]
    fast += 1
```

## Time & Space Complexity

| Scenario | Time | Space |
|----------|------|-------|
| Two pointers, both ends | O(n) | O(1) |
| Slow/fast pointers | O(n) | O(1) |
| With sorting first | O(n log n) | O(1) |

## Common Mistakes to Avoid

1. **Forgetting to skip duplicates** — Essential in 3Sum and similar
2. **Not considering array must be sorted** — Two pointers usually needs sorting
3. **Wrong pointer movement logic** — Think about what move increases/decreases sum
4. **Off-by-one errors** — `left < right` vs `left <= right`
5. **Returning indices vs values** — Some problems want 1-indexed indices (LeetCode)

## Problems in This Section

| Problem | Difficulty | LeetCode |
|---------|-----------|----------|
| Valid Palindrome | Easy | 125 |
| Two Sum II | Medium | 167 |
| 3Sum | Medium | 15 |
| Container With Most Water | Medium | 11 |

## Key Insights

- **Sorted array is key** — Most two-pointer problems require/work best on sorted data
- **Move the smaller pointer** — In sum problems, always move the pointer at the smaller value
- **Skip duplicates** — When looking for unique triplets, skip duplicate values to avoid returning same combo
- **Pointers converge** — They typically meet in the middle or at boundary
- **Space efficient** — Two pointers uses constant space, great for interviews

## Related Patterns

- **Sliding Window** — Uses two pointers but for contiguous subarrays
- **Binary Search** — Also converges pointers to find target
- **HashMap** — Alternative for problems like Two Sum without sorting
