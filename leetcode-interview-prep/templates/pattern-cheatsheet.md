# Pattern Cheatsheet — Quick Reference for 13 Core Patterns

**Use this sheet during mock interviews as a mental checklist.**

---

## 1. Two Pointers

**When to use:**
- Sorted array
- Find pair with target sum
- Palindrome validation
- Remove/partition elements

**Trigger words:** "sorted", "pair", "palindrome", "two-way"

**Template:**
```python
left, right = 0, len(arr) - 1
while left < right:
    if arr[left] + arr[right] == target:
        return [arr[left], arr[right]]
    elif arr[left] + arr[right] < target:
        left += 1
    else:
        right -= 1
```

**Time | Space:** O(n) | O(1)

**#1 Mistake:** Not skipping duplicates in 3Sum

**Top 3 problems:**
1. Two Sum II (167)
2. 3Sum (15)
3. Container With Most Water (11)

---

## 2. Sliding Window

**When to use:**
- Substring/subarray with property
- Longest/shortest with constraint
- Target sum in contiguous elements

**Trigger words:** "substring", "contiguous", "longest", "at most"

**Template:**
```python
left = 0
result = 0
window_state = {}  # Or set, or counter

for right in range(len(arr)):
    # Expand: add right element
    window_state[arr[right]] += 1
    
    # Shrink: while invalid
    while not is_valid(window_state):
        window_state[arr[left]] -= 1
        left += 1
    
    # Update result
    result = max(result, right - left + 1)
return result
```

**Time | Space:** O(n) | O(k)

**#1 Mistake:** Calculating window size as `right - left` instead of `right - left + 1`

**Top 3 problems:**
1. Longest Substring Without Repeating (3)
2. Minimum Window Substring (76)
3. Longest Repeating Character Replacement (424)

---

## 3. Binary Search

**When to use:**
- Sorted array, need to find target
- Search space can be halved
- Optimization: binary search on answer

**Trigger words:** "sorted", "search", "find", "minimize/maximize"

**Template:**
```python
left, right = 0, len(arr) - 1
while left <= right:
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return -1

# Optimization pattern (binary search on answer)
def can_achieve(value):
    return True/False

left, right = min_possible, max_possible
while left < right:
    mid = left + (right - left) // 2
    if can_achieve(mid):
        right = mid
    else:
        left = mid + 1
return left
```

**Time | Space:** O(log n) | O(1)

**#1 Mistake:** Using `(left + right) // 2` → overflow risk (though not in Python)

**Top 3 problems:**
1. Binary Search (704)
2. Search Rotated Sorted Array (33)
3. Koko Eating Bananas (875)

---

## 4. HashMap / Set

**When to use:**
- Lookup in O(1)
- Count frequencies
- Grouping by key
- Detect duplicates

**Trigger words:** "find", "check if exists", "count", "group"

**Template:**
```python
# Frequency counting
from collections import Counter
freq = Counter(arr)  # Or: freq[x] = freq.get(x, 0) + 1

# Grouping
from collections import defaultdict
groups = defaultdict(list)
for item in arr:
    key = get_key(item)
    groups[key].append(item)

# Lookup
seen = set()
for item in arr:
    if item in seen:
        return True
    seen.add(item)
```

**Time | Space:** O(1) lookup | O(n) for storage

**#1 Mistake:** Hash collision (rare but matters for interviewer)

**Top 3 problems:**
1. Two Sum (1)
2. Group Anagrams (49)
3. Contains Duplicate (217)

---

## 5. Stack

**When to use:**
- Matching pairs (parentheses)
- Next greater/smaller element
- Undo/backtrack
- Evaluate expressions

**Trigger words:** "matching", "parentheses", "next", "expression", "reverse"

**Template:**
```python
# Matching pairs
stack = []
for char in s:
    if char in opening:
        stack.append(char)
    elif stack and matches(stack[-1], char):
        stack.pop()
    else:
        return False
return len(stack) == 0

# Next greater element
stack = []
result = [0] * len(arr)
for i in range(len(arr) - 1, -1, -1):
    while stack and stack[-1][0] <= arr[i]:
        stack.pop()
    result[i] = stack[-1][0] if stack else -1
    stack.append((arr[i], i))
```

**Time | Space:** O(n) | O(n)

**#1 Mistake:** Forgetting to check `if stack` before popping

**Top 3 problems:**
1. Valid Parentheses (20)
2. Min Stack (155)
3. Daily Temperatures (739)

---

## 6. BFS / DFS (Graph & Tree)

**When to use:**
- Graph traversal, connectivity
- Find all reachable nodes
- Level-order traversal
- Shortest path (unweighted)

**Trigger words:** "connected", "traverse", "path", "shortest", "islands"

**Template:**
```python
# DFS - Recursive
def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)
    for neighbor in graph[node]:
        dfs(neighbor, visited)

# BFS - Queue based
from collections import deque
visited = {start}
queue = deque([start])
while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```

**Time | Space:** O(V + E) | O(V)

**#1 Mistake:** Forgetting visited set → infinite loops

**Top 3 problems:**
1. Number of Islands (200)
2. Clone Graph (133)
3. Pacific Atlantic Water Flow (417)

---

## 7. Backtracking

**When to use:**
- Generate all combinations/permutations
- Find all solutions
- Constraint satisfaction

**Trigger words:** "all", "combinations", "permutations", "subsets"

**Template:**
```python
def backtrack(path, remaining, result):
    # Base case
    if is_complete(path):
        result.append(path[:])
        return
    
    # Explore all choices
    for choice in get_choices(remaining):
        # Make choice
        path.append(choice)
        remaining.remove(choice)
        
        # Explore recursively
        backtrack(path, remaining, result)
        
        # Undo choice (critical!)
        path.pop()
        remaining.add(choice)

result = []
backtrack([], input_set, result)
return result
```

**Time | Space:** O(2^n) for subsets | O(n) recursion depth

**#1 Mistake:** Forgetting to backtrack (undo changes)

**Top 3 problems:**
1. Subsets (78)
2. Combination Sum (39)
3. Word Search (79)

---

## 8. Dynamic Programming (1D)

**When to use:**
- Linear optimization (climbing stairs, rob houses)
- String problems (decode ways)
- Counting ways

**Trigger words:** "path", "ways", "maximum", "minimum", "optimal"

**Template:**
```python
# 1D DP
dp = [0] * (n + 1)
dp[0] = base_case

for i in range(1, n + 1):
    dp[i] = optimize(dp[i-1], dp[i-2], ...)  # Or other previous states

return dp[n]

# Or top-down (memoization)
memo = {}
def dp(n):
    if n in memo:
        return memo[n]
    if base_case:
        return base_value
    
    memo[n] = optimize(dp(n-1), dp(n-2), ...)
    return memo[n]
```

**Time | Space:** O(n) | O(n) or O(1) if space-optimized

**#1 Mistake:** Wrong state definition → wrong answer

**Top 3 problems:**
1. Climbing Stairs (70)
2. House Robber (198)
3. Coin Change (322)

---

## 9. Dynamic Programming (2D)

**When to use:**
- Grid problems, paths
- String matching, edit distance
- 2D optimization

**Trigger words:** "grid", "path", "matrix", "edit", "distance"

**Template:**
```python
# 2D DP
dp = [[0] * m for _ in range(n)]

# Base case
dp[0][0] = initial_value
for i in range(n):
    dp[i][0] = calc_from_above(dp[i-1][0])
for j in range(m):
    dp[0][j] = calc_from_left(dp[0][j-1])

# Fill table
for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = optimize(dp[i-1][j], dp[i][j-1], ...)

return dp[n-1][m-1]
```

**Time | Space:** O(n×m) | O(n×m)

**#1 Mistake:** Off-by-one errors in boundaries

**Top 3 problems:**
1. Unique Paths (62)
2. Longest Common Subsequence (1143)
3. Edit Distance (72) — not in this course but common

---

## 10. Heap / Priority Queue

**When to use:**
- Top-k problems
- Kth largest/smallest
- Median in stream
- Frequency-based ordering

**Trigger words:** "top k", "kth", "largest", "smallest", "frequent"

**Template:**
```python
import heapq

# Max heap (negate for min)
max_heap = []
heapq.heappush(max_heap, -value)
max_val = -heapq.heappop(max_heap)

# Min heap of size k
min_heap = []
for num in nums:
    heapq.heappush(min_heap, num)
    if len(min_heap) > k:
        heapq.heappop(min_heap)

# Return top k
return min_heap
```

**Time | Space:** O(n log k) | O(k)

**#1 Mistake:** Forgetting Python uses min heap

**Top 3 problems:**
1. Kth Largest Element (215)
2. Find Median Data Stream (295)
3. Top K Frequent Elements (347)

---

## 11. Intervals

**When to use:**
- Merge overlapping intervals
- Schedule meetings, check conflicts
- Non-overlapping interval selection

**Trigger words:** "overlap", "merge", "schedule", "meeting", "conflict"

**Template:**
```python
# Sort by start time
intervals.sort()

merged = [intervals[0]]
for start, end in intervals[1:]:
    if start <= merged[-1][1]:  # Overlapping
        merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:  # Non-overlapping
        merged.append((start, end))

return merged

# For non-overlapping count (greedy)
intervals.sort(key=lambda x: x[1])  # Sort by end time!
count = 0
last_end = float('-inf')
for start, end in intervals:
    if start >= last_end:
        count += 1
        last_end = end
```

**Time | Space:** O(n log n) | O(1)

**#1 Mistake:** Not sorting first, or sorting by wrong field

**Top 3 problems:**
1. Merge Intervals (56)
2. Non-Overlapping Intervals (435)
3. Meeting Rooms II (253)

---

## 12. Trie

**When to use:**
- Prefix matching, autocomplete
- Word dictionary
- Wildcard search

**Trigger words:** "prefix", "autocomplete", "trie", "dictionary"

**Template:**
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

**Time | Space:** O(m) insert/search | O(n×m) total

**#1 Mistake:** Confusing search (full word) with startsWith (prefix)

**Top 3 problems:**
1. Implement Trie (208)
2. Design Add & Search Words (211)
3. Word Search II (212) — not in this course

---

## 13. Linked List

**When to use:**
- Reversal, merging, reordering
- Cycle detection
- Find k-th from end

**Trigger words:** "linked list", "reverse", "merge", "cycle", "middle"

**Template:**
```python
# Node definition
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Reverse
prev, curr = None, head
while curr:
    next_temp = curr.next
    curr.next = prev
    prev = curr
    curr = next_temp
return prev

# Slow & fast pointers (find middle, detect cycle)
slow, fast = head, head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
# slow is at middle (or cycle start for cycle detection)
```

**Time | Space:** O(n) | O(1)

**#1 Mistake:** Losing references when modifying pointers

**Top 3 problems:**
1. Reverse Linked List (206)
2. Linked List Cycle (141)
3. Reorder List (143)

---

## ⚡ Decision Tree — Which Pattern?

```
Is it a SORTED array?
├─ Yes → Need to find pair? → Two Pointers
└─ No

Is it about SUBSTRING/SUBARRAY?
├─ Yes → Properties to match? → Sliding Window
└─ No

Need to SEARCH in sorted?
├─ Yes → Binary Search
└─ No

Need O(1) LOOKUP/FREQUENCY?
├─ Yes → HashMap / Set
└─ No

Need NEXT GREATER or MATCHING PAIRS?
├─ Yes → Stack
└─ No

Need SHORTEST PATH or CONNECTIVITY?
├─ Yes → BFS / DFS
└─ No

Need ALL SOLUTIONS / COMBINATIONS?
├─ Yes → Backtracking
└─ No

Need OPTIMAL CHOICE / COUNTING WAYS?
├─ Yes → Dynamic Programming
└─ No

Need TOP-K or FREQUENCY ORDERING?
├─ Yes → Heap
└─ No

Need OVERLAP / SCHEDULING?
├─ Yes → Intervals
└─ No

Need PREFIX MATCHING?
├─ Yes → Trie
└─ No

Is it about LINKED LIST?
├─ Yes → Linked List techniques
└─ No

Otherwise → Tree / Recursion
```

---

**During an interview:** Look at the problem, follow this decision tree, remember the template, code it up. You've got this! 💪
