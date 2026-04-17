"""
Problem: Subsets
LeetCode #: 78
Difficulty: Medium
URL: https://leetcode.com/problems/subsets/

Pattern: Backtracking
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Iterate through all 2^n possible subsets using bit manipulation
- Time: O(2^n)  |  Space: O(2^n)

Optimal:
- Backtracking: for each element, decide include or exclude
- Build all combinations recursively
- Key Insight: Each number either is or isn't in a subset
- Time: O(2^n)  |  Space: O(2^n)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"To generate all subsets, we use backtracking. For each number, we have
two choices: include it in the subset or exclude it. We recursively explore
both choices. The base case is when we've considered all numbers - then
we add the current subset to our result."

"""
from typing import List


# ─── Brute Force ───
class BruteForceSolution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Bit manipulation to generate all 2^n subsets.
        """
        result = []
        n = len(nums)
        
        # Iterate through all 2^n combinations
        for i in range(1 << n):  # 2^n combinations
            subset = []
            for j in range(n):
                # Check if j-th bit is set
                if i & (1 << j):
                    subset.append(nums[j])
            result.append(subset)
        
        return result


# ─── Optimal ───
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Backtracking - O(2^n) time.
        """
        result = []
        
        def backtrack(index, current):
            # Add current subset to result
            result.append(current[:])
            
            # Try adding each remaining number
            for i in range(index, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()
        
        backtrack(0, [])
        return result


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard case
    result1 = sol.subsets([1, 2, 3])
    assert len(result1) == 8
    assert [] in result1
    assert [1, 2, 3] in result1
    
    # Test 2: Single element
    result2 = sol.subsets([0])
    assert result2 == [[], [0]]
    
    # Test 3: Two elements
    result3 = sol.subsets([1, 2])
    assert len(result3) == 4
    
    # Test 4: Empty
    result4 = sol.subsets([])
    assert result4 == [[]]
    
    print("All tests passed!")
