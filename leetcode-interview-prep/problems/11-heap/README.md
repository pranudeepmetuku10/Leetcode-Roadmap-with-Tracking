# Heap

## Pattern Overview

Heap problems involve priority queues and efficient ordering. Use heaps for top-k problems and frequent element queries.

## When to Recognize This Pattern

**Trigger words:**
- "Top k"
- "Kth largest/smallest"
- "Median"
- "Most frequent"
- "Schedule/order by priority"

## Template/Pseudocode

```python
import heapq

# Max heap (Python has min heap; negate for max)
max_heap = []
heapq.heappush(max_heap, -x)  # Push negative
value = -heapq.heappop(max_heap)  # Pop and negate

# Min heap
min_heap = []
heapq.heappush(min_heap, x)
value = heapq.heappop(min_heap)

# Heap of tuples (sorted by first element)
heap = []
heapq.heappush(heap, (priority, item))

# Find median with two heaps
max_heap = []  # For smaller half (negate values)
min_heap = []  # For larger half
# Maintain invariant: max_heap has <= one more element than min_heap
```

## Time & Space Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Push/Pop | O(log n) | O(n) |
| Heapify | O(n) | O(1) |
| Top k | O(n log k) | O(k) |

## Common Mistakes to Avoid

1. **Forgetting Python heaps are min heaps** — Negate for max heap
2. **Heap not sorted** — Heap is partially ordered, not fully sorted
3. **Modifying heap after insertion** — Breaks heap invariant
4. **Wrong heap size** — For top-k, maintain exactly k elements
5. **Time complexity** — O(n log k) for top-k, not O(k log n)

## Problems in This Section

| Problem | Difficulty | LeetCode |
|---------|-----------|----------|
| Kth Largest Element | Medium | 215 |
| Task Scheduler | Medium | 621 |
| Find Median Data Stream | Hard | 295 |

## Key Insights

- **Two heaps for median** — Max heap for lower half, min heap for upper
- **Top-k pattern** — Min heap of size k, ignore elements below kth largest
- **Lazy deletion** — Sometimes easier to keep invalid elements in heap
- **Frequency tracking** — Combine with HashMap for frequency-based ordering
- **Partial sort advantage** — Heap maintains order without full sort

## Related Patterns

- **QuickSelect** — Alternative for top-k (faster average but O(n²) worst)
- **Sorting** — Simple but O(n log n); heap can be O(n log k)
- **HashMap+Sorting** — Another approach to frequency problems
