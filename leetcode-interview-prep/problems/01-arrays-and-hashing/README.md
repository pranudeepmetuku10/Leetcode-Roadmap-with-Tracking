# Arrays & Hashing

## Pattern Overview

The Arrays & Hashing pattern involves using hash tables (dictionaries/sets) to optimize array problems by trading space for time. This is one of the most fundamental patterns in coding interviews.

## When to Recognize This Pattern

**Trigger words:**
- "Find/Check if exists"
- "Count frequencies"
- "Group/Categorize elements"
- "Need O(1) lookup time"
- "Complement/Pair problems"

## Template/Pseudocode

```python
# Pattern 1: Tracking frequencies
freq = {}
for item in arr:
    freq[item] = freq.get(item, 0) + 1

# Pattern 2: Complement lookup
seen = {}
for item in arr:
    target = DESIRED_VALUE - item
    if target in seen:
        return [item, target]
    seen[item] = index

# Pattern 3: Grouping
groups = defaultdict(list)
for item in arr:
    key = get_key(item)  # Sorted string for anagrams, etc.
    groups[key].append(item)
return groups.values()
```

## Time & Space Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Insert | O(1) avg | O(1) |
| Lookup | O(1) avg | O(1) |
| Delete | O(1) avg | O(1) |
| Hash collision | O(n) worst | O(1) |

## Common Mistakes to Avoid

1. **Forgetting about hash collisions** — Average O(1) but worst O(n)
2. **Using lists instead of sets** — Set lookup is O(1), list is O(n)
3. **Not handling edge cases** — Empty arrays, duplicates, zeros
4. **Memory overflow** — HashMap can grow to O(n) space; be aware on memory-constrained problems
5. **Not considering if hash order matters** — Most languages: dictionaries preserve insertion order in Python 3.7+

## Problems in This Section

| Problem | Difficulty | LeetCode | Status |
|---------|-----------|----------|--------|
| Two Sum | Easy | 1 | |
| Valid Anagram | Easy | 242 | |
| Contains Duplicate | Easy | 217 | |
| Group Anagrams | Medium | 49 | |
| Top K Frequent Elements | Medium | 347 | |
| Product of Array Except Self | Medium | 238 | |

## Key Insights

- **HashMap is your friend** — When you see O(n²) brute force with nested loops, think HashMap
- **Sorted strings as keys** — For anagram problems, sorting gives you a unique key
- **Track what you've seen** — Many problems need "have I seen this value before?"
- **Count frequencies** — Group elements by frequency, then sort/heap
- **Avoid division with zeros** — Use prefix/suffix products instead

## Related Patterns

- **Two Pointers** — Can also solve some array problems when array is sorted
- **Sliding Window** — For contiguous subarrays with some property
- **Heap** — When you need top-k or sorted frequencies
