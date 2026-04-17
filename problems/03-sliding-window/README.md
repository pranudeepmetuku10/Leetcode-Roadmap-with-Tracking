# Sliding Window

## Pattern Overview

The Sliding Window pattern expands and shrinks a window over data to solve problems efficiently. It's used for finding subarrays/substrings with specific properties.

## When to Recognize This Pattern

**Trigger words:**
- "Contiguous subarray/substring"
- "Longest/shortest"
- "At most/at least"
- "Average/sum of all subarrays"
- "Any subarray with property X"

## Template/Pseudocode

```python
# Basic sliding window template
left = 0
for right in range(len(array)):
    # Add element at right pointer
    window_element = array[right]
    
    # Shrink from left while condition not met
    while not is_valid(window):
        left += 1
    
    # Process current window
    result = max(result, right - left + 1)

return result
```

## Time & Space Complexity

| Scenario | Time | Space |
|----------|------|-------|
| Basic sliding window | O(n) | O(k) for window |
| With HashMap | O(n) | O(26) for chars |

## Common Mistakes to Avoid

1. **Forgetting to shrink window** — Don't just expand
2. **Off-by-one in window size** — Use `right - left + 1`
3. **Not resetting window state** — Clear hashmap when starting over
4. **Complexity miscalculation** — Both pointers move but still O(n) total
5. **Silent bugs** — Edge cases: empty array, single element

## Problems in This Section

| Problem | Difficulty | LeetCode |
|---------|-----------|----------|
| Best Time to Buy & Sell Stock | Easy | 121 |
| Longest Substring Without Repeating | Medium | 3 |
| Longest Repeating Char Replacement | Medium | 424 |
| Minimum Window Substring | Hard | 76 |

## Key Insights

- **Two pointers move in same direction** — Distinguishes from two-pointer pattern
- **Expand first, shrink later** — Right expands until condition, left shrinks
- **Track window state** — HashMap for frequencies, set for uniqueness
- **Linear time guaranteed** — Each element visited at most twice
- **Great for substring/subarray problems** — When order matters

## Related Patterns

- **Two Pointers** — Both pointers but from opposite ends
- **HashMap** — Often combined with sliding window for tracking
- **Binary Search** — Alternative for some problems (slower but valid)
