"""
Problem: Min Stack
LeetCode #: 155
Difficulty: Medium
URL: https://leetcode.com/problems/min-stack/

Pattern: Stack
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Use a regular stack and calculate min for each getMin() call
- Time: push/pop O(1), getMin O(n)  |  Space: O(n)

Optimal:
- Keep two stacks: one for values, one for minimums
- Each minimum stack entry corresponds to the min up to that point
- When pushing, push min of new value and current min
- Time: All O(1)  |  Space: O(n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"We need a stack that also tracks the minimum in O(1). We can't just find
the min on demand - that's O(n). Instead, we use a second 'min stack' that
stores the running minimum. Every time we push a value, we also push the
minimum up to that point. This way, getMin is always O(1)."

"""


# ─── Brute Force ───
class BruteForceSolution:
    def __init__(self):
        self.stack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
    
    def pop(self) -> None:
        self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        """
        Find min by scanning - O(n).
        """
        return min(self.stack)


# ─── Optimal ───
class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val: int) -> None:
        """Push value and update min stack - O(1)."""
        self.stack.append(val)
        # Push the minimum up to this point
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)
    
    def pop(self) -> None:
        """Pop from both stacks - O(1)."""
        self.stack.pop()
        self.min_stack.pop()
    
    def top(self) -> int:
        """Return top element - O(1)."""
        return self.stack[-1]
    
    def getMin(self) -> int:
        """Return minimum - O(1)."""
        return self.min_stack[-1]


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Basic operations
    sol.push(-2)
    sol.push(0)
    sol.push(-3)
    assert sol.getMin() == -3
    sol.pop()
    assert sol.top() == 0
    assert sol.getMin() == -2
    
    # Test 2: All negative
    sol2 = Solution()
    sol2.push(-1)
    sol2.push(-2)
    assert sol2.getMin() == -2
    
    # Test 3: Increasing values
    sol3 = Solution()
    sol3.push(1)
    sol3.push(2)
    sol3.push(3)
    assert sol3.getMin() == 1
    assert sol3.top() == 3
    
    # Test 4: Duplicate minimums
    sol4 = Solution()
    sol4.push(5)
    sol4.push(5)
    sol4.push(5)
    assert sol4.getMin() == 5
    
    print("All tests passed!")
