# Interview Flow — The 10-Step Framework

**Total time: 45 minutes**

This is your complete script for any coding interview. Follow this flow, and you'll communicate clearly, solve systematically, and give yourself the best chance at an offer.

---

## Step 1: Clarify (0:00–1:00)

**Goal**: Fully understand the problem before coding

### What to Say:
- "Let me make sure I understand this correctly..."
- "What are the constraints on the input size?"
- "Can the input be empty? Contain duplicates?"
- "What's the range of values?"
- "Should I return a new array or modify in-place?"
- "Any follow-ups I should think about?"

### What the Interviewer Evaluates:
- Are you thorough or do you rush?
- Can you ask clarifying questions?
- Do you understand the problem completely?

### Red Flags:
- Jumping to coding before clarifying
- Missing obvious constraints (empty input, negative numbers)
- Assuming things not stated

---

## Step 2: Examples (1:00–2:00)

**Goal**: Solidify understanding with concrete examples

### What to Do:
- Walk through one **normal case** (normal input → expected output)
- Create one **edge case** (empty, single element, all same, etc.)
- Trace through your example **step by step**

### Example:
```
Problem: Find two numbers that sum to target
Input: [2, 7, 11, 15], target = 9
Output: [0, 1]

Step 1: Check (2, 7) → 2 + 7 = 9 ✓ Found!

Edge case: [3, 3], target = 6
Output: [0, 1]
```

### What the Interviewer Evaluates:
- Do you actually understand the problem?
- Can you think on your feet?

---

## Step 3: Brute Force (2:00–4:00)

**Goal**: Establish a baseline solution (often obvious)

### What to Say:
- "The brute force would be to..."
- "...which would be O(n²) time and O(1) space"
- **Don't code it** — just explain it

### Example:
```
"I could check every pair of numbers to see if they sum to the target.
Outer loop through each element, inner loop through remaining elements.
This is O(n²) time, O(1) space. But I notice we can do better."
```

### What NOT to Do:
- Don't spend time coding brute force
- Don't make self-deprecating remarks ("This is dumb but...")

### What the Interviewer Evaluates:
- Can you think systematically?
- Do you know time complexity?

---

## Step 4: Optimize (4:00–7:00)

**Goal**: Identify the pattern and improve

### What to Say:
- "I notice this looks like a [PATTERN NAME] problem..."
- "If I use [technique], I can reduce it to O(...)"
- Walk through **why** the optimization works

### Example:
```
"I notice this is a HashMap pattern. I can store values I've seen,
and for each number, check if the complement exists. This is O(n) time
and O(n) space — linear instead of quadratic."
```

### Pattern Recognition Checklist:
- Must be sorted? → Two Pointers or Binary Search
- Substring/subarray? → Sliding Window
- Need all combinations? → Backtracking
- Graph/connectivity? → DFS/BFS
- Need optimal path/choice? → DP or Greedy
- Need k-th element? → Heap

### What the Interviewer Evaluates:
- Can you recognize patterns?
- Do you know classic optimizations?
- Can you think algorithmically?

---

## Step 5: Plan (7:00–9:00)

**Goal**: Get explicit agreement on approach before coding

### What to Say:
- "Here's my approach:
  1. First I'll...
  2. Then I'll...
  3. Finally I'll..."
- "Does this sound good to you?"

### Example:
```
"Here's my plan:
1. Create a mapping of target values I've already seen
2. Loop through the array once
3. For each number, check if (target - current) exists in the map
4. If yes, return the indices; if no, add current to the map
5. Return empty if no pair found
```

### What the Interviewer Evaluates:
- Is your thinking clear?
- Are you organized?
- Can you communicate?

### Red Flags:
- Being vague or uncertain
- Plan changes mid-way through coding

---

## Step 6: Code (9:00–30:00)

**Goal**: Write clean, working code while talking

### What to Do:
- **Talk while typing** — explain what you're doing
- Write clean, readable code
- Use clear variable names
- Add comments for complex logic
- Test against your examples as you code

### Code Template:
```python
def solution(input):
    # Edge case handling
    if not input:
        return expected_edge_case_result
    
    # Initialize data structures
    data_structure = ...
    
    # Main logic
    for element in input:
        # Process element
        ...
    
    # Return result
    return result
```

### What to Say:
- "I'm checking the edge case first..."
- "Now I'm setting up a HashMap to track..."
- "Here I'm iterating and checking the condition..."

### What NOT to Do:
- Long silence while typing
- Writing without explanation
- Trying to be clever (keep it simple)
- Forgetting edge cases

### What the Interviewer Evaluates:
- Can you write correct code?
- Is it readable/maintainable?
- Do you handle edge cases?
- Speed (not too slow, not rushing)

---

## Step 7: Dry Run (30:00–35:00)

**Goal**: Prove your code works

### What to Do:
- Take the example from Step 2
- Trace through your code **line by line**
- Show variable values at each step
- Test both normal and edge cases

### Example Trace:
```
Input: [2, 7, 11, 15], target = 9

Initialize: seen = {}

i=0, num=2:
  target - num = 7
  7 not in seen
  seen = {2: 0}

i=1, num=7:
  target - num = 2
  2 in seen! ✓
  Return [seen[2], 1] = [0, 1] ✓
```

### What the Interviewer Evaluates:
- Do you catch your own bugs?
- Are you careful/meticulous?

---

## Step 8: Edge Cases (35:00–38:00)

**Goal**: Show you think about boundaries

### Common Edge Cases:
- Empty input
- Single element
- All same values
- Maximum/minimum values
- Duplicates
- Negative numbers
- Very large input

### What to Say:
- "Let me check some edge cases:
  - Empty array: [returns] ✓
  - Single element: [returns] ✓
  - All duplicates: [returns] ✓"

### What NOT to Do:
- Just list edge cases without testing
- Spend more than 3 minutes here

---

## Step 9: Complexity Analysis (38:00–40:00)

**Goal**: Justify your solution

### What to Say:
```
"Time Complexity: O(n)
  - Single pass through array
  - HashMap operations are O(1)
  - So overall O(n)

Space Complexity: O(n)
  - Worst case, all elements go in the map
  - So O(n) space for the HashMap"
```

### What the Interviewer Evaluates:
- Do you understand complexity?
- Can you justify your solution?

### Red Flags:
- Saying "O(n)" without explanation
- Wrong analysis

---

## Step 10: Follow-up (40:00–45:00)

**Goal**: Show you can adapt

### Common Follow-ups:
- **Two Sum variants:**
  - "What if you need all unique pairs?"
  - "What if the array is sorted?"
  - "What about three numbers (3Sum)?"

- **General:**
  - "Can you do this in-place?"
  - "Can you do this without extra space?"
  - "What if the input is coming in as a stream?"
  - "How would you optimize for space?"

### What to Do:
- Take 30–40 seconds to think
- Say "Great question! Let me think..."
- Outline approach (don't code unless asked)

### What the Interviewer Evaluates:
- Can you adapt?
- Do you understand trade-offs?

---

## 🆘 Panic Recovery — What to Do When Stuck

### **In the middle of coding, you realize your approach won't work:**

1. **Stay calm** — Don't panic or apologize excessively
2. **Communicate** — "I'm realizing this approach won't work because..."
3. **Go back to basics** — "Let me step back and reconsider..."
4. **Brute force** — "Let me go with the O(n²) approach to get something working..."
5. **Move forward** — Complete the brute force, mention optimizations

### **You're stuck on a specific part:**

- "Let me think out loud about this for a second..."
- Consider walking through an example
- Ask the interviewer for a hint ("Can I think about how to handle X?")

### **You freeze completely:**

- "I know this pattern, but I'm blanking. Can I take 30 seconds to think?"
- Use the pattern cheatsheet mentally (HashMap, two pointers, etc.)
- Start with brute force to unstick yourself

### **You're running low on time:**

- Finish coding the brute force
- Mention complexity issues clearly
- Say "In a real scenario, I'd refactor to use [pattern]"

---

## 📋 Timing Checklist

| Time | Done? | Next |
|------|-------|------|
| 0:00–1:00 | ☐ | Move to examples |
| 1:00–2:00 | ☐ | Start brute force |
| 2:00–4:00 | ☐ | Identify optimization |
| 4:00–7:00 | ☐ | Plan it out |
| 7:00–9:00 | ☐ | Get a nod, start coding |
| 9:00–30:00 | ☐ | Finish + test against examples |
| 30:00–35:00 | ☐ | Check edge cases |
| 35:00–38:00 | ☐ | Analyze complexity |
| 38:00–40:00 | ☐ | Answer follow-up |
| 40:00–45:00 | ☐ | Wrap up |

---

## 🎯 Key Phrases to Remember

✅ **Say these:**
- "Let me make sure I understand..."
- "I notice this looks like a [PATTERN] problem..."
- "Here's my approach..."
- "Okay, now let me trace through my example..."
- "One edge case to watch for is..."
- "The time is O(...) because..."
- "Great question! Let me think about that..."

❌ **Don't say these:**
- "I think..." (say "I know")
- "Sorry, I'm nervous" (they don't want to hear it)
- "I don't know" (say "let me think about that")
- "This is dumb but..." (be confident)
- "I'm bad at X" (negative self-talk)

---

## 📚 Practice This

1. **Do 3 problems today**, using every step
2. **Do a timed mock** on Pramp.com, following this flow exactly
3. **Repeat** until it becomes automatic

You've got this! 💪
