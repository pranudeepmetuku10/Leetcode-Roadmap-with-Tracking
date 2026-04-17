# Intervals

## Pattern Overview

Interval problems involve merging, scheduling, and overlapping detection. Sorting is almost always the first step.

## When to Recognize This Pattern

**Trigger words:**
- "Overlap/merge intervals"
- "Meeting rooms"
- "Schedule/calendar"
- "Non-overlapping"
- "Intersection"

## Template/Pseudocode

```python
# Sort intervals by start time
intervals.sort()

# Merge intervals
merged = [intervals[0]]
for start, end in intervals[1:]:
    if start <= merged[-1][1]:
        # Overlapping: merge
        merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:
        # Non-overlapping: add new interval
        merged.append((start, end))

# Count non-overlapping (greedy: always pick earliest end)
intervals.sort(key=lambda x: x[1])
count = 0
last_end = float('-inf')
for start, end in intervals:
    if start >= last_end:
        count += 1
        last_end = end
```

## Time & Space Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Merge | O(n log n) | O(1) |
| Non-overlapping | O(n log n) | O(1) |

## Common Mistakes to Avoid

1. **Wrong overlap condition** — `start <= prev_end` includes touching intervals
2. **Forgetting to sort** — Almost all interval problems need sorting first
3. **Not considering edge cases** — Empty input, single interval
4. **Greedy goes wrong** — Counterintuitive when to pick earliest end
5. **Off-by-one in boundaries** — `start <` vs `start <=`

## Problems in This Section

| Problem | Difficulty | LeetCode |
|---------|-----------|----------|
| Merge Intervals | Medium | 56 |
| Non-Overlapping Intervals | Medium | 435 |
| Meeting Rooms II | Medium | 253 |

## Key Insights

- **Sort first** — Enables linear merge/check after sorting
- **Scan once** — After sorting, single pass often solves
- **Greedy works** — For many interval problems (earliest end optimal)
- **Overlap = start <= prev_end** — Not just `<`
- **Boundary careful** — Inclusive vs exclusive matters

## Related Patterns

- **Sweepline Algorithm** — Events at start/end for coordinate problems
- **Priority Queue** — For meeting rooms (track end times)
- **Binary Search** — Insert intervals into sorted list
