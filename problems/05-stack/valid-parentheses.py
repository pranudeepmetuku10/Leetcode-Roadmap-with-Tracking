"""
Problem: Valid Parentheses
LeetCode #: 20
Difficulty: Easy
URL: https://leetcode.com/problems/valid-parentheses/

Pattern: Stack
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Check for valid parentheses by recursively removing pairs
- Time: O(n²)  |  Space: O(n) for recursion

Optimal:
- Use a stack to track opening brackets
- For each closing bracket, check if it matches the top of stack
- If all brackets match and stack is empty, valid
- Key Insight: Stack naturally handles nested structure matching
- Time: O(n)  |  Space: O(n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"We need to verify that parentheses are properly matched. A stack is perfect
for this: we push opening brackets onto the stack, and when we see a closing
bracket, we check if it matches the most recent opening bracket. If all
brackets match and the stack is empty at the end, the string is valid."

"""


# ─── Brute Force ───
class BruteForceSolution:
    def isValid(self, s: str) -> bool:
        """
        Recursively remove matching pairs.
        """
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "").replace("[]", "").replace("{}", "")
        return len(s) == 0


# ─── Optimal ───
class Solution:
    def isValid(self, s: str) -> bool:
        """
        Use stack to match parentheses - O(n) time.
        """
        stack = []
        pairs = {"(": ")", "[": "]", "{": "}"}
        
        for char in s:
            if char in pairs:
                # Opening bracket - push to stack
                stack.append(char)
            else:
                # Closing bracket - check if it matches top of stack
                if not stack or pairs[stack.pop()] != char:
                    return False
        
        return len(stack) == 0


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Valid simple brackets
    assert sol.isValid("()") == True
    
    # Test 2: Valid nested brackets
    assert sol.isValid("()[]{}") == True
    
    # Test 3: Invalid - wrong closing
    assert sol.isValid("(]") == False
    
    # Test 4: Unmatched opening
    assert sol.isValid("(") == False
    
    print("All tests passed!")
