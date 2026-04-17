# Stack

## Pattern Overview

Stack (Last-In-First-Out) problems often involve matching pairs, parsing, or tracking state. The key insight is using a stack to defer processing or maintain order.

## When to Recognize This Pattern

**Trigger words:**
- "Matching pairs" (parentheses)
- "Next greater/smaller element"
- "Evaluate expression"
- "Reverse order"
- "Undo/backtrack functionality"

## Template/Pseudocode

```python
# Pattern 1: Matching pairs
stack = []
for char in s:
    if should_add(char):
        stack.append(char)
    elif stack and stack[-1] matches char:
        stack.pop()
    else:
        return False
return len(stack) == 0

# Pattern 2: Next greater element
stack = []
for i, num in enumerate(nums):
    while stack and stack[-1] < num:
        prev_idx = stack.pop()
        result[prev_idx] = num
    stack.append((num, i))
```

## Time & Space Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Push/Pop | O(1) | O(n) |
| Each element visited once | O(n) | O(n) |

## Common Mistakes to Avoid

1. **Accessing empty stack** — Always check `if stack` before popping
2. **Wrong matching pairs** — Know what closes what
3. **Forgetting to output** — Sometimes result is at end or specific value
4. **Stack grows unbounded** — Be aware of space usage
5. **Confusing flow** — Draw it out, trace through once

## Problems in This Section

| Problem | Difficulty | LeetCode |
|---------|-----------|----------|
| Valid Parentheses | Easy | 20 |
| Min Stack | Medium | 155 |
| Evaluate Reverse Polish Notation | Medium | 150 |
| Daily Temperatures | Medium | 739 |

## Key Insights

- **Deferred processing** — Stack lets you process pairs in order
- **Next greater element** — Classic use: post-order processing
- **Min tracking** — Store both value and minimum up to that point
- **Index tracking** — Often need indices not just values
- **Space trade-off** — Trading space for O(n) time

## Related Patterns

- **Queue** — For BFS and other forward-order problems
- **DFS** — Implicit stack via recursion
- **Monotonic Stack** — Stack maintaining sorted order
