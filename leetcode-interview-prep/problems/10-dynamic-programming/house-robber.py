"""
Problem: House Robber
LeetCode #: 198
Difficulty: Medium
URL: https://leetcode.com/problems/house-robber/

Pattern: Dynamic Programming
Companies: Google, Amazon, Microsoft, Apple, Meta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Brute Force:
- Try all combinations of non-adjacent houses
- Time: O(2^n)  |  Space: O(n)

Optimal:
- DP: dp[i] = max money robbing houses 0..i
- Choice: rob house i or skip it
- dp[i] = max(dp[i-1], dp[i-2] + nums[i])
- Key Insight: Track best result from previous decisions
- Time: O(n)  |  Space: O(1)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTERVIEW SCRIPT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"At each house, we decide to rob it or skip it. If we rob house i, we get
its money plus the best result from houses up to i-2. If we skip, we get
the best result from houses up to i-1. The maximum is our best strategy.
Only need to track last two values for space optimization."

"""
from typing import List


# ─── Brute Force ───
class BruteForceSolution:
    def rob(self, nums: List[int]) -> int:
        """
        Recursion with memoization on subsets.
        """
        memo = {}
        
        def helper(index):
            if index >= len(nums):
                return 0
            if index in memo:
                return memo[index]
            
            # Rob this house or skip it
            rob_current = nums[index] + helper(index + 2)
            skip_current = helper(index + 1)
            result = max(rob_current, skip_current)
            memo[index] = result
            return result
        
        return helper(0)


# ─── Optimal ───
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        DP with O(1) space - O(n) time.
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # prev2 = max money robbing up to i-2
        # prev1 = max money robbing up to i-1
        prev2, prev1 = 0, nums[0]
        
        for i in range(1, len(nums)):
            # Rob current house + best from i-2, or skip current + best from i-1
            current = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = current
        
        return prev1


# ─── Test Cases ───
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Multiple houses
    assert sol.rob([1, 2, 3, 1]) == 4
    
    # Test 2: Different pattern
    assert sol.rob([2, 7, 9, 3, 1]) == 12
    
    # Test 3: Single house
    assert sol.rob([5]) == 5
    
    # Test 4: Two houses
    assert sol.rob([1, 3]) == 3
    
    print("All tests passed!")
