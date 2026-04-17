# Dynamic Programming

## Pattern Overview

Dynamic Programming solves optimization problems by breaking them into subproblems and storing results to avoid recomputation. The key is identifying overlapping subproblems.

## When to Recognize This Pattern

**Trigger words:**
- "Longest/shortest", "Maximum/minimum"
- "Number of ways"
- "Fibonacci-like"
- "Optimal strategy"
- "Can you achieve this?"

## Template/Pseudocode

```python
# Top-down (Memoization - Recursion)
memo = {}
def dp(state):
    if state in memo:
        return memo[state]
    if base_case(state):
        return base_value
    
    result = optimize over choices
    memo[state] = result
    return result

# Bottom-up (Tabulation - Iteration)
dp = [0] * (n + 1)
dp[0] = base_case
for i in range(1, n + 1):
    dp[i] = optimize(dp[i-1], dp[i-2], ...)
return dp[n]
```

## Time & Space Complexity

| Pattern | Time | Space |
|---------|------|-------|
| Fibonacci | O(n) | O(n) |
| Knapsack | O(nW) | O(nW) |
| Edit Distance | O(mn) | O(mn) |

## Common Mistakes to Avoid

1. **Wrong state definition** — State must capture all needed info
2. **Off-by-one errors** — Base cases and transitions critical
3. **Space inefficiency** — Use sliding window when only last few states matter
4. **Memoization miss** — Check all possible subproblems
5. **Recursion depth exceeded** — Use bottom-up for large inputs

## Problems in This Section

| Problem | Difficulty | LeetCode |
|---------|-----------|----------|
| Climbing Stairs | Easy | 70 |
| House Robber | Medium | 198 |
| Coin Change | Medium | 322 |
| Longest Increasing Subsequence | Medium | 300 |
| Word Break | Medium | 139 |
| Unique Paths | Medium | 62 |
| Longest Common Subsequence | Medium | 1143 |
| Decode Ways | Medium | 91 |

## Key Insights

- **State = answer for subproblem** — Define clearly
- **Transition = relationship between states** — How does current depend on previous
- **Base case = smallest subproblem** — Where recursion bottoms out
- **Memoization vs Tabulation** — Memo is top-down/recursive, Tabulation is bottom-up/iterative
- **Space optimization** — Often can reduce from O(n) to O(1) by tracking only recent states

## Related Patterns

- **Backtracking** — Explores all possibilities; DP memoizes optimal
- **Greedy** — Makes locally optimal choices; DP considers all choices
- **Recursion** — Memoization is recursion with caching
