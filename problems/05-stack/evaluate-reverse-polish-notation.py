"""
Problem: Evaluate Reverse Polish Notation
LeetCode #: 150
Difficulty: Medium
URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/

Pattern: Stack
Companies: Amazon, Google, Microsoft, Apple

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Evaluate with multiple passes, building intermediate results
- Time: O(n²)  |  Space: O(n)

Optimal:
- Use a stack for operands
- When seeing an operator, pop two operands, apply operation, push result
- When seeing a number, push to stack
- The last element in stack is the final result
- Key Insight: RPN naturally evaluates with a stack
- Time: O(n)  |  Space: O(n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Reverse Polish Notation is designed for stack-based evaluation. We iterate
through tokens: when we see a number, push it; when we see an operator, pop
two operands, apply the operation, and push the result back. At the end,
the stack contains the final answer."

"""
from typing import List


# ─── Brute Force ───
class BruteForceSolution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Recursive evaluation with string manipulation.
        """
        tokens = tokens[:]
        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in "+-*/":
                    a, op, b = int(tokens[i-2]), tokens[i], int(tokens[i-1])
                    if op == "+":
                        result = a + b
                    elif op == "-":
                        result = a - b
                    elif op == "*":
                        result = a * b
                    else:
                        result = int(a / b)
                    tokens = tokens[:i-2] + [str(result)] + tokens[i+1:]
                    break
        return int(tokens[0])


# ─── Optimal ───
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Use stack to evaluate RPN - O(n) time.
        """
        stack = []
        operators = {"+", "-", "*", "/"}
        
        for token in tokens:
            if token in operators:
                # Pop two operands (note the order matters for - and /)
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    result = a + b
                elif token == "-":
                    result = a - b
                elif token == "*":
                    result = a * b
                else:
                    # Integer division towards zero
                    result = int(a / b)
                
                stack.append(result)
            else:
                # It's a number
                stack.append(int(token))
        
        return stack[0]


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Simple addition and multiplication
    assert sol.evalRPN(["2", "1", "+", "2", "*"]) == 6
    
    # Test 2: Division and subtraction
    assert sol.evalRPN(["4", "13", "5", "/", "+"]) == 6
    
    # Test 3: Single number
    assert sol.evalRPN(["42"]) == 42
    
    # Test 4: Complex expression
    assert sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    
    print("All tests passed!")
