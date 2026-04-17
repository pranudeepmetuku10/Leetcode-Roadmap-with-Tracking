# Backtracking

## Pattern Overview

Backtracking explores all possible solutions by building candidates incrementally and abandoning branches that don't satisfy constraints.

## When to Recognize This Pattern

**Trigger words:**
- "All combinations/permutations/subsets"
- "Find all solutions"
- "N-queens problem"
- "Word search"
- "Board/grid exploration"

## Template/Pseudocode

```python
def backtrack(candidates, path, result):
    # Base case: found a solution
    if is_solution(path):
        result.append(path[:])  # Make a copy
        return
    
    # Explore all choices
    for choice in get_choices(candidates):
        # Prune: skip if choice violates constraints
        if is_valid(choice, path):
            # Make choice
            path.append(choice)
            candidates.remove(choice)
            
            # Explore recursively
            backtrack(candidates, path, result)
            
            # Undo choice (backtrack)
            path.pop()
            candidates.add(choice)

def solve(nums):
    result = []
    backtrack(nums, [], result)
    return result
```

## Time & Space Complexity

| Scenario | Time | Space |
|----------|------|-------|
| Subsets | O(2^n) | O(n) |
| Permutations | O(n!) | O(n) |
| N-queens | O(n!) | O(n) |

## Common Mistakes to Avoid

1. **Forgetting to backtrack** — Must undo changes
2. **Returning reference not copy** — Use `path[:]` to copy
3. **Inefficient pruning** — Cut branches early
4. **Duplicate solutions** — Sort input or use set to avoid
5. **Time limit exceeded** — Backtracking can be slow; optimize pruning

## Problems in This Section

| Problem | Difficulty | LeetCode |
|---------|-----------|----------|
| Subsets | Medium | 78 |
| Combination Sum | Medium | 39 |
| Word Search | Medium | 79 |

## Key Insights

- **Recursion + Undo** — Define choice, solve subproblem, undo
- **Pruning critical** — Backtracking can explode; cut early
- **Path building** — Often maintain current path during recursion
- **All solutions** — Not optimizing for one answer, but finding all
- **State restoration** — Careful with mutable state

## Related Patterns

- **Dynamic Programming** — Both explore possibilities, but DP memoizes
- **DFS** — Backtracking is guided DFS
- **Combinations/Permutations** — Foundational backtracking patterns
