"""
Problem: Daily Temperatures
LeetCode #: 739
Difficulty: Medium
URL: https://leetcode.com/problems/daily-temperatures/

Pattern: Stack
Companies: Google, Amazon, Meta, Microsoft

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- For each day, search forward to find the next warmer day
- Time: O(n²)  |  Space: O(1)

Optimal:
- Use a monotonic decreasing stack storing indices
- Process from right to left
- When current temp is warmer, pop from stack until we find a warmer day
- The right answer is the difference between current and found index
- Key Insight: Stack avoids repeatedly searching forward
- Time: O(n)  |  Space: O(n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"We need to find the next warmer day for each day. A naive approach checks
all future days - O(n²). But we can use a monotonic stack: maintain a stack
of indices in decreasing order of temperature. When we see a warmer day, it
matches with indices on the stack, and we pop them. This is O(n) total."

"""
from typing import List


# ─── Brute Force ───
class BruteForceSolution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        For each day, search forward - O(n²) time.
        """
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break
        return result


# ─── Optimal ───
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Monotonic stack - O(n) time.
        """
        n = len(temperatures)
        result = [0] * n
        stack = []  # Stack of indices with decreasing temperatures
        
        for i in range(n):
            # Pop while current temperature is warmer than stack top
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                result[prev_idx] = i - prev_idx
            
            # Push current index
            stack.append(i)
        
        return result


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Basic case with some matches
    assert sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    
    # Test 2: Strictly decreasing - no warmer days
    assert sol.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    
    # Test 3: Strictly increasing - no warmer days ahead
    assert sol.dailyTemperatures([60, 50, 40, 30]) == [0, 0, 0, 0]
    
    # Test 4: All same temperature
    assert sol.dailyTemperatures([30, 30, 30]) == [0, 0, 0]
    
    print("All tests passed!")
