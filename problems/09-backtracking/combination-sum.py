"""
Problem: Combination Sum
LeetCode #: 39
Difficulty: Medium
URL: https://leetcode.com/problems/combination-sum/

Pattern: Backtracking
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Generate all subsets and filter those that sum to target
- Time: O(2^n)  |  Space: O(n)

Optimal:
- Backtracking with pruning and reuse
- Each number can be used multiple times
- Prune when remaining sum becomes negative
- Key Insight: Start from same index to allow reuse
- Time: O(N^(T/M)) where T=target, M=min element  |  Space: O(T/M)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"We need to find all combinations that sum to the target. Since numbers can
be reused, we use backtracking. For each number, we decide how many times to
include it. We track the remaining sum and stop when it reaches 0. When the
sum becomes negative, we prune that branch."

"""
from typing import List


# ─── Brute Force ───
class BruteForceSolution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Generate all subsets and filter.
        """
        result = []
        n = len(candidates)
        
        def generate_subsets(index, current, current_sum):
            if current_sum == target:
                result.append(current[:])
                return
            if current_sum > target:
                return
            
            for i in range(index, n):
                current.append(candidates[i])
                generate_subsets(i, current, current_sum + candidates[i])
                current.pop()
        
        generate_subsets(0, [], 0)
        return result


# ─── Optimal ───
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Backtracking with pruning - O(N^(T/M)) time.
        """
        result = []
        
        def backtrack(index, current, remaining):
            # Found a valid combination
            if remaining == 0:
                result.append(current[:])
                return
            
            # Prune: remaining sum is negative
            if remaining < 0:
                return
            
            # Try each candidate starting from index
            for i in range(index, len(candidates)):
                current.append(candidates[i])
                # Can reuse same number, so pass i not i+1
                backtrack(i, current, remaining - candidates[i])
                current.pop()
        
        backtrack(0, [], target)
        return result


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard case
    result1 = sol.combinationSum([2, 3, 6, 7], 7)
    assert [7] in result1
    assert [2, 2, 3] in result1
    assert len(result1) == 2
    
    # Test 2: Single solution
    result2 = sol.combinationSum([2], 1)
    assert result2 == []
    
    # Test 3: Multiple solutions
    result3 = sol.combinationSum([2, 3, 5], 8)
    assert len(result3) > 0
    
    # Test 4: Exact match
    result4 = sol.combinationSum([1], 1)
    assert result4 == [[1]]
    
    print("All tests passed!")
